"""This file defines the PreTrainedModel class."""
import pathlib
import typing

import humanize
import numpy as np
from absl import flags
from absl import logging

from clgen import samplers
from clgen import telemetry
from clgen.corpuses import atomizers
from clgen.models import keras_backend
from clgen.models import tensorflow_backend
from clgen.proto import internal_pb2
from clgen.proto import model_pb2
from clgen.proto import telemetry_pb2
from labm8 import cache
from labm8 import labdate
from labm8 import pbutil


FLAGS = flags.FLAGS


class PreTrainedModel(object):
	"""A pre-trained model is a model which can be used only for inference."""

	def __init__(self, path: pathlib.Path):
		self.path = path.absolute()
		self.cache = cache.FSCache(self.path)
		self.corpus = NullCorpus()
		self.config = pbutil.FromFile(
				self.path / 'META.pbtxt', internal_pb2.ModelMeta()).config
		self.atomizer = atomizers.AtomizerBase.FromFile(self.path / 'atomizer')
		self.backend = {
			model_pb2.NetworkArchitecture.TENSORFLOW: tensorflow_backend.TensorFlowBackend,
			model_pb2.NetworkArchitecture.KERAS: keras_backend.KerasBackend,
		}[self.config.architecture.backend](self.config, self.cache, self.atomizer)


	def Train(self):
		"""The training process for a pre-trained model is a no-op."""
		pass

	def TrainingTelemetry(self) -> typing.List[telemetry_pb2.ModelEpochTelemetry]:
		"""Get the training telemetry data."""
		return telemetry.TrainingLogger(self.cache.path / 'logs').EpochTelemetry()

	def Sample(
			self, sampler: samplers.Sampler, min_num_samples: int,
			seed: int = None) -> typing.Iterable[model_pb2.Sample]:
		"""Sample a model.

		If the model is not already trained, calling Sample() first trains the
		model. Thus a call to Sample() is equivalent to calling Train() then
		Sample().

		Args:
			sampler: The sampler to sample using.
			min_num_samples: The minimum number of samples to return. Note that the
				true number of samples returned may be higher than this value, as
				sampling occurs in batches. The model will continue producing samples
				until the lowest mulitple of the sampler batch size property that is
				larger than this value. E.g. if min_num_samples is 7 and the Sampler
				batch size is 10, 10 samples will be returned.
			seed: A numeric value to seed the RNG with. If not present, the RNG is
				seeded randomly.

		Returns:
			A iterator over samples.

		Raises:
			UnableToAcquireLockError: If the model is locked (i.e. there is another
				process currently modifying the model).
			InvalidStartText: If the sampler start text cannot be encoded.
			InvalidSymtokTokens: If the sampler symmetrical depth tokens cannot be
				encoded.
		"""
		sample_count = 1
		self.SamplerCache(sampler).mkdir(exist_ok=True)
		atomizer = self.atomizer
		sampler.Specialize(atomizer)
		batch_size = self.backend.InitSampling(sampler, seed)
		sample_start_time = labdate.MillisecondsTimestamp()
		samples=[]
		sample_dir = self.SamplerCache(sampler)
		print("batch Size : "+str(batch_size))
		if(FLAGS.sampling_technique.split(" ")[0]  in ["topK", "nucleus" ,"beam", "default"]):
			logging.info('Sampling technique set to :  %s with value : %s ', FLAGS.sampling_technique.split(" ")[0] ,FLAGS.sampling_technique.split(" ")[1] )
		else:
			logging.info('Sampling technique set to :  default')

		# Per-sample batch outer loop. Continues until we have as many samples
		# as we want.
		while True:
			samples_in_progress = [
				sampler.tokenized_start_text.copy()
				for _ in range(batch_size)]
			done = np.zeros(batch_size, dtype=np.bool)
			start_time = labdate.MillisecondsTimestamp()
			wall_time_start = start_time


			self.backend.InitSampleBatch(sampler, batch_size)

			# Sampling loop. Continues until all samples in the batch are done.
			while True:
				indices = self.backend.SampleNextIndices(sampler, batch_size)
				
				# Iterate over all samples in batch to determine whether they're
				# done.
				print
				for i in range(batch_size):
					#print("batch_size : "+ str(i)+" :"+ str(batch_size)+" num_tokens : "+str(len(samples_in_progress[i])))
					if done[i]:
						continue

					token = atomizer.decoder[indices[i]]
					samples_in_progress[i].append(token)

					if sampler.SampleIsComplete(samples_in_progress[i]):
						end_time = labdate.MillisecondsTimestamp()
						done[i] = 1
						sample = model_pb2.Sample(
								text=''.join(samples_in_progress[i]),
								sample_start_epoch_ms_utc=start_time,
								sample_time_ms=end_time - start_time,
								wall_time_ms=end_time - wall_time_start,
								num_tokens=len(samples_in_progress[i]))
						print(f'=== BEGIN SIMULINK MDL SAMPLE (Pretrained Model){sample_count} ')
										#f'===\n\n{sample.text}\n')
						sample_count += 1
						sample_path = sample_dir / f'Sample{sample_count}.mdl'
						pbutil.ToFile(sample, sample_path)
						if min_num_samples > 0:
							samples.append(sample)
						wall_time_start = labdate.MillisecondsTimestamp()

				# Complete the batch.
				if done.all():
					break

			# Complete sampling. Note that sample_count starts at 1.
			if sample_count > min_num_samples:
				now = labdate.MillisecondsTimestamp()
				logging.info(
						'Produced %s samples at a rate of %s ms / sample.',
						humanize.intcomma(sample_count - 1),
						humanize.intcomma(
								int((now - sample_start_time) / max(sample_count - 1, 1))))
				break
		return samples
	
	def SamplerCache(self, sampler: samplers.Sampler) -> pathlib.Path:
		"""Get the path to a sampler cache.

		Args:
			sampler: A Sampler instance.

		Returns:
			A path to a directory. Note that this directory may not exist - it is
			created only after a call to Sample().
		"""
		return self.cache.path / 'samples' / sampler.hash




class NullCorpus(object):
	"""Corpus for a pre-trained model."""

	def Create(self):
		"""The creation process for a null corpus is a no-op."""
		pass

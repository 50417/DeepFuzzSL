# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clgen/proto/internal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clgen.proto import corpus_pb2 as clgen_dot_proto_dot_corpus__pb2
from clgen.proto import model_pb2 as clgen_dot_proto_dot_model__pb2
from clgen.proto import sampler_pb2 as clgen_dot_proto_dot_sampler__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='clgen/proto/internal.proto',
  package='clgen',
  syntax='proto2',
  serialized_options=_b('\n\022deeplearning.clgenB\016InternalProtos'),
  serialized_pb=_b('\n\x1a\x63lgen/proto/internal.proto\x12\x05\x63lgen\x1a\x18\x63lgen/proto/corpus.proto\x1a\x17\x63lgen/proto/model.proto\x1a\x19\x63lgen/proto/sampler.proto\"G\n\nCorpusMeta\x12\x1d\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\r.clgen.Corpus\x12\x1a\n\x12preprocess_time_ms\x18\x02 \x01(\x05\")\n\tModelMeta\x12\x1c\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x0c.clgen.Model\"-\n\x0bSamplerMeta\x12\x1e\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x0e.clgen.Sampler\"S\n\x15PreprocessorWorkerJob\x12\x16\n\x0e\x63ontentfile_id\x18\x01 \x01(\t\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\x15\n\rpreprocessors\x18\x03 \x03(\t\"\xa0\x01\n\x1cPreprocessorWorkerJobOutcome\x12\x16\n\x0e\x63ontentfile_id\x18\x01 \x01(\t\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t\x12:\n\x06status\x18\x03 \x01(\x0e\x32*.clgen.PreprocessorWorkerJobOutcome.Status\"\x1a\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"V\n\x12PreprocessorWorker\x12\x18\n\x10\x63ontentfile_root\x18\x01 \x01(\t\x12\x0f\n\x07relpath\x18\x02 \x01(\t\x12\x15\n\rpreprocessors\x18\x03 \x03(\t\"b\n\rEncoderWorker\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x1d\n\x15\x63ontentfile_separator\x18\x04 \x01(\t\x12\x18\n\x10pickled_atomizer\x18\x05 \x01(\x0c\"\x90\x01\n\x0fJavaRewriterJob\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x0b\n\x03src\x18\x02 \x01(\t\x12-\n\x06status\x18\x03 \x01(\x0e\x32\x1d.clgen.JavaRewriterJob.Status\x12\x12\n\nstatus_msg\x18\x04 \x01(\t\"\x1a\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x42$\n\x12\x64\x65\x65plearning.clgenB\x0eInternalProtos')
  ,
  dependencies=[clgen_dot_proto_dot_corpus__pb2.DESCRIPTOR,clgen_dot_proto_dot_model__pb2.DESCRIPTOR,clgen_dot_proto_dot_sampler__pb2.DESCRIPTOR,])



_PREPROCESSORWORKERJOBOUTCOME_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='clgen.PreprocessorWorkerJobOutcome.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=498,
  serialized_end=524,
)
_sym_db.RegisterEnumDescriptor(_PREPROCESSORWORKERJOBOUTCOME_STATUS)

_JAVAREWRITERJOB_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='clgen.JavaRewriterJob.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=498,
  serialized_end=524,
)
_sym_db.RegisterEnumDescriptor(_JAVAREWRITERJOB_STATUS)


_CORPUSMETA = _descriptor.Descriptor(
  name='CorpusMeta',
  full_name='clgen.CorpusMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='clgen.CorpusMeta.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preprocess_time_ms', full_name='clgen.CorpusMeta.preprocess_time_ms', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=186,
)


_MODELMETA = _descriptor.Descriptor(
  name='ModelMeta',
  full_name='clgen.ModelMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='clgen.ModelMeta.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=229,
)


_SAMPLERMETA = _descriptor.Descriptor(
  name='SamplerMeta',
  full_name='clgen.SamplerMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='clgen.SamplerMeta.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=276,
)


_PREPROCESSORWORKERJOB = _descriptor.Descriptor(
  name='PreprocessorWorkerJob',
  full_name='clgen.PreprocessorWorkerJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentfile_id', full_name='clgen.PreprocessorWorkerJob.contentfile_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src', full_name='clgen.PreprocessorWorkerJob.src', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preprocessors', full_name='clgen.PreprocessorWorkerJob.preprocessors', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=361,
)


_PREPROCESSORWORKERJOBOUTCOME = _descriptor.Descriptor(
  name='PreprocessorWorkerJobOutcome',
  full_name='clgen.PreprocessorWorkerJobOutcome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentfile_id', full_name='clgen.PreprocessorWorkerJobOutcome.contentfile_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='clgen.PreprocessorWorkerJobOutcome.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='clgen.PreprocessorWorkerJobOutcome.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREPROCESSORWORKERJOBOUTCOME_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=524,
)


_PREPROCESSORWORKER = _descriptor.Descriptor(
  name='PreprocessorWorker',
  full_name='clgen.PreprocessorWorker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentfile_root', full_name='clgen.PreprocessorWorker.contentfile_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relpath', full_name='clgen.PreprocessorWorker.relpath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preprocessors', full_name='clgen.PreprocessorWorker.preprocessors', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=612,
)


_ENCODERWORKER = _descriptor.Descriptor(
  name='EncoderWorker',
  full_name='clgen.EncoderWorker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clgen.EncoderWorker.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='clgen.EncoderWorker.text', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentfile_separator', full_name='clgen.EncoderWorker.contentfile_separator', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pickled_atomizer', full_name='clgen.EncoderWorker.pickled_atomizer', index=3,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=712,
)


_JAVAREWRITERJOB = _descriptor.Descriptor(
  name='JavaRewriterJob',
  full_name='clgen.JavaRewriterJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='clgen.JavaRewriterJob.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src', full_name='clgen.JavaRewriterJob.src', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='clgen.JavaRewriterJob.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_msg', full_name='clgen.JavaRewriterJob.status_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JAVAREWRITERJOB_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=859,
)

_CORPUSMETA.fields_by_name['config'].message_type = clgen_dot_proto_dot_corpus__pb2._CORPUS
_MODELMETA.fields_by_name['config'].message_type = clgen_dot_proto_dot_model__pb2._MODEL
_SAMPLERMETA.fields_by_name['config'].message_type = clgen_dot_proto_dot_sampler__pb2._SAMPLER
_PREPROCESSORWORKERJOBOUTCOME.fields_by_name['status'].enum_type = _PREPROCESSORWORKERJOBOUTCOME_STATUS
_PREPROCESSORWORKERJOBOUTCOME_STATUS.containing_type = _PREPROCESSORWORKERJOBOUTCOME
_JAVAREWRITERJOB.fields_by_name['status'].enum_type = _JAVAREWRITERJOB_STATUS
_JAVAREWRITERJOB_STATUS.containing_type = _JAVAREWRITERJOB
DESCRIPTOR.message_types_by_name['CorpusMeta'] = _CORPUSMETA
DESCRIPTOR.message_types_by_name['ModelMeta'] = _MODELMETA
DESCRIPTOR.message_types_by_name['SamplerMeta'] = _SAMPLERMETA
DESCRIPTOR.message_types_by_name['PreprocessorWorkerJob'] = _PREPROCESSORWORKERJOB
DESCRIPTOR.message_types_by_name['PreprocessorWorkerJobOutcome'] = _PREPROCESSORWORKERJOBOUTCOME
DESCRIPTOR.message_types_by_name['PreprocessorWorker'] = _PREPROCESSORWORKER
DESCRIPTOR.message_types_by_name['EncoderWorker'] = _ENCODERWORKER
DESCRIPTOR.message_types_by_name['JavaRewriterJob'] = _JAVAREWRITERJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CorpusMeta = _reflection.GeneratedProtocolMessageType('CorpusMeta', (_message.Message,), dict(
  DESCRIPTOR = _CORPUSMETA,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.CorpusMeta)
  ))
_sym_db.RegisterMessage(CorpusMeta)

ModelMeta = _reflection.GeneratedProtocolMessageType('ModelMeta', (_message.Message,), dict(
  DESCRIPTOR = _MODELMETA,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.ModelMeta)
  ))
_sym_db.RegisterMessage(ModelMeta)

SamplerMeta = _reflection.GeneratedProtocolMessageType('SamplerMeta', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLERMETA,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.SamplerMeta)
  ))
_sym_db.RegisterMessage(SamplerMeta)

PreprocessorWorkerJob = _reflection.GeneratedProtocolMessageType('PreprocessorWorkerJob', (_message.Message,), dict(
  DESCRIPTOR = _PREPROCESSORWORKERJOB,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.PreprocessorWorkerJob)
  ))
_sym_db.RegisterMessage(PreprocessorWorkerJob)

PreprocessorWorkerJobOutcome = _reflection.GeneratedProtocolMessageType('PreprocessorWorkerJobOutcome', (_message.Message,), dict(
  DESCRIPTOR = _PREPROCESSORWORKERJOBOUTCOME,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.PreprocessorWorkerJobOutcome)
  ))
_sym_db.RegisterMessage(PreprocessorWorkerJobOutcome)

PreprocessorWorker = _reflection.GeneratedProtocolMessageType('PreprocessorWorker', (_message.Message,), dict(
  DESCRIPTOR = _PREPROCESSORWORKER,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.PreprocessorWorker)
  ))
_sym_db.RegisterMessage(PreprocessorWorker)

EncoderWorker = _reflection.GeneratedProtocolMessageType('EncoderWorker', (_message.Message,), dict(
  DESCRIPTOR = _ENCODERWORKER,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.EncoderWorker)
  ))
_sym_db.RegisterMessage(EncoderWorker)

JavaRewriterJob = _reflection.GeneratedProtocolMessageType('JavaRewriterJob', (_message.Message,), dict(
  DESCRIPTOR = _JAVAREWRITERJOB,
  __module__ = 'clgen.proto.internal_pb2'
  # @@protoc_insertion_point(class_scope:clgen.JavaRewriterJob)
  ))
_sym_db.RegisterMessage(JavaRewriterJob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

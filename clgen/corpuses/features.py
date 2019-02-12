"""OpenCL feature extraction."""
import csv
import os
import re
import sys
from collections import OrderedDict
from io import StringIO, open
from subprocess import PIPE, Popen
from typing import List, TextIO

import numpy as np

from deeplearning.clgen import errors
from labm8 import bazelutil
from labm8 import labmath


CLGEN_FEATURES = bazelutil.DataPath(
    'phd/deeplearning/clgen/corpuses/opencl_kernel_features')
SHIMFILE = bazelutil.DataPath(
    'phd/deeplearning/clgen/data/include/opencl-shim.h')

# On Linux we must preload the LLVM sharded libraries.
CLGEN_FEATURES_ENV = os.environ.copy()
_LIBCLANG_SO = bazelutil.DataPath(
    f'llvm_linux/lib/libclang.so', must_exist=False)
_LIBLTO_SO = bazelutil.DataPath(
    f'llvm_linux/lib/libLTO.so', must_exist=False)
if _LIBCLANG_SO.is_file() and _LIBLTO_SO.is_file():
  CLGEN_FEATURES_ENV['LD_PRELOAD'] = f'{_LIBCLANG_SO}:{_LIBLTO_SO}'


class FeatureExtractionError(errors.CLgenError):
  """ Thrown in case feature extraction fails """
  pass


def _shim_args(use_shim: bool = False) -> list:
  """get shim header args"""
  args = []
  if use_shim:
    args += ["-DCLGEN_FEATURES", "-include", str(SHIMFILE)]
  return args


def _is_features(line: str) -> bool:
  """true if features"""
  return len(line) == 10


def _is_good_features(line: str, stderr: str) -> bool:
  """true if feature extractor worked"""
  if _is_features(line):
    has_err = False if stderr.find(' error: ') == -1 else True
    return not has_err
  return False


def to_np_arrays(paths: List[str], **kwargs):
  """
  Returns a list of numpy arrays for features in kernels in files.

  Parameters
  ----------
  path : List[str]
      List of file paths.
  **kwargs
      Arguments to features()

  Raises
  ------
  FeatureExtractionError
      In case feature extraction fails.
  """

  def _process_file(path: str, **kwargs):
    buf = StringIO()
    features(path=path, file=buf, **kwargs)
    ret = buf.getvalue()
    try:
      # last line is empty:
      lines = ret.split('\n')[:-1]
      # first two cols are ignored (path and kernel names):
      parse = lambda l: np.array([float(x) for x in l.split(',')[2:]])
      return [parse(line) for line in lines]
    except IndexError:
      raise FeatureExtractionError

  flatten = lambda l: [item for sublist in l for item in sublist]
  return flatten([_process_file(path, **kwargs) for path in paths])


# FIXME(polyglot): Add support for multiple languages.
def features(path: str, file=sys.stdout, fatal_errors: bool = False,
             use_shim: bool = False, quiet: bool = False) -> None:
  """
  Print CSV format features of file.

  Parameters
  ----------
  path : str
      Path.
  file : pipe, optional
      Target to print to.
  fatal_errors : bool, optional
      Exit on error.
  use_shim : bool, optional
      Inject shim header.
  quiet : bool, optional
      Don't print compiler output on errors.
  """
  cmd = [str(CLGEN_FEATURES), path] + ['-extra-arg=' + x for x in
                                       _shim_args(use_shim=use_shim)]
  process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                  env=CLGEN_FEATURES_ENV)
  stdout, stderr = process.communicate()
  stdout, stderr = stdout.decode('utf-8'), stderr.decode('utf-8')

  data = [line.split(',') for line in stdout.split('\n')]

  if stderr:
    has_error = re.search(" error: ", stderr)
    if has_error:
      if quiet:
        print("error:", path, file=sys.stderr)
      else:
        print("=== COMPILER OUTPUT FOR", path, "===", file=sys.stderr)
        print(stderr, file=sys.stderr)
    if fatal_errors and has_error:
      sys.exit(1)

  if process.returncode != 0:
    print("error: compiler crashed on '{}'".format(path), file=sys.stderr)
    return

  for line in data[1:]:
    if _is_good_features(line, stderr):
      print(','.join(line), file=file)


def feature_headers(file: TextIO = sys.stdout) -> None:
  """
  Print CSV format feature header.

  Parameters
  ----------
  file : TextIO, optional
      Target to print to.
  """
  cmd = [str(CLGEN_FEATURES), '-header-only']
  process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                  env=CLGEN_FEATURES_ENV)
  stdout, _ = process.communicate()
  stdout = stdout.decode('utf-8').strip()

  print(stdout, file=file)


def files(paths: List[str], header: bool = True, file: TextIO = sys.stdout,
          **kwargs) -> None:
  """
  Print feature values of files in CSV format.

  Parameters
  ----------
  paths : List[str]
      Files.
  header : bool, optional
      Include CSV format header.
  file : TextIO, optional
      Target to print to.
  **kwargs
      Additional arguments to features().
  """
  if header:
    feature_headers(file=file)
  for path in paths:
    print(path, file=sys.stderr)
    features(path, file=file, **kwargs)


def summarize(csv_path: str) -> OrderedDict:
  """
  Summarize a CSV file of feature values.

  Parameters
  ----------
  csv_path : str
      Path to csv.

  Returns
  -------
  OrderedDict
      Summary values.
  """
  with open(csv_path) as infile:
    reader = csv.reader(infile)
    table = [row for row in reader]

  d = OrderedDict()
  ignored_cols = 2
  d['datapoints'] = len(table) - 1
  for i, col in enumerate(table[0][ignored_cols:]):
    i += ignored_cols
    d[col] = labmath.mean([float(r[i]) for r in table[1:]])

  return d

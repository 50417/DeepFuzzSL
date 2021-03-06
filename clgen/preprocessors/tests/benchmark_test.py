"""Benchmarks for the preprocessing pipeline."""
import sys
import typing

import pytest
from absl import app
from absl import flags
from absl import logging

from deeplearning.clgen import errors
from deeplearning.clgen.preprocessors import preprocessors


FLAGS = flags.FLAGS

# A full preprocessing pipeline for the C++ programming language.
CXX_PREPROCESSORS = ['deeplearning.clgen.preprocessors.cxx:ClangPreprocess',
                     'deeplearning.clgen.preprocessors.cxx:Compile',
                     'deeplearning.clgen.preprocessors.cxx'
                     ':NormalizeIdentifiers',
                     'deeplearning.clgen.preprocessors.common'
                     ':StripDuplicateEmptyLines',
                     'deeplearning.clgen.preprocessors.common'
                     ':MinimumLineCount3',
                     'deeplearning.clgen.preprocessors.common'
                     ':StripTrailingWhitespace',
                     'deeplearning.clgen.preprocessors.cxx:ClangFormat', ]
# A full preprocessing pipeline for the OpenCL programming language.
OPENCL_PREPROCESSORS = [
  'deeplearning.clgen.preprocessors.opencl:ClangPreprocessWithShim',
  'deeplearning.clgen.preprocessors.opencl:Compile',
  'deeplearning.clgen.preprocessors.opencl:NormalizeIdentifiers',
  'deeplearning.clgen.preprocessors.opencl:StripDoubleUnderscorePrefixes',
  'deeplearning.clgen.preprocessors.common:StripDuplicateEmptyLines',
  'deeplearning.clgen.preprocessors.opencl:SanitizeKernelPrototype',
  'deeplearning.clgen.preprocessors.common:StripTrailingWhitespace',
  'deeplearning.clgen.preprocessors.opencl:ClangFormat',
  'deeplearning.clgen.preprocessors.common:MinimumLineCount3', ]


def _PreprocessBenchmarkInnerLoop(preprocessors_: typing.List[str],
                                  code_in: str, code_out: str):
  """Benchmark inner loop for code with expected output."""
  assert preprocessors.Preprocess(code_in, preprocessors_) == code_out


def _PreprocessBenchmarkInnerLoopBadCode(preprocessors_: typing.List[str],
                                         code_in):
  """Benchmark inner loop for bad code."""
  with pytest.raises(errors.BadCodeException):
    preprocessors.Preprocess(code_in, preprocessors_)


def test_benchmark_cxx_small_program(benchmark):
  """Benchmark preprocessing a C++ program using a full pipeline."""
  code_in = """
#include <iostream>

int do_something(int a) { return a * 2; }


int main(int argc, char **argv) { return do_something(argc); }
"""
  code_out = """\
int A(int a) {
  return a * 2;
}

int B(int a, char** b) {
  return A(a);
}\
"""
  benchmark(_PreprocessBenchmarkInnerLoop, CXX_PREPROCESSORS, code_in, code_out)


def test_benchmark_cxx_invalid_syntax(benchmark):
  """Benchmark preprocessing a C++ program with syntax errors."""
  benchmark(_PreprocessBenchmarkInnerLoopBadCode, CXX_PREPROCESSORS,
            'inva@asd!!!')


def test_benchmark_opencl_small_program(benchmark):
  """Benchmark preprocessing an OpenCL kernel using a full pipeline."""
  code_in = """
__kernel void foo(__global float* a, const int b) {
  int id = get_global_id(0);
  if (id <= b)
    a[id] = 0;
}
"""
  code_out = """\
kernel void A(global float* a, const int b) {
  int c = get_global_id(0);
  if (c <= b)
    a[c] = 0;
}\
"""
  benchmark(_PreprocessBenchmarkInnerLoop, OPENCL_PREPROCESSORS, code_in,
            code_out)


def test_benchmark_opencl_invalid_syntax(benchmark):
  """Benchmark preprocessing an OpenCL program with syntax errors."""
  benchmark(_PreprocessBenchmarkInnerLoopBadCode, OPENCL_PREPROCESSORS,
            'inva@asd!!!')


def main(argv):
  """Main entry point."""
  if len(argv) > 1:
    raise app.UsageError('Unrecognized command line flags.')
  logging.set_verbosity(logging.DEBUG)
  sys.exit(pytest.main([__file__, '-vv']))


if __name__ == '__main__':
  app.run(main)

"""Preprocess OpenCL files for machine learning."""
import importlib
import typing
from io import open

from absl import flags

from clgen import errors
from clgen.preprocessors import public


FLAGS = flags.FLAGS


def GetPreprocessorFunction(name: str) -> public.PreprocessorFunction:
  """Lookup a preprocess function by name.

  A preprocessor is a function which takes a single argument 'text' of type str,
  and returns a str. The name is the fully qualified name of the python
  function which implements it, in the form <module>:<name>. For example,
  the name 'preprocessors.cxx:Compile' will return the
  function 'Compile' in the module 'preprocessors.cxx'.

  Args:
    name: The name of the preprocessor to get.

  Returns:
    The python preprocessor function.

  Raises:
    UserError: If the requested name cannot be found or is not a
      @clgen_preprocessor decorated function.
  """
  components = name.split(':')
  if len(components) != 2:
    raise errors.UserError(f'Invalid preprocessor name {name}')
  module_name, function_name = components
  
  try:
    module = importlib.import_module(module_name)
    function_ = getattr(module, function_name)
  except (ModuleNotFoundError, AttributeError):
    raise errors.UserError(f'Preprocessor {name} not found.')
  if not function_.__dict__.get('is_clgen_preprocessor'):
    raise errors.UserError(
        f'Preprocessor {name} not decorated with @clgen_preprocessor')
  return function_


def Preprocess(text: str, preprocessors: typing.List[str]) -> str:
  """Preprocess a text using the given preprocessor pipeline.

  If preprocessing succeeds, the preprocessed text is returned. If preprocessing
  fails (in an expected way, for example by trying to compile incorrect code),
  a BadCodeException is raised. Any other error leads to an InternalError.


  Args:
    text: The input to be preprocessed.
    preprocessors: The list of preprocessor functions to run. These will be
      passed to GetPreprocessorFunction() to resolve the python implementations.

  Returns:
    Preprocessed source input as a string.

  Raises:
    UserError: If the requested preprocessors cannot be loaded.
    BadCodeException: If one of the preprocessors rejects the input.
    InternalException: In case of some other error.
  """
  preprocessor_functions = [GetPreprocessorFunction(p) for p in preprocessors]
  for preprocessor in preprocessor_functions:
    text = preprocessor(text)
  return text


def PreprocessFile(path: str, preprocessors: typing.List[str],
                   inplace: bool) -> str:
  """Preprocess a file and optionally update it.

  Args:
    text: The input to be preprocessed.
    preprocessors: The list of preprocessor functions to run. These will be
      passed to GetPreprocessorFunction() to resolve the python implementations.
    inplace: If True, the input file is overwritten with the preprocessed code,
      unless the preprocessing fails. If the preprocessing fails, the input
      file is left unmodified.

  Returns:
    Preprocessed source input as a string.

  Raises:
    UserError: If the requested preprocessors cannot be loaded.
    BadCodeException: If one of the preprocessors rejects the input.
    InternalException: In case of some other error.
  """
  with open(path) as infile:
    contents = infile.read()
  preprocessed = Preprocess(contents, preprocessors)
  if inplace:
    with open(path, 'w') as outfile:
      outfile.write(preprocessed)
  return preprocessed

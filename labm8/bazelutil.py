"""A module for working within Bazel's hemetic and sandboxed world.

The design goals of Bazel has led it to have a lot of quirks. This module
contains utility code designed to help live with these quirks.
"""
import os
import pathlib
import re
import typing

from config import getconfig


# Regular expression to everything in a path up until the '*.runfiles'
# directory, e.g. for the path '/private/var/bazel/foo/bar.runfiles/a/b/c',
# this regex will match '/private/var/bazel/foo/bar.runfiles'
RUNFILES_PATTERN = re.compile(r'^(.*\.runfiles)/')


def IsBazelSandbox() -> bool:
  """Determine if the current process is running in a bazel sandbox.

  Returns:
    True if the current process is running inside a bazel sandbox, else false.
  """
  config = getconfig.GetGlobalConfig()
  return not __file__.startswith(config.paths.repo_root)


def FindRunfilesDirectory() -> typing.Optional[pathlib.Path]:
  """Find the '.runfiles' directory, if there is one.

  Returns:
    The absolute path of the runfiles directory, else None if not found.
  """
  # Follow symlinks, looking for my module space
  stub_filename = os.path.abspath(__file__)
  module_space = stub_filename + '.runfiles'
  if os.path.isdir(module_space):
    return pathlib.Path(module_space)
  match = RUNFILES_PATTERN.match(os.path.abspath(__file__))
  if match:
    return pathlib.Path(match.group(1))
  return None


def DataPath(path: typing.Union[str, pathlib.Path],
             must_exist: bool = True) -> pathlib.Path:
  """Return the absolute path to a data file.

  This allows you to access files from the 'data' attribute of a Python
  target in Bazel. This is needed because the path to the file changes depending
  on whether the current process is executing with a 'bazel run' environment, or
  as a 'bazel-bin' script.

  Args:
    path: The path to the data, including the name of the workspace.
    must_exist: Require that the file exists, else raise FileNotFoundError.

  Returns:
    An absolute file path.

  Raises:
    FileNotFoundError: If the requested path is not found and must_exist is
      True.
  """
  if not str(path):
    if must_exist:
      raise FileNotFoundError(f"No such file or directory: ''")
    else:
      # An empty path yields the runfiles directory.
      return FindRunfilesDirectory()
  runfiles = FindRunfilesDirectory()
  real_path = runfiles / path if runfiles else pathlib.Path(path).absolute()
  if must_exist and not (real_path.is_file() or real_path.is_dir()):
    raise FileNotFoundError(f"No such file or directory: '{path}'")
  return real_path

"""Unit tests for //config/config.py."""
import os
import pathlib
import subprocess
import sys

import pytest
from absl import app
from absl import flags

from config import getconfig


FLAGS = flags.FLAGS


def test_GetGlobalConfig_system_values():
  """Check that the repo config has all of the expected fields."""
  config = getconfig.GetGlobalConfig()
  assert config.HasField('uname')
  assert config.HasField('configure_id')
  assert config.HasField('with_cuda')
  assert config.options.HasField('with_cuda')
  assert config.options.HasField('update_git_submodules')
  assert config.paths.HasField('repo_root')
  assert config.paths.HasField('python')


def test_uname():
  """Test that uname is one of the expected values."""
  config = getconfig.GetGlobalConfig()
  assert config.uname in {'darwin', 'linux'}


def test_configure_id():
  """Test that the ID generated by configure has not changed.

  If this test fails, do not panic. It simply indicates that the you need to
  run ./configure again.
  """
  config = getconfig.GetGlobalConfig()
  configure_path = pathlib.Path(config.paths.repo_root) / 'configure'
  assert configure_path.is_file()

  def ToConfigureArg(field: str) -> str:
    """Turn an 'options' field into a --[no]arg ./configure argument."""
    return f'--{field}' if getattr(config.options, field) else f'--no{field}'

  args = [ToConfigureArg(f.name) for f in config.options.DESCRIPTOR.fields]
  cmd = [str(configure_path), '--print_id', '--noninteractive'] + args
  print('$', ' '.join(cmd))
  assert config.configure_id == subprocess.check_output(
      cmd, universal_newlines=True).rstrip()


def test_GlobalConfigPaths_repo_root():
  """Test that repo_root is a directory."""
  config = getconfig.GetGlobalConfig()
  assert pathlib.Path(config.paths.repo_root).is_dir()


def test_GlobalConfigPaths_python():
  """Test that python is an executable."""
  config = getconfig.GetGlobalConfig()
  assert pathlib.Path(config.paths.python).is_file()
  assert os.access(config.paths.python, os.X_OK)


def main(argv):
  """Main entry point."""
  del argv
  sys.exit(pytest.main([__file__, '-v']))


if __name__ == '__main__':
  app.run(main)

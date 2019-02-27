# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/proto/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config/proto/config.proto',
  package='phd',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63onfig/proto/config.proto\x12\x03phd\"\x98\x01\n\x0cGlobalConfig\x12\r\n\x05uname\x18\x01 \x02(\t\x12\x14\n\x0c\x63onfigure_id\x18\x02 \x02(\t\x12\x11\n\twith_cuda\x18\x64 \x02(\x08\x12)\n\x07options\x18\x03 \x02(\x0b\x32\x18.phd.GlobalConfigOptions\x12%\n\x05paths\x18\x04 \x02(\x0b\x32\x16.phd.GlobalConfigPaths\"_\n\x13GlobalConfigOptions\x12\x11\n\twith_cuda\x18\x01 \x02(\x08\x12\x1d\n\x15update_git_submodules\x18\x02 \x02(\x08\x12\x16\n\x0esymlink_python\x18\x03 \x02(\x08\"6\n\x11GlobalConfigPaths\x12\x11\n\trepo_root\x18\x01 \x02(\t\x12\x0e\n\x06python\x18\x02 \x02(\t')
)




_GLOBALCONFIG = _descriptor.Descriptor(
  name='GlobalConfig',
  full_name='phd.GlobalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uname', full_name='phd.GlobalConfig.uname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configure_id', full_name='phd.GlobalConfig.configure_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_cuda', full_name='phd.GlobalConfig.with_cuda', index=2,
      number=100, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='phd.GlobalConfig.options', index=3,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paths', full_name='phd.GlobalConfig.paths', index=4,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=35,
  serialized_end=187,
)


_GLOBALCONFIGOPTIONS = _descriptor.Descriptor(
  name='GlobalConfigOptions',
  full_name='phd.GlobalConfigOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='with_cuda', full_name='phd.GlobalConfigOptions.with_cuda', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_git_submodules', full_name='phd.GlobalConfigOptions.update_git_submodules', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symlink_python', full_name='phd.GlobalConfigOptions.symlink_python', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=189,
  serialized_end=284,
)


_GLOBALCONFIGPATHS = _descriptor.Descriptor(
  name='GlobalConfigPaths',
  full_name='phd.GlobalConfigPaths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_root', full_name='phd.GlobalConfigPaths.repo_root', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python', full_name='phd.GlobalConfigPaths.python', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=286,
  serialized_end=340,
)

_GLOBALCONFIG.fields_by_name['options'].message_type = _GLOBALCONFIGOPTIONS
_GLOBALCONFIG.fields_by_name['paths'].message_type = _GLOBALCONFIGPATHS
DESCRIPTOR.message_types_by_name['GlobalConfig'] = _GLOBALCONFIG
DESCRIPTOR.message_types_by_name['GlobalConfigOptions'] = _GLOBALCONFIGOPTIONS
DESCRIPTOR.message_types_by_name['GlobalConfigPaths'] = _GLOBALCONFIGPATHS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GlobalConfig = _reflection.GeneratedProtocolMessageType('GlobalConfig', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALCONFIG,
  __module__ = 'config.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:phd.GlobalConfig)
  ))
_sym_db.RegisterMessage(GlobalConfig)

GlobalConfigOptions = _reflection.GeneratedProtocolMessageType('GlobalConfigOptions', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALCONFIGOPTIONS,
  __module__ = 'config.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:phd.GlobalConfigOptions)
  ))
_sym_db.RegisterMessage(GlobalConfigOptions)

GlobalConfigPaths = _reflection.GeneratedProtocolMessageType('GlobalConfigPaths', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALCONFIGPATHS,
  __module__ = 'config.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:phd.GlobalConfigPaths)
  ))
_sym_db.RegisterMessage(GlobalConfigPaths)


# @@protoc_insertion_point(module_scope)

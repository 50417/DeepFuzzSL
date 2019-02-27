# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clgen/proto/clgen.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import model_pb2 as clgen_dot_proto_dot_model__pb2
from proto import sampler_pb2 as clgen_dot_proto_dot_sampler__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='clgen/proto/clgen.proto',
  package='clgen',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x63lgen/proto/clgen.proto\x12\x05\x63lgen\x1a\x17\x63lgen/proto/model.proto\x1a\x19\x63lgen/proto/sampler.proto\"\x92\x01\n\x08Instance\x12\x13\n\x0bworking_dir\x18\x01 \x01(\t\x12\x1d\n\x05model\x18\x02 \x01(\x0b\x32\x0c.clgen.ModelH\x00\x12\x1a\n\x10pretrained_model\x18\x04 \x01(\tH\x00\x12\x1f\n\x07sampler\x18\x03 \x01(\x0b\x32\x0e.clgen.SamplerB\x15\n\x13model_specification\".\n\tInstances\x12!\n\x08instance\x18\x01 \x03(\x0b\x32\x0f.clgen.Instance')
  ,
  dependencies=[clgen_dot_proto_dot_model__pb2.DESCRIPTOR,clgen_dot_proto_dot_sampler__pb2.DESCRIPTOR,])




_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='clgen.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='working_dir', full_name='clgen.Instance.working_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='clgen.Instance.model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pretrained_model', full_name='clgen.Instance.pretrained_model', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampler', full_name='clgen.Instance.sampler', index=3,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='model_specification', full_name='clgen.Instance.model_specification',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=87,
  serialized_end=233,
)


_INSTANCES = _descriptor.Descriptor(
  name='Instances',
  full_name='clgen.Instances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='clgen.Instances.instance', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=235,
  serialized_end=281,
)

_INSTANCE.fields_by_name['model'].message_type = clgen_dot_proto_dot_model__pb2._MODEL
_INSTANCE.fields_by_name['sampler'].message_type = clgen_dot_proto_dot_sampler__pb2._SAMPLER
_INSTANCE.oneofs_by_name['model_specification'].fields.append(
  _INSTANCE.fields_by_name['model'])
_INSTANCE.fields_by_name['model'].containing_oneof = _INSTANCE.oneofs_by_name['model_specification']
_INSTANCE.oneofs_by_name['model_specification'].fields.append(
  _INSTANCE.fields_by_name['pretrained_model'])
_INSTANCE.fields_by_name['pretrained_model'].containing_oneof = _INSTANCE.oneofs_by_name['model_specification']
_INSTANCES.fields_by_name['instance'].message_type = _INSTANCE
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['Instances'] = _INSTANCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCE,
  __module__ = 'clgen.proto.clgen_pb2'
  # @@protoc_insertion_point(class_scope:clgen.Instance)
  ))
_sym_db.RegisterMessage(Instance)

Instances = _reflection.GeneratedProtocolMessageType('Instances', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCES,
  __module__ = 'clgen.proto.clgen_pb2'
  # @@protoc_insertion_point(class_scope:clgen.Instances)
  ))
_sym_db.RegisterMessage(Instances)


# @@protoc_insertion_point(module_scope)

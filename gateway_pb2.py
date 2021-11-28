# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import celaut_pb2 as celaut__pb2
import buffer_pb2 as buffer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x12\x07gateway\x1a\x0c\x63\x65laut.proto\x1a\x0c\x62uffer.proto\"\x07\n\x05\x45mpty\"\x1d\n\x0cTokenMessage\x12\r\n\x05token\x18\x01 \x01(\t\"\x90\x01\n\x08Instance\x12\x30\n\rinstance_meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.MetadataH\x00\x88\x01\x01\x12\"\n\x08instance\x18\x02 \x01(\x0b\x32\x10.celaut.Instance\x12\x12\n\x05token\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_instance_metaB\x08\n\x06_token\"[\n\x0fServiceWithMeta\x12&\n\x08metadata\x18\x01 \x01(\x0b\x32\x14.celaut.Any.Metadata\x12 \n\x07service\x18\x02 \x01(\x0b\x32\x0f.celaut.Service\"h\n\x0eHashWithConfig\x12/\n\x04hash\x18\x01 \x01(\x0b\x32!.celaut.Any.Metadata.HashTag.Hash\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration\"e\n\x11ServiceWithConfig\x12)\n\x07service\x18\x02 \x01(\x0b\x32\x18.gateway.ServiceWithMeta\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration2t\n\x07Gateway\x12\x34\n\x0cStartService\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x33\n\x0bStopService\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[celaut__pb2.DESCRIPTOR,buffer__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='gateway.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=61,
)


_TOKENMESSAGE = _descriptor.Descriptor(
  name='TokenMessage',
  full_name='gateway.TokenMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.TokenMessage.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=92,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='gateway.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_meta', full_name='gateway.Instance.instance_meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='gateway.Instance.instance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.Instance.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_instance_meta', full_name='gateway.Instance._instance_meta',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_token', full_name='gateway.Instance._token',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=95,
  serialized_end=239,
)


_SERVICEWITHMETA = _descriptor.Descriptor(
  name='ServiceWithMeta',
  full_name='gateway.ServiceWithMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='gateway.ServiceWithMeta.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.ServiceWithMeta.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=332,
)


_HASHWITHCONFIG = _descriptor.Descriptor(
  name='HashWithConfig',
  full_name='gateway.HashWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='gateway.HashWithConfig.hash', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.HashWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=438,
)


_SERVICEWITHCONFIG = _descriptor.Descriptor(
  name='ServiceWithConfig',
  full_name='gateway.ServiceWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.ServiceWithConfig.service', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.ServiceWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=541,
)

_INSTANCE.fields_by_name['instance_meta'].message_type = celaut__pb2._ANY_METADATA
_INSTANCE.fields_by_name['instance'].message_type = celaut__pb2._INSTANCE
_INSTANCE.oneofs_by_name['_instance_meta'].fields.append(
  _INSTANCE.fields_by_name['instance_meta'])
_INSTANCE.fields_by_name['instance_meta'].containing_oneof = _INSTANCE.oneofs_by_name['_instance_meta']
_INSTANCE.oneofs_by_name['_token'].fields.append(
  _INSTANCE.fields_by_name['token'])
_INSTANCE.fields_by_name['token'].containing_oneof = _INSTANCE.oneofs_by_name['_token']
_SERVICEWITHMETA.fields_by_name['metadata'].message_type = celaut__pb2._ANY_METADATA
_SERVICEWITHMETA.fields_by_name['service'].message_type = celaut__pb2._SERVICE
_HASHWITHCONFIG.fields_by_name['hash'].message_type = celaut__pb2._ANY_METADATA_HASHTAG_HASH
_HASHWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
_SERVICEWITHCONFIG.fields_by_name['service'].message_type = _SERVICEWITHMETA
_SERVICEWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['TokenMessage'] = _TOKENMESSAGE
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['ServiceWithMeta'] = _SERVICEWITHMETA
DESCRIPTOR.message_types_by_name['HashWithConfig'] = _HASHWITHCONFIG
DESCRIPTOR.message_types_by_name['ServiceWithConfig'] = _SERVICEWITHCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Empty)
  })
_sym_db.RegisterMessage(Empty)

TokenMessage = _reflection.GeneratedProtocolMessageType('TokenMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMESSAGE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.TokenMessage)
  })
_sym_db.RegisterMessage(TokenMessage)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Instance)
  })
_sym_db.RegisterMessage(Instance)

ServiceWithMeta = _reflection.GeneratedProtocolMessageType('ServiceWithMeta', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHMETA,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ServiceWithMeta)
  })
_sym_db.RegisterMessage(ServiceWithMeta)

HashWithConfig = _reflection.GeneratedProtocolMessageType('HashWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _HASHWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.HashWithConfig)
  })
_sym_db.RegisterMessage(HashWithConfig)

ServiceWithConfig = _reflection.GeneratedProtocolMessageType('ServiceWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ServiceWithConfig)
  })
_sym_db.RegisterMessage(ServiceWithConfig)



_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='gateway.Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=543,
  serialized_end=659,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartService',
    full_name='gateway.Gateway.StartService',
    index=0,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopService',
    full_name='gateway.Gateway.StopService',
    index=1,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)

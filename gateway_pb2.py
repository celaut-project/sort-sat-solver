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


import ipss_pb2 as ipss__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x1a\nipss.proto\"V\n\x05Token\x12\x15\n\x0bvalue_int32\x18\x01 \x01(\x05H\x00\x12\x15\n\x0bvalue_int64\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cvalue_string\x18\x03 \x01(\tH\x00\x42\x07\n\x05oneOf\"\x07\n\x05\x45mpty\"C\n\x08Instance\x12 \n\x08instance\x18\x01 \x01(\x0b\x32\x0e.ipss.Instance\x12\x15\n\x05token\x18\x02 \x01(\x0b\x32\x06.Token\"\x8d\x01\n\x0fServiceExtended\x12\x1a\n\x04hash\x18\x01 \x01(\x0b\x32\n.ipss.HashH\x00\x12 \n\x07service\x18\x02 \x01(\x0b\x32\r.ipss.ServiceH\x00\x12(\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x13.ipss.ConfigurationH\x01\x88\x01\x01\x42\x07\n\x05oneOfB\t\n\x07_config2[\n\x07Gateway\x12/\n\x0cStartService\x12\x10.ServiceExtended\x1a\t.Instance\"\x00(\x01\x12\x1f\n\x0bStopService\x12\x06.Token\x1a\x06.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[ipss__pb2.DESCRIPTOR,])




_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_int32', full_name='Token.value_int32', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_int64', full_name='Token.value_int64', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_string', full_name='Token.value_string', index=2,
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
      name='oneOf', full_name='Token.oneOf',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=29,
  serialized_end=115,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=117,
  serialized_end=124,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='Instance.instance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='Instance.token', index=1,
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
  serialized_start=126,
  serialized_end=193,
)


_SERVICEEXTENDED = _descriptor.Descriptor(
  name='ServiceExtended',
  full_name='ServiceExtended',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ServiceExtended.hash', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='ServiceExtended.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='ServiceExtended.config', index=2,
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
    _descriptor.OneofDescriptor(
      name='oneOf', full_name='ServiceExtended.oneOf',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_config', full_name='ServiceExtended._config',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=196,
  serialized_end=337,
)

_TOKEN.oneofs_by_name['oneOf'].fields.append(
  _TOKEN.fields_by_name['value_int32'])
_TOKEN.fields_by_name['value_int32'].containing_oneof = _TOKEN.oneofs_by_name['oneOf']
_TOKEN.oneofs_by_name['oneOf'].fields.append(
  _TOKEN.fields_by_name['value_int64'])
_TOKEN.fields_by_name['value_int64'].containing_oneof = _TOKEN.oneofs_by_name['oneOf']
_TOKEN.oneofs_by_name['oneOf'].fields.append(
  _TOKEN.fields_by_name['value_string'])
_TOKEN.fields_by_name['value_string'].containing_oneof = _TOKEN.oneofs_by_name['oneOf']
_INSTANCE.fields_by_name['instance'].message_type = ipss__pb2._INSTANCE
_INSTANCE.fields_by_name['token'].message_type = _TOKEN
_SERVICEEXTENDED.fields_by_name['hash'].message_type = ipss__pb2._HASH
_SERVICEEXTENDED.fields_by_name['service'].message_type = ipss__pb2._SERVICE
_SERVICEEXTENDED.fields_by_name['config'].message_type = ipss__pb2._CONFIGURATION
_SERVICEEXTENDED.oneofs_by_name['oneOf'].fields.append(
  _SERVICEEXTENDED.fields_by_name['hash'])
_SERVICEEXTENDED.fields_by_name['hash'].containing_oneof = _SERVICEEXTENDED.oneofs_by_name['oneOf']
_SERVICEEXTENDED.oneofs_by_name['oneOf'].fields.append(
  _SERVICEEXTENDED.fields_by_name['service'])
_SERVICEEXTENDED.fields_by_name['service'].containing_oneof = _SERVICEEXTENDED.oneofs_by_name['oneOf']
_SERVICEEXTENDED.oneofs_by_name['_config'].fields.append(
  _SERVICEEXTENDED.fields_by_name['config'])
_SERVICEEXTENDED.fields_by_name['config'].containing_oneof = _SERVICEEXTENDED.oneofs_by_name['_config']
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['ServiceExtended'] = _SERVICEEXTENDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Token)
  })
_sym_db.RegisterMessage(Token)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Instance)
  })
_sym_db.RegisterMessage(Instance)

ServiceExtended = _reflection.GeneratedProtocolMessageType('ServiceExtended', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEEXTENDED,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ServiceExtended)
  })
_sym_db.RegisterMessage(ServiceExtended)



_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=339,
  serialized_end=430,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartService',
    full_name='Gateway.StartService',
    index=0,
    containing_service=None,
    input_type=_SERVICEEXTENDED,
    output_type=_INSTANCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopService',
    full_name='Gateway.StopService',
    index=1,
    containing_service=None,
    input_type=_TOKEN,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)
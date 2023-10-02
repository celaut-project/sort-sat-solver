# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import buffer_pb2 as buffer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x03\x61pi\x1a\x0c\x62uffer.proto\"L\n\x0eInterpretation\x12\x10\n\x08variable\x18\x01 \x03(\x05\x12\x18\n\x0bsatisfiable\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\x0e\n\x0c_satisfiable\"\x19\n\x06\x43lause\x12\x0f\n\x07literal\x18\x01 \x03(\x05\"\"\n\x03\x43nf\x12\x1b\n\x06\x63lause\x18\x01 \x03(\x0b\x32\x0b.api.Clause27\n\x06Solver\x12-\n\x05Solve\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[buffer__pb2.DESCRIPTOR,])




_INTERPRETATION = _descriptor.Descriptor(
  name='Interpretation',
  full_name='api.Interpretation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='api.Interpretation.variable', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='satisfiable', full_name='api.Interpretation.satisfiable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
      name='_satisfiable', full_name='api.Interpretation._satisfiable',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=32,
  serialized_end=108,
)


_CLAUSE = _descriptor.Descriptor(
  name='Clause',
  full_name='api.Clause',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='literal', full_name='api.Clause.literal', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=110,
  serialized_end=135,
)


_CNF = _descriptor.Descriptor(
  name='Cnf',
  full_name='api.Cnf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clause', full_name='api.Cnf.clause', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=137,
  serialized_end=171,
)

_INTERPRETATION.oneofs_by_name['_satisfiable'].fields.append(
  _INTERPRETATION.fields_by_name['satisfiable'])
_INTERPRETATION.fields_by_name['satisfiable'].containing_oneof = _INTERPRETATION.oneofs_by_name['_satisfiable']
_CNF.fields_by_name['clause'].message_type = _CLAUSE
DESCRIPTOR.message_types_by_name['Interpretation'] = _INTERPRETATION
DESCRIPTOR.message_types_by_name['Clause'] = _CLAUSE
DESCRIPTOR.message_types_by_name['Cnf'] = _CNF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Interpretation = _reflection.GeneratedProtocolMessageType('Interpretation', (_message.Message,), {
  'DESCRIPTOR' : _INTERPRETATION,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Interpretation)
  })
_sym_db.RegisterMessage(Interpretation)

Clause = _reflection.GeneratedProtocolMessageType('Clause', (_message.Message,), {
  'DESCRIPTOR' : _CLAUSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Clause)
  })
_sym_db.RegisterMessage(Clause)

Cnf = _reflection.GeneratedProtocolMessageType('Cnf', (_message.Message,), {
  'DESCRIPTOR' : _CNF,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Cnf)
  })
_sym_db.RegisterMessage(Cnf)



_SOLVER = _descriptor.ServiceDescriptor(
  name='Solver',
  full_name='api.Solver',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=173,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='Solve',
    full_name='api.Solver.Solve',
    index=0,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOLVER)

DESCRIPTOR.services_by_name['Solver'] = _SOLVER

# @@protoc_insertion_point(module_scope)

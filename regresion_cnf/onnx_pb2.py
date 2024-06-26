# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: onnx.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nonnx.proto\x12\x0btensor_onnx\"\xeb\x02\n\x04ONNX\x12*\n\x07\x65scalar\x18\x01 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12<\n\x0bnon_escalar\x18\x02 \x01(\x0b\x32%.tensor_onnx.ONNX.NonEscalarDimensionH\x00\x1a\xef\x01\n\x13NonEscalarDimension\x12\x45\n\x0bnon_escalar\x18\x01 \x03(\x0b\x32\x30.tensor_onnx.ONNX.NonEscalarDimension.NonEscalar\x1a\x90\x01\n\nNonEscalar\x12\x0f\n\x07\x65lement\x18\x01 \x02(\x0c\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12<\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32%.tensor_onnx.ONNX.NonEscalarDimensionH\x00\x42\x07\n\x05modelB\x07\n\x05model\"\x83\x04\n\x0e\x41ttributeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rref_attr_name\x18\x15 \x01(\t\x12\x12\n\ndoc_string\x18\r \x01(\t\x12\x37\n\x04type\x18\x14 \x01(\x0e\x32).tensor_onnx.AttributeProto.AttributeType\x12\t\n\x01\x66\x18\x02 \x01(\x02\x12\t\n\x01i\x18\x03 \x01(\x03\x12\t\n\x01s\x18\x04 \x01(\x0c\x12#\n\x01t\x18\x05 \x01(\x0b\x32\x18.tensor_onnx.TensorProto\x12\"\n\x01g\x18\x06 \x01(\x0b\x32\x17.tensor_onnx.GraphProto\x12\x0e\n\x06\x66loats\x18\x07 \x03(\x02\x12\x0c\n\x04ints\x18\x08 \x03(\x03\x12\x0f\n\x07strings\x18\t \x03(\x0c\x12)\n\x07tensors\x18\n \x03(\x0b\x32\x18.tensor_onnx.TensorProto\x12\'\n\x06graphs\x18\x0b \x03(\x0b\x32\x17.tensor_onnx.GraphProto\"\x91\x01\n\rAttributeType\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\x07\n\x03INT\x10\x02\x12\n\n\x06STRING\x10\x03\x12\n\n\x06TENSOR\x10\x04\x12\t\n\x05GRAPH\x10\x05\x12\n\n\x06\x46LOATS\x10\x06\x12\x08\n\x04INTS\x10\x07\x12\x0b\n\x07STRINGS\x10\x08\x12\x0b\n\x07TENSORS\x10\t\x12\n\n\x06GRAPHS\x10\n\"X\n\x0eValueInfoProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0b\x32\x16.tensor_onnx.TypeProto\x12\x12\n\ndoc_string\x18\x03 \x01(\t\"\x9d\x01\n\tNodeProto\x12\r\n\x05input\x18\x01 \x03(\t\x12\x0e\n\x06output\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07op_type\x18\x04 \x01(\t\x12\x0e\n\x06\x64omain\x18\x07 \x01(\t\x12.\n\tattribute\x18\x05 \x03(\x0b\x32\x1b.tensor_onnx.AttributeProto\x12\x12\n\ndoc_string\x18\x06 \x01(\t\"\xa8\x02\n\nModelProto\x12\x12\n\nir_version\x18\x01 \x01(\x03\x12\x35\n\x0copset_import\x18\x08 \x03(\x0b\x32\x1f.tensor_onnx.OperatorSetIdProto\x12\x15\n\rproducer_name\x18\x02 \x01(\t\x12\x18\n\x10producer_version\x18\x03 \x01(\t\x12\x0e\n\x06\x64omain\x18\x04 \x01(\t\x12\x15\n\rmodel_version\x18\x05 \x01(\x03\x12\x12\n\ndoc_string\x18\x06 \x01(\t\x12&\n\x05graph\x18\x07 \x01(\x0b\x32\x17.tensor_onnx.GraphProto\x12;\n\x0emetadata_props\x18\x0e \x03(\x0b\x32#.tensor_onnx.StringStringEntryProto\"4\n\x16StringStringEntryProto\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x8d\x02\n\nGraphProto\x12$\n\x04node\x18\x01 \x03(\x0b\x32\x16.tensor_onnx.NodeProto\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x0binitializer\x18\x05 \x03(\x0b\x32\x18.tensor_onnx.TensorProto\x12\x12\n\ndoc_string\x18\n \x01(\t\x12*\n\x05input\x18\x0b \x03(\x0b\x32\x1b.tensor_onnx.ValueInfoProto\x12+\n\x06output\x18\x0c \x03(\x0b\x32\x1b.tensor_onnx.ValueInfoProto\x12/\n\nvalue_info\x18\r \x03(\x0b\x32\x1b.tensor_onnx.ValueInfoProto\"\xbd\x04\n\x0bTensorProto\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\x12\x34\n\tdata_type\x18\x02 \x01(\x0e\x32!.tensor_onnx.TensorProto.DataType\x12\x31\n\x07segment\x18\x03 \x01(\x0b\x32 .tensor_onnx.TensorProto.Segment\x12\x16\n\nfloat_data\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\x16\n\nint32_data\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x13\n\x0bstring_data\x18\x06 \x03(\x0c\x12\x16\n\nint64_data\x18\x07 \x03(\x03\x42\x02\x10\x01\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x12\n\ndoc_string\x18\x0c \x01(\t\x12\x10\n\x08raw_data\x18\t \x01(\x0c\x12\x17\n\x0b\x64ouble_data\x18\n \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0buint64_data\x18\x0b \x03(\x04\x42\x02\x10\x01\x1a%\n\x07Segment\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"\xcc\x01\n\x08\x44\x61taType\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\t\n\x05UINT8\x10\x02\x12\x08\n\x04INT8\x10\x03\x12\n\n\x06UINT16\x10\x04\x12\t\n\x05INT16\x10\x05\x12\t\n\x05INT32\x10\x06\x12\t\n\x05INT64\x10\x07\x12\n\n\x06STRING\x10\x08\x12\x08\n\x04\x42OOL\x10\t\x12\x0b\n\x07\x46LOAT16\x10\n\x12\n\n\x06\x44OUBLE\x10\x0b\x12\n\n\x06UINT32\x10\x0c\x12\n\n\x06UINT64\x10\r\x12\r\n\tCOMPLEX64\x10\x0e\x12\x0e\n\nCOMPLEX128\x10\x0f\"\x9c\x01\n\x10TensorShapeProto\x12\x34\n\x03\x64im\x18\x01 \x03(\x0b\x32\'.tensor_onnx.TensorShapeProto.Dimension\x1aR\n\tDimension\x12\x13\n\tdim_value\x18\x01 \x01(\x03H\x00\x12\x13\n\tdim_param\x18\x02 \x01(\tH\x00\x12\x12\n\ndenotation\x18\x03 \x01(\tB\x07\n\x05value\"\xcc\x01\n\tTypeProto\x12\x34\n\x0btensor_type\x18\x01 \x01(\x0b\x32\x1d.tensor_onnx.TypeProto.TensorH\x00\x12\x12\n\ndenotation\x18\x06 \x01(\t\x1al\n\x06Tensor\x12\x34\n\telem_type\x18\x01 \x01(\x0e\x32!.tensor_onnx.TensorProto.DataType\x12,\n\x05shape\x18\x02 \x01(\x0b\x32\x1d.tensor_onnx.TensorShapeProtoB\x07\n\x05value\"5\n\x12OperatorSetIdProto\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03*c\n\x07Version\x12\x12\n\x0e_START_VERSION\x10\x00\x12\x19\n\x15IR_VERSION_2017_10_10\x10\x01\x12\x19\n\x15IR_VERSION_2017_10_30\x10\x02\x12\x0e\n\nIR_VERSION\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'onnx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TENSORPROTO'].fields_by_name['float_data']._options = None
  _globals['_TENSORPROTO'].fields_by_name['float_data']._serialized_options = b'\020\001'
  _globals['_TENSORPROTO'].fields_by_name['int32_data']._options = None
  _globals['_TENSORPROTO'].fields_by_name['int32_data']._serialized_options = b'\020\001'
  _globals['_TENSORPROTO'].fields_by_name['int64_data']._options = None
  _globals['_TENSORPROTO'].fields_by_name['int64_data']._serialized_options = b'\020\001'
  _globals['_TENSORPROTO'].fields_by_name['double_data']._options = None
  _globals['_TENSORPROTO'].fields_by_name['double_data']._serialized_options = b'\020\001'
  _globals['_TENSORPROTO'].fields_by_name['uint64_data']._options = None
  _globals['_TENSORPROTO'].fields_by_name['uint64_data']._serialized_options = b'\020\001'
  _globals['_VERSION']._serialized_start=2783
  _globals['_VERSION']._serialized_end=2882
  _globals['_ONNX']._serialized_start=28
  _globals['_ONNX']._serialized_end=391
  _globals['_ONNX_NONESCALARDIMENSION']._serialized_start=143
  _globals['_ONNX_NONESCALARDIMENSION']._serialized_end=382
  _globals['_ONNX_NONESCALARDIMENSION_NONESCALAR']._serialized_start=238
  _globals['_ONNX_NONESCALARDIMENSION_NONESCALAR']._serialized_end=382
  _globals['_ATTRIBUTEPROTO']._serialized_start=394
  _globals['_ATTRIBUTEPROTO']._serialized_end=909
  _globals['_ATTRIBUTEPROTO_ATTRIBUTETYPE']._serialized_start=764
  _globals['_ATTRIBUTEPROTO_ATTRIBUTETYPE']._serialized_end=909
  _globals['_VALUEINFOPROTO']._serialized_start=911
  _globals['_VALUEINFOPROTO']._serialized_end=999
  _globals['_NODEPROTO']._serialized_start=1002
  _globals['_NODEPROTO']._serialized_end=1159
  _globals['_MODELPROTO']._serialized_start=1162
  _globals['_MODELPROTO']._serialized_end=1458
  _globals['_STRINGSTRINGENTRYPROTO']._serialized_start=1460
  _globals['_STRINGSTRINGENTRYPROTO']._serialized_end=1512
  _globals['_GRAPHPROTO']._serialized_start=1515
  _globals['_GRAPHPROTO']._serialized_end=1784
  _globals['_TENSORPROTO']._serialized_start=1787
  _globals['_TENSORPROTO']._serialized_end=2360
  _globals['_TENSORPROTO_SEGMENT']._serialized_start=2116
  _globals['_TENSORPROTO_SEGMENT']._serialized_end=2153
  _globals['_TENSORPROTO_DATATYPE']._serialized_start=2156
  _globals['_TENSORPROTO_DATATYPE']._serialized_end=2360
  _globals['_TENSORSHAPEPROTO']._serialized_start=2363
  _globals['_TENSORSHAPEPROTO']._serialized_end=2519
  _globals['_TENSORSHAPEPROTO_DIMENSION']._serialized_start=2437
  _globals['_TENSORSHAPEPROTO_DIMENSION']._serialized_end=2519
  _globals['_TYPEPROTO']._serialized_start=2522
  _globals['_TYPEPROTO']._serialized_end=2726
  _globals['_TYPEPROTO_TENSOR']._serialized_start=2609
  _globals['_TYPEPROTO_TENSOR']._serialized_end=2717
  _globals['_OPERATORSETIDPROTO']._serialized_start=2728
  _globals['_OPERATORSETIDPROTO']._serialized_end=2781
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe2/proto/hsm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe2/proto/hsm.proto',
  package='caffe2',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x63\x61\x66\x66\x65\x32/proto/hsm.proto\x12\x06\x63\x61\x66\x66\x65\x32\"p\n\tNodeProto\x12#\n\x08\x63hildren\x18\x01 \x03(\x0b\x32\x11.caffe2.NodeProto\x12\x10\n\x08word_ids\x18\x02 \x03(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06scores\x18\x05 \x03(\x02\"1\n\tTreeProto\x12$\n\troot_node\x18\x01 \x01(\x0b\x32\x11.caffe2.NodeProto\"@\n\x0eHierarchyProto\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12 \n\x05paths\x18\x02 \x03(\x0b\x32\x11.caffe2.PathProto\"G\n\tPathProto\x12\x0f\n\x07word_id\x18\x01 \x01(\x05\x12)\n\npath_nodes\x18\x02 \x03(\x0b\x32\x15.caffe2.PathNodeProto\">\n\rPathNodeProto\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x0e\n\x06target\x18\x03 \x01(\x05'
)




_NODEPROTO = _descriptor.Descriptor(
  name='NodeProto',
  full_name='caffe2.NodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='caffe2.NodeProto.children', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='word_ids', full_name='caffe2.NodeProto.word_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='caffe2.NodeProto.offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe2.NodeProto.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='caffe2.NodeProto.scores', index=4,
      number=5, type=2, cpp_type=6, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=146,
)


_TREEPROTO = _descriptor.Descriptor(
  name='TreeProto',
  full_name='caffe2.TreeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_node', full_name='caffe2.TreeProto.root_node', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=197,
)


_HIERARCHYPROTO = _descriptor.Descriptor(
  name='HierarchyProto',
  full_name='caffe2.HierarchyProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='caffe2.HierarchyProto.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='caffe2.HierarchyProto.paths', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=263,
)


_PATHPROTO = _descriptor.Descriptor(
  name='PathProto',
  full_name='caffe2.PathProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word_id', full_name='caffe2.PathProto.word_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path_nodes', full_name='caffe2.PathProto.path_nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=336,
)


_PATHNODEPROTO = _descriptor.Descriptor(
  name='PathNodeProto',
  full_name='caffe2.PathNodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='caffe2.PathNodeProto.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='caffe2.PathNodeProto.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='caffe2.PathNodeProto.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=400,
)

_NODEPROTO.fields_by_name['children'].message_type = _NODEPROTO
_TREEPROTO.fields_by_name['root_node'].message_type = _NODEPROTO
_HIERARCHYPROTO.fields_by_name['paths'].message_type = _PATHPROTO
_PATHPROTO.fields_by_name['path_nodes'].message_type = _PATHNODEPROTO
DESCRIPTOR.message_types_by_name['NodeProto'] = _NODEPROTO
DESCRIPTOR.message_types_by_name['TreeProto'] = _TREEPROTO
DESCRIPTOR.message_types_by_name['HierarchyProto'] = _HIERARCHYPROTO
DESCRIPTOR.message_types_by_name['PathProto'] = _PATHPROTO
DESCRIPTOR.message_types_by_name['PathNodeProto'] = _PATHNODEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeProto = _reflection.GeneratedProtocolMessageType('NodeProto', (_message.Message,), {
  'DESCRIPTOR' : _NODEPROTO,
  '__module__' : 'caffe2.proto.hsm_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.NodeProto)
  })
_sym_db.RegisterMessage(NodeProto)

TreeProto = _reflection.GeneratedProtocolMessageType('TreeProto', (_message.Message,), {
  'DESCRIPTOR' : _TREEPROTO,
  '__module__' : 'caffe2.proto.hsm_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.TreeProto)
  })
_sym_db.RegisterMessage(TreeProto)

HierarchyProto = _reflection.GeneratedProtocolMessageType('HierarchyProto', (_message.Message,), {
  'DESCRIPTOR' : _HIERARCHYPROTO,
  '__module__' : 'caffe2.proto.hsm_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.HierarchyProto)
  })
_sym_db.RegisterMessage(HierarchyProto)

PathProto = _reflection.GeneratedProtocolMessageType('PathProto', (_message.Message,), {
  'DESCRIPTOR' : _PATHPROTO,
  '__module__' : 'caffe2.proto.hsm_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.PathProto)
  })
_sym_db.RegisterMessage(PathProto)

PathNodeProto = _reflection.GeneratedProtocolMessageType('PathNodeProto', (_message.Message,), {
  'DESCRIPTOR' : _PATHNODEPROTO,
  '__module__' : 'caffe2.proto.hsm_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.PathNodeProto)
  })
_sym_db.RegisterMessage(PathNodeProto)


# @@protoc_insertion_point(module_scope)

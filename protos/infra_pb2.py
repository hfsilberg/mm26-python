# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: infra.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='infra.proto',
  package='infra',
  syntax='proto3',
  serialized_options=b'\n2mech.mania.engine.server.communication.infra.modelB\013InfraProtos',
  serialized_pb=b'\n\x0binfra.proto\x12\x05infra\"5\n\x0bInfraPlayer\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\x12\x11\n\tplayer_ip\x18\x02 \x01(\t\".\n\x0bInfraStatus\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\tBA\n2mech.mania.engine.server.communication.infra.modelB\x0bInfraProtosb\x06proto3'
)




_INFRAPLAYER = _descriptor.Descriptor(
  name='InfraPlayer',
  full_name='infra.InfraPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_name', full_name='infra.InfraPlayer.player_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_ip', full_name='infra.InfraPlayer.player_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=75,
)


_INFRASTATUS = _descriptor.Descriptor(
  name='InfraStatus',
  full_name='infra.InfraStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='infra.InfraStatus.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='infra.InfraStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['InfraPlayer'] = _INFRAPLAYER
DESCRIPTOR.message_types_by_name['InfraStatus'] = _INFRASTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InfraPlayer = _reflection.GeneratedProtocolMessageType('InfraPlayer', (_message.Message,), {
  'DESCRIPTOR' : _INFRAPLAYER,
  '__module__' : 'infra_pb2'
  # @@protoc_insertion_point(class_scope:infra.InfraPlayer)
  })
_sym_db.RegisterMessage(InfraPlayer)

InfraStatus = _reflection.GeneratedProtocolMessageType('InfraStatus', (_message.Message,), {
  'DESCRIPTOR' : _INFRASTATUS,
  '__module__' : 'infra_pb2'
  # @@protoc_insertion_point(class_scope:infra.InfraStatus)
  })
_sym_db.RegisterMessage(InfraStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/status/scanner.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import options_pb2 as blickfeld_dot_options__pb2
from .. import error_pb2 as blickfeld_dot_error__pb2
from ..config import scan_pattern_pb2 as blickfeld_dot_config_dot_scan__pattern__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/status/scanner.proto',
  package='blickfeld.protocol.status',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x62lickfeld/status/scanner.proto\x12\x19\x62lickfeld.protocol.status\x1a\x17\x62lickfeld/options.proto\x1a\x15\x62lickfeld/error.proto\x1a#blickfeld/config/scan_pattern.proto\"\xbf\x02\n\x07Scanner\x12\x37\n\x05state\x18\x01 \x01(\x0e\x32(.blickfeld.protocol.status.Scanner.State\x12\x42\n\x0cscan_pattern\x18\x04 \x01(\x0b\x32&.blickfeld.protocol.config.ScanPatternB\x04\xb8\xb5\x18\x01\x12.\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x19.blickfeld.protocol.ErrorB\x04\xb0\xb5\x18\x01\"l\n\x05State\x12\x10\n\x0cINITIALIZING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08STARTING\x10\x03\x12\x0b\n\x07RUNNING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07\x45RRORED\x10\x06\x12\x10\n\x0cSELF_TESTING\x10\x07J\x04\x08\x02\x10\x03R\x13legacy_scan_pattern'
  ,
  dependencies=[blickfeld_dot_options__pb2.DESCRIPTOR,blickfeld_dot_error__pb2.DESCRIPTOR,blickfeld_dot_config_dot_scan__pattern__pb2.DESCRIPTOR,])



_SCANNER_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='blickfeld.protocol.status.Scanner.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERRORED', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELF_TESTING', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=331,
  serialized_end=439,
)
_sym_db.RegisterEnumDescriptor(_SCANNER_STATE)


_SCANNER = _descriptor.Descriptor(
  name='Scanner',
  full_name='blickfeld.protocol.status.Scanner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='blickfeld.protocol.status.Scanner.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scan_pattern', full_name='blickfeld.protocol.status.Scanner.scan_pattern', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\270\265\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='blickfeld.protocol.status.Scanner.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\260\265\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCANNER_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=466,
)

_SCANNER.fields_by_name['state'].enum_type = _SCANNER_STATE
_SCANNER.fields_by_name['scan_pattern'].message_type = blickfeld_dot_config_dot_scan__pattern__pb2._SCANPATTERN
_SCANNER.fields_by_name['error'].message_type = blickfeld_dot_error__pb2._ERROR
_SCANNER_STATE.containing_type = _SCANNER
DESCRIPTOR.message_types_by_name['Scanner'] = _SCANNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scanner = _reflection.GeneratedProtocolMessageType('Scanner', (_message.Message,), {
  'DESCRIPTOR' : _SCANNER,
  '__module__' : 'blickfeld.status.scanner_pb2'
  # @@protoc_insertion_point(class_scope:blickfeld.protocol.status.Scanner)
  })
_sym_db.RegisterMessage(Scanner)


_SCANNER.fields_by_name['scan_pattern']._options = None
_SCANNER.fields_by_name['error']._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/account_view.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/entity/account_view.proto\x12\x03\x61pi\x1a\rapi/ids.proto\"m\n\x0b\x41\x63\x63ountView\x12\x1a\n\x02id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x1e\n\x04type\x18\x04 \x01(\x0e\x32\x10.api.AccountType*z\n\x0b\x41\x63\x63ountType\x12\x18\n\x14\x41\x43\x43OUNT_TYPE_INVALID\x10\x00\x12\x17\n\x13\x41\x43\x43OUNT_TYPE_LEGACY\x10\x01\x12\x19\n\x15\x41\x43\x43OUNT_TYPE_PERSONAL\x10\x02\x12\x1d\n\x19\x41\x43\x43OUNT_TYPE_ORGANIZATION\x10\x03\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')

_ACCOUNTTYPE = DESCRIPTOR.enum_types_by_name['AccountType']
AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
ACCOUNT_TYPE_INVALID = 0
ACCOUNT_TYPE_LEGACY = 1
ACCOUNT_TYPE_PERSONAL = 2
ACCOUNT_TYPE_ORGANIZATION = 3


_ACCOUNTVIEW = DESCRIPTOR.message_types_by_name['AccountView']
AccountView = _reflection.GeneratedProtocolMessageType('AccountView', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTVIEW,
  '__module__' : 'api.entity.account_view_pb2'
  # @@protoc_insertion_point(class_scope:api.AccountView)
  })
_sym_db.RegisterMessage(AccountView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _ACCOUNTTYPE._serialized_start=164
  _ACCOUNTTYPE._serialized_end=286
  _ACCOUNTVIEW._serialized_start=53
  _ACCOUNTVIEW._serialized_end=162
# @@protoc_insertion_point(module_scope)

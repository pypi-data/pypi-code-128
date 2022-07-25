# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/run.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api import ids_pb2 as api_dot_ids__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/entity/run.proto\x12\x03\x61pi\x1a\rapi/ids.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb4\x04\n\x03Run\x12\x16\n\x02id\x18\x01 \x01(\x0b\x32\n.api.RunId\x12#\n\nrun_status\x18\x02 \x01(\x0e\x32\x0f.api.Run.Status\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x14\n\x0cproject_name\x18\x05 \x01(\t\x12\"\n\rcreated_by_id\x18\x06 \x01(\x0b\x32\x0b.api.UserId\x12+\n\x08\x64uration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x30\n\x0c\x63reated_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bstatus_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfinished_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cuser_command\x18\x0b \x01(\t\x12\"\n\nproject_id\x18\x0c \x01(\x0b\x32\x0e.api.ProjectId\x12\"\n\naccount_id\x18\r \x01(\x0b\x32\x0e.api.AccountId\"\x86\x01\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x14\n\x10STATUS_SCHEDULED\x10\x01\x12\x12\n\x0eSTATUS_RUNNING\x10\x02\x12\x14\n\x10STATUS_SUCCEEDED\x10\x03\x12\x11\n\rSTATUS_FAILED\x10\x04\x12\x15\n\x11STATUS_TERMINATED\x10\x05\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_RUN = DESCRIPTOR.message_types_by_name['Run']
_RUN_STATUS = _RUN.enum_types_by_name['Status']
Run = _reflection.GeneratedProtocolMessageType('Run', (_message.Message,), {
  'DESCRIPTOR' : _RUN,
  '__module__' : 'api.entity.run_pb2'
  # @@protoc_insertion_point(class_scope:api.Run)
  })
_sym_db.RegisterMessage(Run)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _RUN._serialized_start=110
  _RUN._serialized_end=674
  _RUN_STATUS._serialized_start=540
  _RUN_STATUS._serialized_end=674
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CanParserNode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Common_pb2 as Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x43\x61nParserNode.proto\x12\rCanParserNode\x1a\x0c\x43ommon.proto\"/\n\x0esubscribe_info\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1a\n\x07\x64\x62_path\x12\x0f\n\x07\x64\x62_path\x18\x01 \x01(\t\"<\n\ndb_configs\x12.\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x1d.CanParserNode.db_config_pair\"2\n\x0e\x64\x62_config_pair\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x62_name\x18\x02 \x01(\t\"C\n\x0fmqtt_topic_tree\x12\x1e\n\x06result\x18\x01 \x01(\x0b\x32\x0e.Common.result\x12\x10\n\x08str_json\x18\x02 \x01(\t\"L\n\x12i_signal_i_pdu_obj\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x10\n\x08pdu_name\x18\x02 \x01(\t\x12\x13\n\x0bpdu_context\x18\x03 \x01(\t\"U\n\x15i_signal_i_pdu_encode\x12\x1e\n\x06result\x18\x01 \x01(\x0b\x32\x0e.Common.result\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\r2\xae\x03\n\rCanParserNode\x12.\n\nGetVersion\x12\r.Common.empty\x1a\x0f.Common.version\"\x00\x12\x35\n\tAddDbFile\x12\x16.CanParserNode.db_path\x1a\x0e.Common.result\"\x00\x12\x38\n\tSetConfig\x12\x19.CanParserNode.db_configs\x1a\x0e.Common.result\"\x00\x12(\n\x05\x43lear\x12\r.Common.empty\x1a\x0e.Common.result\"\x00\x12\x31\n\x0e\x43learSubscribe\x12\r.Common.empty\x1a\x0e.Common.result\"\x00\x12G\n\x14GetMqttTopicTreeJson\x12\r.Common.empty\x1a\x1e.CanParserNode.mqtt_topic_tree\"\x00\x12V\n\tEncodePdu\x12!.CanParserNode.i_signal_i_pdu_obj\x1a$.CanParserNode.i_signal_i_pdu_encode\"\x00\x62\x06proto3')



_SUBSCRIBE_INFO = DESCRIPTOR.message_types_by_name['subscribe_info']
_DB_PATH = DESCRIPTOR.message_types_by_name['db_path']
_DB_CONFIGS = DESCRIPTOR.message_types_by_name['db_configs']
_DB_CONFIG_PAIR = DESCRIPTOR.message_types_by_name['db_config_pair']
_MQTT_TOPIC_TREE = DESCRIPTOR.message_types_by_name['mqtt_topic_tree']
_I_SIGNAL_I_PDU_OBJ = DESCRIPTOR.message_types_by_name['i_signal_i_pdu_obj']
_I_SIGNAL_I_PDU_ENCODE = DESCRIPTOR.message_types_by_name['i_signal_i_pdu_encode']
subscribe_info = _reflection.GeneratedProtocolMessageType('subscribe_info', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_INFO,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.subscribe_info)
  })
_sym_db.RegisterMessage(subscribe_info)

db_path = _reflection.GeneratedProtocolMessageType('db_path', (_message.Message,), {
  'DESCRIPTOR' : _DB_PATH,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.db_path)
  })
_sym_db.RegisterMessage(db_path)

db_configs = _reflection.GeneratedProtocolMessageType('db_configs', (_message.Message,), {
  'DESCRIPTOR' : _DB_CONFIGS,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.db_configs)
  })
_sym_db.RegisterMessage(db_configs)

db_config_pair = _reflection.GeneratedProtocolMessageType('db_config_pair', (_message.Message,), {
  'DESCRIPTOR' : _DB_CONFIG_PAIR,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.db_config_pair)
  })
_sym_db.RegisterMessage(db_config_pair)

mqtt_topic_tree = _reflection.GeneratedProtocolMessageType('mqtt_topic_tree', (_message.Message,), {
  'DESCRIPTOR' : _MQTT_TOPIC_TREE,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.mqtt_topic_tree)
  })
_sym_db.RegisterMessage(mqtt_topic_tree)

i_signal_i_pdu_obj = _reflection.GeneratedProtocolMessageType('i_signal_i_pdu_obj', (_message.Message,), {
  'DESCRIPTOR' : _I_SIGNAL_I_PDU_OBJ,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.i_signal_i_pdu_obj)
  })
_sym_db.RegisterMessage(i_signal_i_pdu_obj)

i_signal_i_pdu_encode = _reflection.GeneratedProtocolMessageType('i_signal_i_pdu_encode', (_message.Message,), {
  'DESCRIPTOR' : _I_SIGNAL_I_PDU_ENCODE,
  '__module__' : 'CanParserNode_pb2'
  # @@protoc_insertion_point(class_scope:CanParserNode.i_signal_i_pdu_encode)
  })
_sym_db.RegisterMessage(i_signal_i_pdu_encode)

_CANPARSERNODE = DESCRIPTOR.services_by_name['CanParserNode']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUBSCRIBE_INFO._serialized_start=52
  _SUBSCRIBE_INFO._serialized_end=99
  _DB_PATH._serialized_start=101
  _DB_PATH._serialized_end=127
  _DB_CONFIGS._serialized_start=129
  _DB_CONFIGS._serialized_end=189
  _DB_CONFIG_PAIR._serialized_start=191
  _DB_CONFIG_PAIR._serialized_end=241
  _MQTT_TOPIC_TREE._serialized_start=243
  _MQTT_TOPIC_TREE._serialized_end=310
  _I_SIGNAL_I_PDU_OBJ._serialized_start=312
  _I_SIGNAL_I_PDU_OBJ._serialized_end=388
  _I_SIGNAL_I_PDU_ENCODE._serialized_start=390
  _I_SIGNAL_I_PDU_ENCODE._serialized_end=475
  _CANPARSERNODE._serialized_start=478
  _CANPARSERNODE._serialized_end=908
# @@protoc_insertion_point(module_scope)

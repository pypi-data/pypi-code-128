# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/config/advanced.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import options_pb2 as blickfeld_dot_options__pb2
from ..stream import connection_pb2 as blickfeld_dot_stream_dot_connection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/config/advanced.proto',
  package='blickfeld.protocol.config',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x62lickfeld/config/advanced.proto\x12\x19\x62lickfeld.protocol.config\x1a\x17\x62lickfeld/options.proto\x1a!blickfeld/stream/connection.proto\"\xbf\x08\n\x08\x41\x64vanced\x12>\n\x08\x64\x65tector\x18\x01 \x01(\x0b\x32,.blickfeld.protocol.config.Advanced.Detector\x12\x42\n\nprocessing\x18\x02 \x01(\x0b\x32..blickfeld.protocol.config.Advanced.Processing\x12:\n\x06server\x18\x03 \x01(\x0b\x32*.blickfeld.protocol.config.Advanced.Server\x12U\n\x14time_synchronization\x18\x04 \x01(\x0b\x32\x37.blickfeld.protocol.config.Advanced.TimeSynchronization\x1a:\n\x08\x44\x65tector\x12.\n\x0bsensitivity\x18\x01 \x01(\x02:\x01\x31\x42\x16\x81\xb5\x18\x9a\x99\x99\x99\x99\x99\xe9?\x89\xb5\x18\x33\x33\x33\x33\x33\x33\xf3?\x1a\xa9\x01\n\nProcessing\x12/\n\x0crange_offset\x18\x01 \x01(\x02:\x01\x30\x42\x16\x81\xb5\x18\x00\x00\x00\x00\x00\x00\x00\xc0\x89\xb5\x18\x00\x00\x00\x00\x00\x00\x00@\x12.\n\x1aimu_static_rotation_offset\x18\x02 \x03(\x02\x42\n\x10\x01\xa0\xb5\x18\x12\xb0\xb5\x18\x01\x12:\n\x17horizontal_phase_offset\x18\x03 \x01(\x02:\x01\x30\x42\x16\x81\xb5\x18\x8d\xed\xb5\xa0\xf7\xc6\x00\xbf\x89\xb5\x18\x8d\xed\xb5\xa0\xf7\xc6\x00?\x1a\x63\n\x06Server\x12Y\n default_point_cloud_subscription\x18\x01 \x01(\x0b\x32/.blickfeld.protocol.stream.Subscribe.PointCloud\x1a\xce\x03\n\x13TimeSynchronization\x12J\n\x03ntp\x18\x01 \x01(\x0b\x32;.blickfeld.protocol.config.Advanced.TimeSynchronization.NTPH\x00\x12J\n\x03ptp\x18\x02 \x01(\x0b\x32;.blickfeld.protocol.config.Advanced.TimeSynchronization.PTPH\x00\x1a\x30\n\x03NTP\x12)\n\x07servers\x18\x01 \x03(\tB\x18\xb0\xb5\x18\x01\xaa\xb5\x18\x10[[:alnum:]\\.\\-]+\x1a\xde\x01\n\x03PTP\x12\x11\n\x06\x64omain\x18\x01 \x01(\r:\x01\x30\x12h\n\x0f\x64\x65lay_mechanism\x18\x02 \x01(\x0e\x32J.blickfeld.protocol.config.Advanced.TimeSynchronization.PTP.DelayMechanism:\x03\x45\x32\x45\x12\x36\n\x14unicast_destinations\x18\x03 \x03(\tB\x18\xb0\xb5\x18\x01\xaa\xb5\x18\x10[[:alnum:]\\.\\-]+\"\"\n\x0e\x44\x65layMechanism\x12\x07\n\x03\x45\x32\x45\x10\x01\x12\x07\n\x03P2P\x10\x02\x42\x0c\n\x04kind\x12\x04\xb0\xb5\x18\x01'
  ,
  dependencies=[blickfeld_dot_options__pb2.DESCRIPTOR,blickfeld_dot_stream_dot_connection__pb2.DESCRIPTOR,])



_ADVANCED_TIMESYNCHRONIZATION_PTP_DELAYMECHANISM = _descriptor.EnumDescriptor(
  name='DelayMechanism',
  full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.PTP.DelayMechanism',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='E2E', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='P2P', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1162,
  serialized_end=1196,
)
_sym_db.RegisterEnumDescriptor(_ADVANCED_TIMESYNCHRONIZATION_PTP_DELAYMECHANISM)


_ADVANCED_DETECTOR = _descriptor.Descriptor(
  name='Detector',
  full_name='blickfeld.protocol.config.Advanced.Detector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensitivity', full_name='blickfeld.protocol.config.Advanced.Detector.sensitivity', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\201\265\030\232\231\231\231\231\231\351?\211\265\030333333\363?', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=414,
  serialized_end=472,
)

_ADVANCED_PROCESSING = _descriptor.Descriptor(
  name='Processing',
  full_name='blickfeld.protocol.config.Advanced.Processing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='range_offset', full_name='blickfeld.protocol.config.Advanced.Processing.range_offset', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\201\265\030\000\000\000\000\000\000\000\300\211\265\030\000\000\000\000\000\000\000@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imu_static_rotation_offset', full_name='blickfeld.protocol.config.Advanced.Processing.imu_static_rotation_offset', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001\240\265\030\022\260\265\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_phase_offset', full_name='blickfeld.protocol.config.Advanced.Processing.horizontal_phase_offset', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\201\265\030\215\355\265\240\367\306\000\277\211\265\030\215\355\265\240\367\306\000?', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=475,
  serialized_end=644,
)

_ADVANCED_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='blickfeld.protocol.config.Advanced.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_point_cloud_subscription', full_name='blickfeld.protocol.config.Advanced.Server.default_point_cloud_subscription', index=0,
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
  serialized_start=646,
  serialized_end=745,
)

_ADVANCED_TIMESYNCHRONIZATION_NTP = _descriptor.Descriptor(
  name='NTP',
  full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.NTP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.NTP.servers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\260\265\030\001\252\265\030\020[[:alnum:]\\.\\-]+', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=923,
  serialized_end=971,
)

_ADVANCED_TIMESYNCHRONIZATION_PTP = _descriptor.Descriptor(
  name='PTP',
  full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.PTP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.PTP.domain', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_mechanism', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.PTP.delay_mechanism', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unicast_destinations', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.PTP.unicast_destinations', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\260\265\030\001\252\265\030\020[[:alnum:]\\.\\-]+', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADVANCED_TIMESYNCHRONIZATION_PTP_DELAYMECHANISM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=974,
  serialized_end=1196,
)

_ADVANCED_TIMESYNCHRONIZATION = _descriptor.Descriptor(
  name='TimeSynchronization',
  full_name='blickfeld.protocol.config.Advanced.TimeSynchronization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ntp', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.ntp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ptp', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.ptp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ADVANCED_TIMESYNCHRONIZATION_NTP, _ADVANCED_TIMESYNCHRONIZATION_PTP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='blickfeld.protocol.config.Advanced.TimeSynchronization.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\260\265\030\001'),
  ],
  serialized_start=748,
  serialized_end=1210,
)

_ADVANCED = _descriptor.Descriptor(
  name='Advanced',
  full_name='blickfeld.protocol.config.Advanced',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detector', full_name='blickfeld.protocol.config.Advanced.detector', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processing', full_name='blickfeld.protocol.config.Advanced.processing', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server', full_name='blickfeld.protocol.config.Advanced.server', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_synchronization', full_name='blickfeld.protocol.config.Advanced.time_synchronization', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ADVANCED_DETECTOR, _ADVANCED_PROCESSING, _ADVANCED_SERVER, _ADVANCED_TIMESYNCHRONIZATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=1210,
)

_ADVANCED_DETECTOR.containing_type = _ADVANCED
_ADVANCED_PROCESSING.containing_type = _ADVANCED
_ADVANCED_SERVER.fields_by_name['default_point_cloud_subscription'].message_type = blickfeld_dot_stream_dot_connection__pb2._SUBSCRIBE_POINTCLOUD
_ADVANCED_SERVER.containing_type = _ADVANCED
_ADVANCED_TIMESYNCHRONIZATION_NTP.containing_type = _ADVANCED_TIMESYNCHRONIZATION
_ADVANCED_TIMESYNCHRONIZATION_PTP.fields_by_name['delay_mechanism'].enum_type = _ADVANCED_TIMESYNCHRONIZATION_PTP_DELAYMECHANISM
_ADVANCED_TIMESYNCHRONIZATION_PTP.containing_type = _ADVANCED_TIMESYNCHRONIZATION
_ADVANCED_TIMESYNCHRONIZATION_PTP_DELAYMECHANISM.containing_type = _ADVANCED_TIMESYNCHRONIZATION_PTP
_ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ntp'].message_type = _ADVANCED_TIMESYNCHRONIZATION_NTP
_ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ptp'].message_type = _ADVANCED_TIMESYNCHRONIZATION_PTP
_ADVANCED_TIMESYNCHRONIZATION.containing_type = _ADVANCED
_ADVANCED_TIMESYNCHRONIZATION.oneofs_by_name['kind'].fields.append(
  _ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ntp'])
_ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ntp'].containing_oneof = _ADVANCED_TIMESYNCHRONIZATION.oneofs_by_name['kind']
_ADVANCED_TIMESYNCHRONIZATION.oneofs_by_name['kind'].fields.append(
  _ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ptp'])
_ADVANCED_TIMESYNCHRONIZATION.fields_by_name['ptp'].containing_oneof = _ADVANCED_TIMESYNCHRONIZATION.oneofs_by_name['kind']
_ADVANCED.fields_by_name['detector'].message_type = _ADVANCED_DETECTOR
_ADVANCED.fields_by_name['processing'].message_type = _ADVANCED_PROCESSING
_ADVANCED.fields_by_name['server'].message_type = _ADVANCED_SERVER
_ADVANCED.fields_by_name['time_synchronization'].message_type = _ADVANCED_TIMESYNCHRONIZATION
DESCRIPTOR.message_types_by_name['Advanced'] = _ADVANCED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Advanced = _reflection.GeneratedProtocolMessageType('Advanced', (_message.Message,), {

  'Detector' : _reflection.GeneratedProtocolMessageType('Detector', (_message.Message,), {
    'DESCRIPTOR' : _ADVANCED_DETECTOR,
    '__module__' : 'blickfeld.config.advanced_pb2'
    # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.Detector)
    })
  ,

  'Processing' : _reflection.GeneratedProtocolMessageType('Processing', (_message.Message,), {
    'DESCRIPTOR' : _ADVANCED_PROCESSING,
    '__module__' : 'blickfeld.config.advanced_pb2'
    # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.Processing)
    })
  ,

  'Server' : _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), {
    'DESCRIPTOR' : _ADVANCED_SERVER,
    '__module__' : 'blickfeld.config.advanced_pb2'
    # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.Server)
    })
  ,

  'TimeSynchronization' : _reflection.GeneratedProtocolMessageType('TimeSynchronization', (_message.Message,), {

    'NTP' : _reflection.GeneratedProtocolMessageType('NTP', (_message.Message,), {
      'DESCRIPTOR' : _ADVANCED_TIMESYNCHRONIZATION_NTP,
      '__module__' : 'blickfeld.config.advanced_pb2'
      # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.TimeSynchronization.NTP)
      })
    ,

    'PTP' : _reflection.GeneratedProtocolMessageType('PTP', (_message.Message,), {
      'DESCRIPTOR' : _ADVANCED_TIMESYNCHRONIZATION_PTP,
      '__module__' : 'blickfeld.config.advanced_pb2'
      # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.TimeSynchronization.PTP)
      })
    ,
    'DESCRIPTOR' : _ADVANCED_TIMESYNCHRONIZATION,
    '__module__' : 'blickfeld.config.advanced_pb2'
    # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced.TimeSynchronization)
    })
  ,
  'DESCRIPTOR' : _ADVANCED,
  '__module__' : 'blickfeld.config.advanced_pb2'
  # @@protoc_insertion_point(class_scope:blickfeld.protocol.config.Advanced)
  })
_sym_db.RegisterMessage(Advanced)
_sym_db.RegisterMessage(Advanced.Detector)
_sym_db.RegisterMessage(Advanced.Processing)
_sym_db.RegisterMessage(Advanced.Server)
_sym_db.RegisterMessage(Advanced.TimeSynchronization)
_sym_db.RegisterMessage(Advanced.TimeSynchronization.NTP)
_sym_db.RegisterMessage(Advanced.TimeSynchronization.PTP)


_ADVANCED_DETECTOR.fields_by_name['sensitivity']._options = None
_ADVANCED_PROCESSING.fields_by_name['range_offset']._options = None
_ADVANCED_PROCESSING.fields_by_name['imu_static_rotation_offset']._options = None
_ADVANCED_PROCESSING.fields_by_name['horizontal_phase_offset']._options = None
_ADVANCED_TIMESYNCHRONIZATION_NTP.fields_by_name['servers']._options = None
_ADVANCED_TIMESYNCHRONIZATION_PTP.fields_by_name['unicast_destinations']._options = None
_ADVANCED_TIMESYNCHRONIZATION.oneofs_by_name['kind']._options = None
# @@protoc_insertion_point(module_scope)

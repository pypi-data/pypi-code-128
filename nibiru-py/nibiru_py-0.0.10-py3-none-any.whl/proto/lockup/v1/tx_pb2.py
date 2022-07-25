# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lockup/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from lockup.v1 import lock_pb2 as lockup_dot_v1_dot_lock__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12lockup/v1/tx.proto\x12\x10nibiru.lockup.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14lockup/v1/lock.proto\x1a\x1cgoogle/api/annotations.proto\"\xec\x01\n\rMsgLockTokens\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"owner\"\x12^\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x12\x64uration,omitempty\xf2\xde\x1f\x0fyaml:\"duration\"\x12Z\n\x05\x63oins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"(\n\x15MsgLockTokensResponse\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\"3\n\x11MsgInitiateUnlock\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\"\x1b\n\x19MsgInitiateUnlockResponse\"+\n\tMsgUnlock\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\"\x13\n\x11MsgUnlockResponse\"\xe7\x01\n\tEventLock\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\x12\r\n\x05owner\x18\x02 \x01(\t\x12^\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x12\x64uration,omitempty\xf2\xde\x1f\x0fyaml:\"duration\"\x12Z\n\x05\x63oins\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xe1\x01\n\x14\x45ventUnlockInitiated\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\x12\r\n\x05owner\x18\x02 \x01(\t\x12Z\n\x05\x63oins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12M\n\x0cunlocking_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1b\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"end_time\"\"\x89\x01\n\x0b\x45ventUnlock\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\x12\r\n\x05owner\x18\x02 \x01(\t\x12Z\n\x05\x63oins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins2\xf5\x02\n\x03Msg\x12z\n\nLockTokens\x12\x1f.nibiru.lockup.v1.MsgLockTokens\x1a\'.nibiru.lockup.v1.MsgLockTokensResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/lockup/lock_tokens\x12\x86\x01\n\x0eInitiateUnlock\x12#.nibiru.lockup.v1.MsgInitiateUnlock\x1a+.nibiru.lockup.v1.MsgInitiateUnlockResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/lockup/init_unlock\x12i\n\x06Unlock\x12\x1b.nibiru.lockup.v1.MsgUnlock\x1a#.nibiru.lockup.v1.MsgUnlockResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/nibiru/lockup/unlockB.Z,github.com/NibiruChain/nibiru/x/lockup/typesb\x06proto3'
)


_MSGLOCKTOKENS = DESCRIPTOR.message_types_by_name['MsgLockTokens']
_MSGLOCKTOKENSRESPONSE = DESCRIPTOR.message_types_by_name['MsgLockTokensResponse']
_MSGINITIATEUNLOCK = DESCRIPTOR.message_types_by_name['MsgInitiateUnlock']
_MSGINITIATEUNLOCKRESPONSE = DESCRIPTOR.message_types_by_name['MsgInitiateUnlockResponse']
_MSGUNLOCK = DESCRIPTOR.message_types_by_name['MsgUnlock']
_MSGUNLOCKRESPONSE = DESCRIPTOR.message_types_by_name['MsgUnlockResponse']
_EVENTLOCK = DESCRIPTOR.message_types_by_name['EventLock']
_EVENTUNLOCKINITIATED = DESCRIPTOR.message_types_by_name['EventUnlockInitiated']
_EVENTUNLOCK = DESCRIPTOR.message_types_by_name['EventUnlock']
MsgLockTokens = _reflection.GeneratedProtocolMessageType(
    'MsgLockTokens',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGLOCKTOKENS,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgLockTokens)
    },
)
_sym_db.RegisterMessage(MsgLockTokens)

MsgLockTokensResponse = _reflection.GeneratedProtocolMessageType(
    'MsgLockTokensResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGLOCKTOKENSRESPONSE,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgLockTokensResponse)
    },
)
_sym_db.RegisterMessage(MsgLockTokensResponse)

MsgInitiateUnlock = _reflection.GeneratedProtocolMessageType(
    'MsgInitiateUnlock',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGINITIATEUNLOCK,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgInitiateUnlock)
    },
)
_sym_db.RegisterMessage(MsgInitiateUnlock)

MsgInitiateUnlockResponse = _reflection.GeneratedProtocolMessageType(
    'MsgInitiateUnlockResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGINITIATEUNLOCKRESPONSE,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgInitiateUnlockResponse)
    },
)
_sym_db.RegisterMessage(MsgInitiateUnlockResponse)

MsgUnlock = _reflection.GeneratedProtocolMessageType(
    'MsgUnlock',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGUNLOCK,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgUnlock)
    },
)
_sym_db.RegisterMessage(MsgUnlock)

MsgUnlockResponse = _reflection.GeneratedProtocolMessageType(
    'MsgUnlockResponse',
    (_message.Message,),
    {
        'DESCRIPTOR': _MSGUNLOCKRESPONSE,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.MsgUnlockResponse)
    },
)
_sym_db.RegisterMessage(MsgUnlockResponse)

EventLock = _reflection.GeneratedProtocolMessageType(
    'EventLock',
    (_message.Message,),
    {
        'DESCRIPTOR': _EVENTLOCK,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.EventLock)
    },
)
_sym_db.RegisterMessage(EventLock)

EventUnlockInitiated = _reflection.GeneratedProtocolMessageType(
    'EventUnlockInitiated',
    (_message.Message,),
    {
        'DESCRIPTOR': _EVENTUNLOCKINITIATED,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.EventUnlockInitiated)
    },
)
_sym_db.RegisterMessage(EventUnlockInitiated)

EventUnlock = _reflection.GeneratedProtocolMessageType(
    'EventUnlock',
    (_message.Message,),
    {
        'DESCRIPTOR': _EVENTUNLOCK,
        '__module__': 'lockup.v1.tx_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.lockup.v1.EventUnlock)
    },
)
_sym_db.RegisterMessage(EventUnlock)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/lockup/types'
    _MSGLOCKTOKENS.fields_by_name['owner']._options = None
    _MSGLOCKTOKENS.fields_by_name['owner']._serialized_options = b'\362\336\037\014yaml:\"owner\"'
    _MSGLOCKTOKENS.fields_by_name['duration']._options = None
    _MSGLOCKTOKENS.fields_by_name[
        'duration'
    ]._serialized_options = (
        b'\310\336\037\000\230\337\037\001\352\336\037\022duration,omitempty\362\336\037\017yaml:\"duration\"'
    )
    _MSGLOCKTOKENS.fields_by_name['coins']._options = None
    _MSGLOCKTOKENS.fields_by_name[
        'coins'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _EVENTLOCK.fields_by_name['duration']._options = None
    _EVENTLOCK.fields_by_name[
        'duration'
    ]._serialized_options = (
        b'\310\336\037\000\230\337\037\001\352\336\037\022duration,omitempty\362\336\037\017yaml:\"duration\"'
    )
    _EVENTLOCK.fields_by_name['coins']._options = None
    _EVENTLOCK.fields_by_name[
        'coins'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _EVENTUNLOCKINITIATED.fields_by_name['coins']._options = None
    _EVENTUNLOCKINITIATED.fields_by_name[
        'coins'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _EVENTUNLOCKINITIATED.fields_by_name['unlocking_at']._options = None
    _EVENTUNLOCKINITIATED.fields_by_name[
        'unlocking_at'
    ]._serialized_options = b'\220\337\037\001\310\336\037\000\362\336\037\017yaml:\"end_time\"'
    _EVENTUNLOCK.fields_by_name['coins']._options = None
    _EVENTUNLOCK.fields_by_name[
        'coins'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSG.methods_by_name['LockTokens']._options = None
    _MSG.methods_by_name['LockTokens']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/lockup/lock_tokens'
    _MSG.methods_by_name['InitiateUnlock']._options = None
    _MSG.methods_by_name[
        'InitiateUnlock'
    ]._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/lockup/init_unlock'
    _MSG.methods_by_name['Unlock']._options = None
    _MSG.methods_by_name['Unlock']._serialized_options = b'\202\323\344\223\002\027\"\025/nibiru/lockup/unlock'
    _MSGLOCKTOKENS._serialized_start = 212
    _MSGLOCKTOKENS._serialized_end = 448
    _MSGLOCKTOKENSRESPONSE._serialized_start = 450
    _MSGLOCKTOKENSRESPONSE._serialized_end = 490
    _MSGINITIATEUNLOCK._serialized_start = 492
    _MSGINITIATEUNLOCK._serialized_end = 543
    _MSGINITIATEUNLOCKRESPONSE._serialized_start = 545
    _MSGINITIATEUNLOCKRESPONSE._serialized_end = 572
    _MSGUNLOCK._serialized_start = 574
    _MSGUNLOCK._serialized_end = 617
    _MSGUNLOCKRESPONSE._serialized_start = 619
    _MSGUNLOCKRESPONSE._serialized_end = 638
    _EVENTLOCK._serialized_start = 641
    _EVENTLOCK._serialized_end = 872
    _EVENTUNLOCKINITIATED._serialized_start = 875
    _EVENTUNLOCKINITIATED._serialized_end = 1100
    _EVENTUNLOCK._serialized_start = 1103
    _EVENTUNLOCK._serialized_end = 1240
    _MSG._serialized_start = 1243
    _MSG._serialized_end = 1616
# @@protoc_insertion_point(module_scope)

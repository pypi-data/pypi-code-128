# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perp/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from perp.v1 import state_pb2 as perp_dot_v1_dot_state__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13perp/v1/event.proto\x12\x0enibiru.perp.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x13perp/v1/state.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x13\x63ommon/common.proto\"\x83\x07\n\x14PositionChangedEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x16\n\x0etrader_address\x18\x02 \x01(\t\x12@\n\x06margin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:\"margin\"\xc8\xde\x1f\x00\x12I\n\x11position_notional\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x65xchanged_position_size\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12R\n\x0ftransaction_fee\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1e\xf2\xde\x1f\x16yaml:\"transaction_fee\"\xc8\xde\x1f\x00\x12\x45\n\rposition_size\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0crealized_pnl\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12L\n\x14unrealized_pnl_after\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x31\n\x08\x62\x61\x64_debt\x18\n \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12K\n\x13liquidation_penalty\x18\x0b \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nspot_price\x18\x0c \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0f\x66unding_payment\x18\r \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x62lock_height\x18\x0e \x01(\x03\x12\x15\n\rblock_time_ms\x18\x0f \x01(\x03\"\xf3\x06\n\x17PositionLiquidatedEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x16\n\x0etrader_address\x18\x02 \x01(\t\x12N\n\x16\x65xchanged_quote_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x65xchanged_position_size\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x1a\n\x12liquidator_address\x18\x05 \x01(\t\x12V\n\x11\x66\x65\x65_to_liquidator\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB \xf2\xde\x1f\x18yaml:\"fee_to_liquidator\"\xc8\xde\x1f\x00\x12^\n\x15\x66\x65\x65_to_ecosystem_fund\x18\x07 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB$\xf2\xde\x1f\x1cyaml:\"fee_to_ecosystem_fund\"\xc8\xde\x1f\x00\x12\x31\n\x08\x62\x61\x64_debt\x18\x08 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12@\n\x06margin\x18\t \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:\"margin\"\xc8\xde\x1f\x00\x12I\n\x11position_notional\x18\n \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rposition_size\x18\x0b \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\runrealizedPnl\x18\x0c \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nmark_price\x18\r \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x62lock_height\x18\x0e \x01(\x03\x12\x15\n\rblock_time_ms\x18\x0f \x01(\x03\"\xb8\x01\n\x14PositionSettledEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x16\n\x0etrader_address\x18\x02 \x01(\t\x12z\n\rsettled_coins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBH\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x14yaml:\"settled_coins\"\xc8\xde\x1f\x00\"\xfb\x02\n\x17\x46undingRateChangedEvent\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\x42\n\nmark_price\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x43\n\x0bindex_price\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12K\n\x13latest_funding_rate\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x63umulative_funding_rate\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x62lock_height\x18\x06 \x01(\x03\x12\x15\n\rblock_time_ms\x18\x07 \x01(\x03\x42,Z*github.com/NibiruChain/nibiru/x/perp/typesb\x06proto3'
)


_POSITIONCHANGEDEVENT = DESCRIPTOR.message_types_by_name['PositionChangedEvent']
_POSITIONLIQUIDATEDEVENT = DESCRIPTOR.message_types_by_name['PositionLiquidatedEvent']
_POSITIONSETTLEDEVENT = DESCRIPTOR.message_types_by_name['PositionSettledEvent']
_FUNDINGRATECHANGEDEVENT = DESCRIPTOR.message_types_by_name['FundingRateChangedEvent']
PositionChangedEvent = _reflection.GeneratedProtocolMessageType(
    'PositionChangedEvent',
    (_message.Message,),
    {
        'DESCRIPTOR': _POSITIONCHANGEDEVENT,
        '__module__': 'perp.v1.event_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.perp.v1.PositionChangedEvent)
    },
)
_sym_db.RegisterMessage(PositionChangedEvent)

PositionLiquidatedEvent = _reflection.GeneratedProtocolMessageType(
    'PositionLiquidatedEvent',
    (_message.Message,),
    {
        'DESCRIPTOR': _POSITIONLIQUIDATEDEVENT,
        '__module__': 'perp.v1.event_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.perp.v1.PositionLiquidatedEvent)
    },
)
_sym_db.RegisterMessage(PositionLiquidatedEvent)

PositionSettledEvent = _reflection.GeneratedProtocolMessageType(
    'PositionSettledEvent',
    (_message.Message,),
    {
        'DESCRIPTOR': _POSITIONSETTLEDEVENT,
        '__module__': 'perp.v1.event_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.perp.v1.PositionSettledEvent)
    },
)
_sym_db.RegisterMessage(PositionSettledEvent)

FundingRateChangedEvent = _reflection.GeneratedProtocolMessageType(
    'FundingRateChangedEvent',
    (_message.Message,),
    {
        'DESCRIPTOR': _FUNDINGRATECHANGEDEVENT,
        '__module__': 'perp.v1.event_pb2'
        # @@protoc_insertion_point(class_scope:nibiru.perp.v1.FundingRateChangedEvent)
    },
)
_sym_db.RegisterMessage(FundingRateChangedEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/perp/types'
    _POSITIONCHANGEDEVENT.fields_by_name['margin']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'margin'
    ]._serialized_options = b'\362\336\037\ryaml:\"margin\"\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['position_notional']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'position_notional'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['exchanged_position_size']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'exchanged_position_size'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['transaction_fee']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'transaction_fee'
    ]._serialized_options = b'\362\336\037\026yaml:\"transaction_fee\"\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['position_size']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'position_size'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['realized_pnl']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'realized_pnl'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['unrealized_pnl_after']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'unrealized_pnl_after'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['bad_debt']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name['bad_debt']._serialized_options = b'\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['liquidation_penalty']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'liquidation_penalty'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['spot_price']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'spot_price'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT.fields_by_name['funding_payment']._options = None
    _POSITIONCHANGEDEVENT.fields_by_name[
        'funding_payment'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['exchanged_quote_amount']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'exchanged_quote_amount'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['exchanged_position_size']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'exchanged_position_size'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['fee_to_liquidator']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'fee_to_liquidator'
    ]._serialized_options = b'\362\336\037\030yaml:\"fee_to_liquidator\"\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['fee_to_ecosystem_fund']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'fee_to_ecosystem_fund'
    ]._serialized_options = b'\362\336\037\034yaml:\"fee_to_ecosystem_fund\"\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['bad_debt']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name['bad_debt']._serialized_options = b'\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['margin']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'margin'
    ]._serialized_options = b'\362\336\037\ryaml:\"margin\"\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['position_notional']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'position_notional'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['position_size']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'position_size'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['unrealizedPnl']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'unrealizedPnl'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONLIQUIDATEDEVENT.fields_by_name['mark_price']._options = None
    _POSITIONLIQUIDATEDEVENT.fields_by_name[
        'mark_price'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONSETTLEDEVENT.fields_by_name['settled_coins']._options = None
    _POSITIONSETTLEDEVENT.fields_by_name[
        'settled_coins'
    ]._serialized_options = (
        b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\024yaml:\"settled_coins\"\310\336\037\000'
    )
    _FUNDINGRATECHANGEDEVENT.fields_by_name['mark_price']._options = None
    _FUNDINGRATECHANGEDEVENT.fields_by_name[
        'mark_price'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _FUNDINGRATECHANGEDEVENT.fields_by_name['index_price']._options = None
    _FUNDINGRATECHANGEDEVENT.fields_by_name[
        'index_price'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _FUNDINGRATECHANGEDEVENT.fields_by_name['latest_funding_rate']._options = None
    _FUNDINGRATECHANGEDEVENT.fields_by_name[
        'latest_funding_rate'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _FUNDINGRATECHANGEDEVENT.fields_by_name['cumulative_funding_rate']._options = None
    _FUNDINGRATECHANGEDEVENT.fields_by_name[
        'cumulative_funding_rate'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _POSITIONCHANGEDEVENT._serialized_start = 166
    _POSITIONCHANGEDEVENT._serialized_end = 1065
    _POSITIONLIQUIDATEDEVENT._serialized_start = 1068
    _POSITIONLIQUIDATEDEVENT._serialized_end = 1951
    _POSITIONSETTLEDEVENT._serialized_start = 1954
    _POSITIONSETTLEDEVENT._serialized_end = 2138
    _FUNDINGRATECHANGEDEVENT._serialized_start = 2141
    _FUNDINGRATECHANGEDEVENT._serialized_end = 2520
# @@protoc_insertion_point(module_scope)

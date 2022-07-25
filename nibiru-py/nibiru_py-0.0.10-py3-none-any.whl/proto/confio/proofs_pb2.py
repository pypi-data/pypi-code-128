# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: confio/proofs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63onfio/proofs.proto\x12\x05ics23\"g\n\x0e\x45xistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b\x32\r.ics23.LeafOp\x12\x1c\n\x04path\x18\x04 \x03(\x0b\x32\x0e.ics23.InnerOp\"k\n\x11NonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12#\n\x04left\x18\x02 \x01(\x0b\x32\x15.ics23.ExistenceProof\x12$\n\x05right\x18\x03 \x01(\x0b\x32\x15.ics23.ExistenceProof\"\xc7\x01\n\x0f\x43ommitmentProof\x12&\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b\x32\x18.ics23.NonExistenceProofH\x00\x12\"\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32\x11.ics23.BatchProofH\x00\x12\x31\n\ncompressed\x18\x04 \x01(\x0b\x32\x1b.ics23.CompressedBatchProofH\x00\x42\x07\n\x05proof\"\xa0\x01\n\x06LeafOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e\x32\r.ics23.HashOp\x12\"\n\x0bprehash_key\x18\x02 \x01(\x0e\x32\r.ics23.HashOp\x12$\n\rprehash_value\x18\x03 \x01(\x0e\x32\r.ics23.HashOp\x12\x1f\n\x06length\x18\x04 \x01(\x0e\x32\x0f.ics23.LengthOp\x12\x0e\n\x06prefix\x18\x05 \x01(\x0c\"F\n\x07InnerOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e\x32\r.ics23.HashOp\x12\x0e\n\x06prefix\x18\x02 \x01(\x0c\x12\x0e\n\x06suffix\x18\x03 \x01(\x0c\"y\n\tProofSpec\x12 \n\tleaf_spec\x18\x01 \x01(\x0b\x32\r.ics23.LeafOp\x12$\n\ninner_spec\x18\x02 \x01(\x0b\x32\x10.ics23.InnerSpec\x12\x11\n\tmax_depth\x18\x03 \x01(\x05\x12\x11\n\tmin_depth\x18\x04 \x01(\x05\"\x9c\x01\n\tInnerSpec\x12\x13\n\x0b\x63hild_order\x18\x01 \x03(\x05\x12\x12\n\nchild_size\x18\x02 \x01(\x05\x12\x19\n\x11min_prefix_length\x18\x03 \x01(\x05\x12\x19\n\x11max_prefix_length\x18\x04 \x01(\x05\x12\x13\n\x0b\x65mpty_child\x18\x05 \x01(\x0c\x12\x1b\n\x04hash\x18\x06 \x01(\x0e\x32\r.ics23.HashOp\"0\n\nBatchProof\x12\"\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x11.ics23.BatchEntry\"k\n\nBatchEntry\x12&\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b\x32\x18.ics23.NonExistenceProofH\x00\x42\x07\n\x05proof\"k\n\x14\x43ompressedBatchProof\x12,\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1b.ics23.CompressedBatchEntry\x12%\n\rlookup_inners\x18\x02 \x03(\x0b\x32\x0e.ics23.InnerOp\"\x89\x01\n\x14\x43ompressedBatchEntry\x12\x30\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProofH\x00\x12\x36\n\x08nonexist\x18\x02 \x01(\x0b\x32\".ics23.CompressedNonExistenceProofH\x00\x42\x07\n\x05proof\"a\n\x18\x43ompressedExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b\x32\r.ics23.LeafOp\x12\x0c\n\x04path\x18\x04 \x03(\x05\"\x89\x01\n\x1b\x43ompressedNonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12-\n\x04left\x18\x02 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProof\x12.\n\x05right\x18\x03 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProof*U\n\x06HashOp\x12\x0b\n\x07NO_HASH\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\n\n\x06SHA512\x10\x02\x12\n\n\x06KECCAK\x10\x03\x12\r\n\tRIPEMD160\x10\x04\x12\x0b\n\x07\x42ITCOIN\x10\x05*\xab\x01\n\x08LengthOp\x12\r\n\tNO_PREFIX\x10\x00\x12\r\n\tVAR_PROTO\x10\x01\x12\x0b\n\x07VAR_RLP\x10\x02\x12\x0f\n\x0b\x46IXED32_BIG\x10\x03\x12\x12\n\x0e\x46IXED32_LITTLE\x10\x04\x12\x0f\n\x0b\x46IXED64_BIG\x10\x05\x12\x12\n\x0e\x46IXED64_LITTLE\x10\x06\x12\x14\n\x10REQUIRE_32_BYTES\x10\x07\x12\x14\n\x10REQUIRE_64_BYTES\x10\x08\x42\x1cZ\x1agithub.com/confio/ics23/gob\x06proto3')

_HASHOP = DESCRIPTOR.enum_types_by_name['HashOp']
HashOp = enum_type_wrapper.EnumTypeWrapper(_HASHOP)
_LENGTHOP = DESCRIPTOR.enum_types_by_name['LengthOp']
LengthOp = enum_type_wrapper.EnumTypeWrapper(_LENGTHOP)
NO_HASH = 0
SHA256 = 1
SHA512 = 2
KECCAK = 3
RIPEMD160 = 4
BITCOIN = 5
NO_PREFIX = 0
VAR_PROTO = 1
VAR_RLP = 2
FIXED32_BIG = 3
FIXED32_LITTLE = 4
FIXED64_BIG = 5
FIXED64_LITTLE = 6
REQUIRE_32_BYTES = 7
REQUIRE_64_BYTES = 8


_EXISTENCEPROOF = DESCRIPTOR.message_types_by_name['ExistenceProof']
_NONEXISTENCEPROOF = DESCRIPTOR.message_types_by_name['NonExistenceProof']
_COMMITMENTPROOF = DESCRIPTOR.message_types_by_name['CommitmentProof']
_LEAFOP = DESCRIPTOR.message_types_by_name['LeafOp']
_INNEROP = DESCRIPTOR.message_types_by_name['InnerOp']
_PROOFSPEC = DESCRIPTOR.message_types_by_name['ProofSpec']
_INNERSPEC = DESCRIPTOR.message_types_by_name['InnerSpec']
_BATCHPROOF = DESCRIPTOR.message_types_by_name['BatchProof']
_BATCHENTRY = DESCRIPTOR.message_types_by_name['BatchEntry']
_COMPRESSEDBATCHPROOF = DESCRIPTOR.message_types_by_name['CompressedBatchProof']
_COMPRESSEDBATCHENTRY = DESCRIPTOR.message_types_by_name['CompressedBatchEntry']
_COMPRESSEDEXISTENCEPROOF = DESCRIPTOR.message_types_by_name['CompressedExistenceProof']
_COMPRESSEDNONEXISTENCEPROOF = DESCRIPTOR.message_types_by_name['CompressedNonExistenceProof']
ExistenceProof = _reflection.GeneratedProtocolMessageType('ExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _EXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.ExistenceProof)
  })
_sym_db.RegisterMessage(ExistenceProof)

NonExistenceProof = _reflection.GeneratedProtocolMessageType('NonExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _NONEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.NonExistenceProof)
  })
_sym_db.RegisterMessage(NonExistenceProof)

CommitmentProof = _reflection.GeneratedProtocolMessageType('CommitmentProof', (_message.Message,), {
  'DESCRIPTOR' : _COMMITMENTPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CommitmentProof)
  })
_sym_db.RegisterMessage(CommitmentProof)

LeafOp = _reflection.GeneratedProtocolMessageType('LeafOp', (_message.Message,), {
  'DESCRIPTOR' : _LEAFOP,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.LeafOp)
  })
_sym_db.RegisterMessage(LeafOp)

InnerOp = _reflection.GeneratedProtocolMessageType('InnerOp', (_message.Message,), {
  'DESCRIPTOR' : _INNEROP,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.InnerOp)
  })
_sym_db.RegisterMessage(InnerOp)

ProofSpec = _reflection.GeneratedProtocolMessageType('ProofSpec', (_message.Message,), {
  'DESCRIPTOR' : _PROOFSPEC,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.ProofSpec)
  })
_sym_db.RegisterMessage(ProofSpec)

InnerSpec = _reflection.GeneratedProtocolMessageType('InnerSpec', (_message.Message,), {
  'DESCRIPTOR' : _INNERSPEC,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.InnerSpec)
  })
_sym_db.RegisterMessage(InnerSpec)

BatchProof = _reflection.GeneratedProtocolMessageType('BatchProof', (_message.Message,), {
  'DESCRIPTOR' : _BATCHPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.BatchProof)
  })
_sym_db.RegisterMessage(BatchProof)

BatchEntry = _reflection.GeneratedProtocolMessageType('BatchEntry', (_message.Message,), {
  'DESCRIPTOR' : _BATCHENTRY,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.BatchEntry)
  })
_sym_db.RegisterMessage(BatchEntry)

CompressedBatchProof = _reflection.GeneratedProtocolMessageType('CompressedBatchProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDBATCHPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedBatchProof)
  })
_sym_db.RegisterMessage(CompressedBatchProof)

CompressedBatchEntry = _reflection.GeneratedProtocolMessageType('CompressedBatchEntry', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDBATCHENTRY,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedBatchEntry)
  })
_sym_db.RegisterMessage(CompressedBatchEntry)

CompressedExistenceProof = _reflection.GeneratedProtocolMessageType('CompressedExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedExistenceProof)
  })
_sym_db.RegisterMessage(CompressedExistenceProof)

CompressedNonExistenceProof = _reflection.GeneratedProtocolMessageType('CompressedNonExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDNONEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedNonExistenceProof)
  })
_sym_db.RegisterMessage(CompressedNonExistenceProof)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032github.com/confio/ics23/go'
  _HASHOP._serialized_start=1610
  _HASHOP._serialized_end=1695
  _LENGTHOP._serialized_start=1698
  _LENGTHOP._serialized_end=1869
  _EXISTENCEPROOF._serialized_start=30
  _EXISTENCEPROOF._serialized_end=133
  _NONEXISTENCEPROOF._serialized_start=135
  _NONEXISTENCEPROOF._serialized_end=242
  _COMMITMENTPROOF._serialized_start=245
  _COMMITMENTPROOF._serialized_end=444
  _LEAFOP._serialized_start=447
  _LEAFOP._serialized_end=607
  _INNEROP._serialized_start=609
  _INNEROP._serialized_end=679
  _PROOFSPEC._serialized_start=681
  _PROOFSPEC._serialized_end=802
  _INNERSPEC._serialized_start=805
  _INNERSPEC._serialized_end=961
  _BATCHPROOF._serialized_start=963
  _BATCHPROOF._serialized_end=1011
  _BATCHENTRY._serialized_start=1013
  _BATCHENTRY._serialized_end=1120
  _COMPRESSEDBATCHPROOF._serialized_start=1122
  _COMPRESSEDBATCHPROOF._serialized_end=1229
  _COMPRESSEDBATCHENTRY._serialized_start=1232
  _COMPRESSEDBATCHENTRY._serialized_end=1369
  _COMPRESSEDEXISTENCEPROOF._serialized_start=1371
  _COMPRESSEDEXISTENCEPROOF._serialized_end=1468
  _COMPRESSEDNONEXISTENCEPROOF._serialized_start=1471
  _COMPRESSEDNONEXISTENCEPROOF._serialized_end=1608
# @@protoc_insertion_point(module_scope)

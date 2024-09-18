"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/mint/v1beta1/mint.proto\x12\x13cosmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\x9c\x01\n\x06Minter\x12D\n\tinflation\x18\x01 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\x12L\n\x11annual_provisions\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec"\x96\x03\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12U\n\x15inflation_rate_change\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12M\n\rinflation_max\x18\x03 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12M\n\rinflation_min\x18\x04 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12K\n\x0bgoal_bonded\x18\x05 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12\x17\n\x0fblocks_per_year\x18\x06 \x01(\x04:\x1d\x8a\xe7\xb0*\x18cosmos-sdk/x/mint/ParamsB+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.mint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
    _globals['_MINTER'].fields_by_name['inflation']._options = None
    _globals['_MINTER'].fields_by_name['inflation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec'
    _globals['_MINTER'].fields_by_name['annual_provisions']._options = None
    _globals['_MINTER'].fields_by_name['annual_provisions']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec'
    _globals['_PARAMS'].fields_by_name['inflation_rate_change']._options = None
    _globals['_PARAMS'].fields_by_name['inflation_rate_change']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS'].fields_by_name['inflation_max']._options = None
    _globals['_PARAMS'].fields_by_name['inflation_max']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS'].fields_by_name['inflation_min']._options = None
    _globals['_PARAMS'].fields_by_name['inflation_min']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS'].fields_by_name['goal_bonded']._options = None
    _globals['_PARAMS'].fields_by_name['goal_bonded']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS']._options = None
    _globals['_PARAMS']._serialized_options = b'\x8a\xe7\xb0*\x18cosmos-sdk/x/mint/Params'
    _globals['_MINTER']._serialized_start = 124
    _globals['_MINTER']._serialized_end = 280
    _globals['_PARAMS']._serialized_start = 283
    _globals['_PARAMS']._serialized_end = 689
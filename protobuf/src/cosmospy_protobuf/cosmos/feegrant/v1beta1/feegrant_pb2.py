"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/feegrant/v1beta1/feegrant.proto\x12\x17cosmos.feegrant.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x11amino/amino.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto"\x87\x02\n\x0eBasicAllowance\x12v\n\x0bspend_limit\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x124\n\nexpiration\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01:G\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x19cosmos-sdk/BasicAllowance"\x99\x04\n\x11PeriodicAllowance\x12A\n\x05basic\x18\x01 \x01(\x0b2\'.cosmos.feegrant.v1beta1.BasicAllowanceB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x128\n\x06period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12}\n\x12period_spend_limit\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12{\n\x10period_can_spend\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12?\n\x0cperiod_reset\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01:J\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x1ccosmos-sdk/PeriodicAllowance"\xd5\x01\n\x13AllowedMsgAllowance\x12R\n\tallowance\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB)\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x12\x18\n\x10allowed_messages\x18\x02 \x03(\t:P\x88\xa0\x1f\x00\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x1ecosmos-sdk/AllowedMsgAllowance"\xb1\x01\n\x05Grant\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12R\n\tallowance\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB)\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceIB\x19Z\x17cosmossdk.io/x/feegrantb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.feegrant_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x17cosmossdk.io/x/feegrant'
    _globals['_BASICALLOWANCE'].fields_by_name['spend_limit']._options = None
    _globals['_BASICALLOWANCE'].fields_by_name['spend_limit']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_BASICALLOWANCE'].fields_by_name['expiration']._options = None
    _globals['_BASICALLOWANCE'].fields_by_name['expiration']._serialized_options = b'\x90\xdf\x1f\x01'
    _globals['_BASICALLOWANCE']._options = None
    _globals['_BASICALLOWANCE']._serialized_options = b'\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x19cosmos-sdk/BasicAllowance'
    _globals['_PERIODICALLOWANCE'].fields_by_name['basic']._options = None
    _globals['_PERIODICALLOWANCE'].fields_by_name['basic']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_PERIODICALLOWANCE'].fields_by_name['period']._options = None
    _globals['_PERIODICALLOWANCE'].fields_by_name['period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_spend_limit']._options = None
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_spend_limit']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_can_spend']._options = None
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_can_spend']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_reset']._options = None
    _globals['_PERIODICALLOWANCE'].fields_by_name['period_reset']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_PERIODICALLOWANCE']._options = None
    _globals['_PERIODICALLOWANCE']._serialized_options = b'\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x1ccosmos-sdk/PeriodicAllowance'
    _globals['_ALLOWEDMSGALLOWANCE'].fields_by_name['allowance']._options = None
    _globals['_ALLOWEDMSGALLOWANCE'].fields_by_name['allowance']._serialized_options = b'\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI'
    _globals['_ALLOWEDMSGALLOWANCE']._options = None
    _globals['_ALLOWEDMSGALLOWANCE']._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI\x8a\xe7\xb0*\x1ecosmos-sdk/AllowedMsgAllowance'
    _globals['_GRANT'].fields_by_name['granter']._options = None
    _globals['_GRANT'].fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GRANT'].fields_by_name['grantee']._options = None
    _globals['_GRANT'].fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GRANT'].fields_by_name['allowance']._options = None
    _globals['_GRANT'].fields_by_name['allowance']._serialized_options = b'\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI'
    _globals['_BASICALLOWANCE']._serialized_start = 260
    _globals['_BASICALLOWANCE']._serialized_end = 523
    _globals['_PERIODICALLOWANCE']._serialized_start = 526
    _globals['_PERIODICALLOWANCE']._serialized_end = 1063
    _globals['_ALLOWEDMSGALLOWANCE']._serialized_start = 1066
    _globals['_ALLOWEDMSGALLOWANCE']._serialized_end = 1279
    _globals['_GRANT']._serialized_start = 1282
    _globals['_GRANT']._serialized_end = 1459
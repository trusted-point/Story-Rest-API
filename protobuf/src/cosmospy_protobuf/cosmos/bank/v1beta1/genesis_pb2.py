"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/bank/v1beta1/genesis.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\xf9\x02\n\x0cGenesisState\x126\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x129\n\x08balances\x18\x02 \x03(\x0b2\x1c.cosmos.bank.v1beta1.BalanceB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12q\n\x06supply\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12@\n\x0edenom_metadata\x18\x04 \x03(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12A\n\x0csend_enabled\x18\x05 \x03(\x0b2 .cosmos.bank.v1beta1.SendEnabledB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\xb0\x01\n\x07Balance\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12p\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _globals['_GENESISSTATE'].fields_by_name['params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['balances']._options = None
    _globals['_GENESISSTATE'].fields_by_name['balances']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['supply']._options = None
    _globals['_GENESISSTATE'].fields_by_name['supply']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['denom_metadata']._options = None
    _globals['_GENESISSTATE'].fields_by_name['denom_metadata']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['send_enabled']._options = None
    _globals['_GENESISSTATE'].fields_by_name['send_enabled']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_BALANCE'].fields_by_name['address']._options = None
    _globals['_BALANCE'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_BALANCE'].fields_by_name['coins']._options = None
    _globals['_BALANCE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_BALANCE']._options = None
    _globals['_BALANCE']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 191
    _globals['_GENESISSTATE']._serialized_end = 568
    _globals['_BALANCE']._serialized_start = 571
    _globals['_BALANCE']._serialized_end = 747
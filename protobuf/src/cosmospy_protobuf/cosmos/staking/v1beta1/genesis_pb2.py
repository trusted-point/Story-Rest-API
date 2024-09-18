"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/genesis.proto\x12\x16cosmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\xa2\x04\n\x0cGenesisState\x129\n\x06params\x18\x01 \x01(\x0b2\x1e.cosmos.staking.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12J\n\x10last_total_power\x18\x02 \x01(\x0cB0\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01\x12T\n\x15last_validator_powers\x18\x03 \x03(\x0b2*.cosmos.staking.v1beta1.LastValidatorPowerB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12@\n\nvalidators\x18\x04 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12B\n\x0bdelegations\x18\x05 \x03(\x0b2".cosmos.staking.v1beta1.DelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12U\n\x15unbonding_delegations\x18\x06 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12F\n\rredelegations\x18\x07 \x03(\x0b2$.cosmos.staking.v1beta1.RedelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x10\n\x08exported\x18\x08 \x01(\x08"X\n\x12LastValidatorPower\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\r\n\x05power\x18\x02 \x01(\x03:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _globals['_GENESISSTATE'].fields_by_name['params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['last_total_power']._options = None
    _globals['_GENESISSTATE'].fields_by_name['last_total_power']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['last_validator_powers']._options = None
    _globals['_GENESISSTATE'].fields_by_name['last_validator_powers']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['validators']._options = None
    _globals['_GENESISSTATE'].fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['delegations']._options = None
    _globals['_GENESISSTATE'].fields_by_name['delegations']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['unbonding_delegations']._options = None
    _globals['_GENESISSTATE'].fields_by_name['unbonding_delegations']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['redelegations']._options = None
    _globals['_GENESISSTATE'].fields_by_name['redelegations']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_LASTVALIDATORPOWER'].fields_by_name['address']._options = None
    _globals['_LASTVALIDATORPOWER'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_LASTVALIDATORPOWER']._options = None
    _globals['_LASTVALIDATORPOWER']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 171
    _globals['_GENESISSTATE']._serialized_end = 717
    _globals['_LASTVALIDATORPOWER']._serialized_start = 719
    _globals['_LASTVALIDATORPOWER']._serialized_end = 807
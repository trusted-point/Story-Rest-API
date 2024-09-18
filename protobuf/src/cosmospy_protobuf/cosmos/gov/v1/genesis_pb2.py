"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/gov/v1/genesis.proto\x12\rcosmos.gov.v1\x1a\x17cosmos/gov/v1/gov.proto"\x8b\x03\n\x0cGenesisState\x12\x1c\n\x14starting_proposal_id\x18\x01 \x01(\x04\x12(\n\x08deposits\x18\x02 \x03(\x0b2\x16.cosmos.gov.v1.Deposit\x12"\n\x05votes\x18\x03 \x03(\x0b2\x13.cosmos.gov.v1.Vote\x12*\n\tproposals\x18\x04 \x03(\x0b2\x17.cosmos.gov.v1.Proposal\x128\n\x0edeposit_params\x18\x05 \x01(\x0b2\x1c.cosmos.gov.v1.DepositParamsB\x02\x18\x01\x126\n\rvoting_params\x18\x06 \x01(\x0b2\x1b.cosmos.gov.v1.VotingParamsB\x02\x18\x01\x124\n\x0ctally_params\x18\x07 \x01(\x0b2\x1a.cosmos.gov.v1.TallyParamsB\x02\x18\x01\x12%\n\x06params\x18\x08 \x01(\x0b2\x15.cosmos.gov.v1.Params\x12\x14\n\x0cconstitution\x18\t \x01(\tB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
    _globals['_GENESISSTATE'].fields_by_name['deposit_params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['deposit_params']._serialized_options = b'\x18\x01'
    _globals['_GENESISSTATE'].fields_by_name['voting_params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['voting_params']._serialized_options = b'\x18\x01'
    _globals['_GENESISSTATE'].fields_by_name['tally_params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['tally_params']._serialized_options = b'\x18\x01'
    _globals['_GENESISSTATE']._serialized_start = 72
    _globals['_GENESISSTATE']._serialized_end = 467
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\xe4\x01\n\x0cGenesisState\x12:\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12F\n\rsigning_infos\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.SigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12P\n\rmissed_blocks\x18\x03 \x03(\x0b2..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x9b\x01\n\x0bSigningInfo\x122\n\x07address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ConsensusAddressString\x12X\n\x16validator_signing_info\x18\x02 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x93\x01\n\x15ValidatorMissedBlocks\x122\n\x07address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ConsensusAddressString\x12F\n\rmissed_blocks\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.MissedBlockB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08B/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _globals['_GENESISSTATE'].fields_by_name['params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['signing_infos']._options = None
    _globals['_GENESISSTATE'].fields_by_name['signing_infos']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._options = None
    _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_SIGNINGINFO'].fields_by_name['address']._options = None
    _globals['_SIGNINGINFO'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ConsensusAddressString'
    _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._options = None
    _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._options = None
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ConsensusAddressString'
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._options = None
    _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_GENESISSTATE']._serialized_start = 175
    _globals['_GENESISSTATE']._serialized_end = 403
    _globals['_SIGNINGINFO']._serialized_start = 406
    _globals['_SIGNINGINFO']._serialized_end = 561
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_start = 564
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_end = 711
    _globals['_MISSEDBLOCK']._serialized_start = 713
    _globals['_MISSEDBLOCK']._serialized_end = 757
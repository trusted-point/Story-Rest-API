"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from .....tendermint.types import evidence_pb2 as tendermint_dot_types_dot_evidence__pb2
from .....tendermint.version import types_pb2 as tendermint_dot_version_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/types.proto\x12\x1ecosmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a\x1ftendermint/types/evidence.proto\x1a\x1etendermint/version/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x11amino/amino.proto"\xe7\x01\n\x05Block\x12A\n\x06header\x18\x01 \x01(\x0b2&.cosmos.base.tendermint.v1beta1.HeaderB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12/\n\x04data\x18\x02 \x01(\x0b2\x16.tendermint.types.DataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\x08evidence\x18\x03 \x01(\x0b2\x1e.tendermint.types.EvidenceListB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12-\n\x0blast_commit\x18\x04 \x01(\x0b2\x18.tendermint.types.Commit"\xc2\x03\n\x06Header\x129\n\x07version\x18\x01 \x01(\x0b2\x1d.tendermint.version.ConsensusB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x1d\n\x08chain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07ChainID\x12\x0e\n\x06height\x18\x03 \x01(\x03\x127\n\x04time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12;\n\rlast_block_id\x18\x05 \x01(\x0b2\x19.tendermint.types.BlockIDB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x18\n\x10last_commit_hash\x18\x06 \x01(\x0c\x12\x11\n\tdata_hash\x18\x07 \x01(\x0c\x12\x17\n\x0fvalidators_hash\x18\x08 \x01(\x0c\x12\x1c\n\x14next_validators_hash\x18\t \x01(\x0c\x12\x16\n\x0econsensus_hash\x18\n \x01(\x0c\x12\x10\n\x08app_hash\x18\x0b \x01(\x0c\x12\x19\n\x11last_results_hash\x18\x0c \x01(\x0c\x12\x15\n\revidence_hash\x18\r \x01(\x0c\x12\x18\n\x10proposer_address\x18\x0e \x01(\tB5Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtserviceb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.tendermint.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtservice'
    _globals['_BLOCK'].fields_by_name['header']._options = None
    _globals['_BLOCK'].fields_by_name['header']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_BLOCK'].fields_by_name['data']._options = None
    _globals['_BLOCK'].fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_BLOCK'].fields_by_name['evidence']._options = None
    _globals['_BLOCK'].fields_by_name['evidence']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_HEADER'].fields_by_name['version']._options = None
    _globals['_HEADER'].fields_by_name['version']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_HEADER'].fields_by_name['chain_id']._options = None
    _globals['_HEADER'].fields_by_name['chain_id']._serialized_options = b'\xe2\xde\x1f\x07ChainID'
    _globals['_HEADER'].fields_by_name['time']._options = None
    _globals['_HEADER'].fields_by_name['time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_HEADER'].fields_by_name['last_block_id']._options = None
    _globals['_HEADER'].fields_by_name['last_block_id']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_BLOCK']._serialized_start = 248
    _globals['_BLOCK']._serialized_end = 479
    _globals['_HEADER']._serialized_start = 482
    _globals['_HEADER']._serialized_end = 932
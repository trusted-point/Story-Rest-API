"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.nft.v1beta1 import nft_pb2 as cosmos_dot_nft_dot_v1beta1_dot_nft__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/nft/v1beta1/genesis.proto\x12\x12cosmos.nft.v1beta1\x1a\x1ccosmos/nft/v1beta1/nft.proto"f\n\x0cGenesisState\x12*\n\x07classes\x18\x01 \x03(\x0b2\x19.cosmos.nft.v1beta1.Class\x12*\n\x07entries\x18\x02 \x03(\x0b2\x19.cosmos.nft.v1beta1.Entry"=\n\x05Entry\x12\r\n\x05owner\x18\x01 \x01(\t\x12%\n\x04nfts\x18\x02 \x03(\x0b2\x17.cosmos.nft.v1beta1.NFTB\x14Z\x12cosmossdk.io/x/nftb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x12cosmossdk.io/x/nft'
    _globals['_GENESISSTATE']._serialized_start = 86
    _globals['_GENESISSTATE']._serialized_end = 188
    _globals['_ENTRY']._serialized_start = 190
    _globals['_ENTRY']._serialized_end = 251
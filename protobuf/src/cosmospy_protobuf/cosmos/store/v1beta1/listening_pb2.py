"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/store/v1beta1/listening.proto\x12\x14cosmos.store.v1beta1\x1a\x1btendermint/abci/types.proto"L\n\x0bStoreKVPair\x12\x11\n\tstore_key\x18\x01 \x01(\t\x12\x0e\n\x06delete\x18\x02 \x01(\x08\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\r\n\x05value\x18\x04 \x01(\x0c"\xf7\x01\n\rBlockMetadata\x128\n\x0fresponse_commit\x18\x06 \x01(\x0b2\x1f.tendermint.abci.ResponseCommit\x12E\n\x16request_finalize_block\x18\x07 \x01(\x0b2%.tendermint.abci.RequestFinalizeBlock\x12G\n\x17response_finalize_block\x18\x08 \x01(\x0b2&.tendermint.abci.ResponseFinalizeBlockJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06B\x1aZ\x18cosmossdk.io/store/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.v1beta1.listening_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18cosmossdk.io/store/types'
    _globals['_STOREKVPAIR']._serialized_start = 91
    _globals['_STOREKVPAIR']._serialized_end = 167
    _globals['_BLOCKMETADATA']._serialized_start = 170
    _globals['_BLOCKMETADATA']._serialized_end = 417
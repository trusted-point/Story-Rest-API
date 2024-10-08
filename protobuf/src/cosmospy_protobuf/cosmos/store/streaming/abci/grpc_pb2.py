"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
from .....cosmos.store.v1beta1 import listening_pb2 as cosmos_dot_store_dot_v1beta1_dot_listening__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/store/streaming/abci/grpc.proto\x12\x1bcosmos.store.streaming.abci\x1a\x1btendermint/abci/types.proto\x1a$cosmos/store/v1beta1/listening.proto"\x85\x01\n\x1aListenFinalizeBlockRequest\x122\n\x03req\x18\x01 \x01(\x0b2%.tendermint.abci.RequestFinalizeBlock\x123\n\x03res\x18\x02 \x01(\x0b2&.tendermint.abci.ResponseFinalizeBlock"\x1d\n\x1bListenFinalizeBlockResponse"\x90\x01\n\x13ListenCommitRequest\x12\x14\n\x0cblock_height\x18\x01 \x01(\x03\x12,\n\x03res\x18\x02 \x01(\x0b2\x1f.tendermint.abci.ResponseCommit\x125\n\nchange_set\x18\x03 \x03(\x0b2!.cosmos.store.v1beta1.StoreKVPair"\x16\n\x14ListenCommitResponse2\x95\x02\n\x13ABCIListenerService\x12\x88\x01\n\x13ListenFinalizeBlock\x127.cosmos.store.streaming.abci.ListenFinalizeBlockRequest\x1a8.cosmos.store.streaming.abci.ListenFinalizeBlockResponse\x12s\n\x0cListenCommit\x120.cosmos.store.streaming.abci.ListenCommitRequest\x1a1.cosmos.store.streaming.abci.ListenCommitResponseB#Z!cosmossdk.io/store/streaming/abcib\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.streaming.abci.grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z!cosmossdk.io/store/streaming/abci'
    _globals['_LISTENFINALIZEBLOCKREQUEST']._serialized_start = 139
    _globals['_LISTENFINALIZEBLOCKREQUEST']._serialized_end = 272
    _globals['_LISTENFINALIZEBLOCKRESPONSE']._serialized_start = 274
    _globals['_LISTENFINALIZEBLOCKRESPONSE']._serialized_end = 303
    _globals['_LISTENCOMMITREQUEST']._serialized_start = 306
    _globals['_LISTENCOMMITREQUEST']._serialized_end = 450
    _globals['_LISTENCOMMITRESPONSE']._serialized_start = 452
    _globals['_LISTENCOMMITRESPONSE']._serialized_end = 474
    _globals['_ABCILISTENERSERVICE']._serialized_start = 477
    _globals['_ABCILISTENERSERVICE']._serialized_end = 754
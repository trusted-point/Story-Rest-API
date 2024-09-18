"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18tendermint/p2p/pex.proto\x12\x0etendermint.p2p\x1a\x1atendermint/p2p/types.proto\x1a\x14gogoproto/gogo.proto"\x0c\n\nPexRequest";\n\x08PexAddrs\x12/\n\x05addrs\x18\x01 \x03(\x0b2\x1a.tendermint.p2p.NetAddressB\x04\xc8\xde\x1f\x00"r\n\x07Message\x121\n\x0bpex_request\x18\x01 \x01(\x0b2\x1a.tendermint.p2p.PexRequestH\x00\x12-\n\tpex_addrs\x18\x02 \x01(\x0b2\x18.tendermint.p2p.PexAddrsH\x00B\x05\n\x03sumB3Z1github.com/cometbft/cometbft/proto/tendermint/p2pb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.p2p.pex_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cometbft/cometbft/proto/tendermint/p2p'
    _globals['_PEXADDRS'].fields_by_name['addrs']._options = None
    _globals['_PEXADDRS'].fields_by_name['addrs']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PEXREQUEST']._serialized_start = 94
    _globals['_PEXREQUEST']._serialized_end = 106
    _globals['_PEXADDRS']._serialized_start = 108
    _globals['_PEXADDRS']._serialized_end = 167
    _globals['_MESSAGE']._serialized_start = 169
    _globals['_MESSAGE']._serialized_end = 283
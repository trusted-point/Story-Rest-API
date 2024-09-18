"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....amino import amino_pb2 as amino_dot_amino__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/crypto/hd/v1/hd.proto\x12\x13cosmos.crypto.hd.v1\x1a\x11amino/amino.proto\x1a\x14gogoproto/gogo.proto"\x8e\x01\n\x0bBIP44Params\x12\x0f\n\x07purpose\x18\x01 \x01(\r\x12\x11\n\tcoin_type\x18\x02 \x01(\r\x12\x0f\n\x07account\x18\x03 \x01(\r\x12\x0e\n\x06change\x18\x04 \x01(\x08\x12\x15\n\raddress_index\x18\x05 \x01(\r:#\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1acrypto/keys/hd/BIP44ParamsB,Z&github.com/cosmos/cosmos-sdk/crypto/hd\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.hd.v1.hd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z&github.com/cosmos/cosmos-sdk/crypto/hd\xc8\xe1\x1e\x00'
    _globals['_BIP44PARAMS']._options = None
    _globals['_BIP44PARAMS']._serialized_options = b'\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1acrypto/keys/hd/BIP44Params'
    _globals['_BIP44PARAMS']._serialized_start = 95
    _globals['_BIP44PARAMS']._serialized_end = 237
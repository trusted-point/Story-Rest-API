"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/crypto/secp256r1/keys.proto\x12\x17cosmos.crypto.secp256r1\x1a\x14gogoproto/gogo.proto""\n\x06PubKey\x12\x18\n\x03key\x18\x01 \x01(\x0cB\x0b\xda\xde\x1f\x07ecdsaPK"&\n\x07PrivKey\x12\x1b\n\x06secret\x18\x01 \x01(\x0cB\x0b\xda\xde\x1f\x07ecdsaSKB@Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xc8\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256r1.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xc8\xe3\x1e\x01'
    _globals['_PUBKEY'].fields_by_name['key']._options = None
    _globals['_PUBKEY'].fields_by_name['key']._serialized_options = b'\xda\xde\x1f\x07ecdsaPK'
    _globals['_PRIVKEY'].fields_by_name['secret']._options = None
    _globals['_PRIVKEY'].fields_by_name['secret']._serialized_options = b'\xda\xde\x1f\x07ecdsaSK'
    _globals['_PUBKEY']._serialized_start = 85
    _globals['_PUBKEY']._serialized_end = 119
    _globals['_PRIVKEY']._serialized_start = 121
    _globals['_PRIVKEY']._serialized_end = 159
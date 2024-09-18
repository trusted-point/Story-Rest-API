"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/crypto/multisig/keys.proto\x12\x16cosmos.crypto.multisig\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x11amino/amino.proto"\xac\x01\n\x11LegacyAminoPubKey\x12\x11\n\tthreshold\x18\x01 \x01(\r\x12B\n\x0bpublic_keys\x18\x02 \x03(\x0b2\x14.google.protobuf.AnyB\x17\xe2\xde\x1f\x07PubKeys\xa2\xe7\xb0*\x07pubkeys:@\x88\xa0\x1f\x00\x8a\xe7\xb0*"tendermint/PubKeyMultisigThreshold\x92\xe7\xb0*\x10threshold_stringB3Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisigb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.multisig.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisig'
    _globals['_LEGACYAMINOPUBKEY'].fields_by_name['public_keys']._options = None
    _globals['_LEGACYAMINOPUBKEY'].fields_by_name['public_keys']._serialized_options = b'\xe2\xde\x1f\x07PubKeys\xa2\xe7\xb0*\x07pubkeys'
    _globals['_LEGACYAMINOPUBKEY']._options = None
    _globals['_LEGACYAMINOPUBKEY']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0*"tendermint/PubKeyMultisigThreshold\x92\xe7\xb0*\x10threshold_string'
    _globals['_LEGACYAMINOPUBKEY']._serialized_start = 130
    _globals['_LEGACYAMINOPUBKEY']._serialized_end = 302
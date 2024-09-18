"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/authz.proto\x12\x14cosmos.authz.v1beta1\x1a\x11amino/amino.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"o\n\x14GenericAuthorization\x12\x0b\n\x03msg\x18\x01 \x01(\t:J\xca\xb4-"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\x1fcosmos-sdk/GenericAuthorization"\x96\x01\n\x05Grant\x12S\n\rauthorization\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB&\xca\xb4-"cosmos.authz.v1beta1.Authorization\x128\n\nexpiration\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x01\x90\xdf\x1f\x01"\xf5\x01\n\x12GrantAuthorization\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12S\n\rauthorization\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB&\xca\xb4-"cosmos.authz.v1beta1.Authorization\x124\n\nexpiration\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01"\'\n\x0eGrantQueueItem\x12\x15\n\rmsg_type_urls\x18\x01 \x03(\tB*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00'
    _globals['_GENERICAUTHORIZATION']._options = None
    _globals['_GENERICAUTHORIZATION']._serialized_options = b'\xca\xb4-"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\x1fcosmos-sdk/GenericAuthorization'
    _globals['_GRANT'].fields_by_name['authorization']._options = None
    _globals['_GRANT'].fields_by_name['authorization']._serialized_options = b'\xca\xb4-"cosmos.authz.v1beta1.Authorization'
    _globals['_GRANT'].fields_by_name['expiration']._options = None
    _globals['_GRANT'].fields_by_name['expiration']._serialized_options = b'\xc8\xde\x1f\x01\x90\xdf\x1f\x01'
    _globals['_GRANTAUTHORIZATION'].fields_by_name['granter']._options = None
    _globals['_GRANTAUTHORIZATION'].fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GRANTAUTHORIZATION'].fields_by_name['grantee']._options = None
    _globals['_GRANTAUTHORIZATION'].fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GRANTAUTHORIZATION'].fields_by_name['authorization']._options = None
    _globals['_GRANTAUTHORIZATION'].fields_by_name['authorization']._serialized_options = b'\xca\xb4-"cosmos.authz.v1beta1.Authorization'
    _globals['_GRANTAUTHORIZATION'].fields_by_name['expiration']._options = None
    _globals['_GRANTAUTHORIZATION'].fields_by_name['expiration']._serialized_options = b'\x90\xdf\x1f\x01'
    _globals['_GENERICAUTHORIZATION']._serialized_start = 186
    _globals['_GENERICAUTHORIZATION']._serialized_end = 297
    _globals['_GRANT']._serialized_start = 300
    _globals['_GRANT']._serialized_end = 450
    _globals['_GRANTAUTHORIZATION']._serialized_start = 453
    _globals['_GRANTAUTHORIZATION']._serialized_end = 698
    _globals['_GRANTQUEUEITEM']._serialized_start = 700
    _globals['_GRANTQUEUEITEM']._serialized_end = 739
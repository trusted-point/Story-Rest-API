"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/auth/v1beta1/auth.proto\x12\x13cosmos.auth.v1beta1\x1a\x11amino/amino.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xf7\x01\n\x0bBaseAccount\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12N\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\'\xea\xde\x1f\x14public_key,omitempty\xa2\xe7\xb0*\npublic_key\x12\x16\n\x0eaccount_number\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\x04:C\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1ccosmos.auth.v1beta1.AccountI\x8a\xe7\xb0*\x16cosmos-sdk/BaseAccount"\xcc\x01\n\rModuleAccount\x12<\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t:Z\x88\xa0\x1f\x00\xca\xb4-"cosmos.auth.v1beta1.ModuleAccountI\x8a\xe7\xb0*\x18cosmos-sdk/ModuleAccount\x92\xe7\xb0*\x0emodule_account"h\n\x10ModuleCredential\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x17\n\x0fderivation_keys\x18\x02 \x03(\x0c:&\x8a\xe7\xb0*!cosmos-sdk/GroupAccountCredential"\xf7\x01\n\x06Params\x12\x1b\n\x13max_memo_characters\x18\x01 \x01(\x04\x12\x14\n\x0ctx_sig_limit\x18\x02 \x01(\x04\x12\x1d\n\x15tx_size_cost_per_byte\x18\x03 \x01(\x04\x129\n\x17sig_verify_cost_ed25519\x18\x04 \x01(\x04B\x18\xe2\xde\x1f\x14SigVerifyCostED25519\x12=\n\x19sig_verify_cost_secp256k1\x18\x05 \x01(\x04B\x1a\xe2\xde\x1f\x16SigVerifyCostSecp256k1:!\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x18cosmos-sdk/x/auth/ParamsB+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.auth.v1beta1.auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
    _globals['_BASEACCOUNT'].fields_by_name['address']._options = None
    _globals['_BASEACCOUNT'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_BASEACCOUNT'].fields_by_name['pub_key']._options = None
    _globals['_BASEACCOUNT'].fields_by_name['pub_key']._serialized_options = b'\xea\xde\x1f\x14public_key,omitempty\xa2\xe7\xb0*\npublic_key'
    _globals['_BASEACCOUNT']._options = None
    _globals['_BASEACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1ccosmos.auth.v1beta1.AccountI\x8a\xe7\xb0*\x16cosmos-sdk/BaseAccount'
    _globals['_MODULEACCOUNT'].fields_by_name['base_account']._options = None
    _globals['_MODULEACCOUNT'].fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_MODULEACCOUNT']._options = None
    _globals['_MODULEACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-"cosmos.auth.v1beta1.ModuleAccountI\x8a\xe7\xb0*\x18cosmos-sdk/ModuleAccount\x92\xe7\xb0*\x0emodule_account'
    _globals['_MODULECREDENTIAL']._options = None
    _globals['_MODULECREDENTIAL']._serialized_options = b'\x8a\xe7\xb0*!cosmos-sdk/GroupAccountCredential'
    _globals['_PARAMS'].fields_by_name['sig_verify_cost_ed25519']._options = None
    _globals['_PARAMS'].fields_by_name['sig_verify_cost_ed25519']._serialized_options = b'\xe2\xde\x1f\x14SigVerifyCostED25519'
    _globals['_PARAMS'].fields_by_name['sig_verify_cost_secp256k1']._options = None
    _globals['_PARAMS'].fields_by_name['sig_verify_cost_secp256k1']._serialized_options = b'\xe2\xde\x1f\x16SigVerifyCostSecp256k1'
    _globals['_PARAMS']._options = None
    _globals['_PARAMS']._serialized_options = b'\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x18cosmos-sdk/x/auth/Params'
    _globals['_BASEACCOUNT']._serialized_start = 151
    _globals['_BASEACCOUNT']._serialized_end = 398
    _globals['_MODULEACCOUNT']._serialized_start = 401
    _globals['_MODULEACCOUNT']._serialized_end = 605
    _globals['_MODULECREDENTIAL']._serialized_start = 607
    _globals['_MODULECREDENTIAL']._serialized_end = 711
    _globals['_PARAMS']._serialized_start = 714
    _globals['_PARAMS']._serialized_end = 961
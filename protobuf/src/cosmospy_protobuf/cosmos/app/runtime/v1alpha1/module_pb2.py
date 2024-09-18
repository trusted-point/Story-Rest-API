"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cosmos/app/runtime/v1alpha1/module.proto\x12\x1bcosmos.app.runtime.v1alpha1\x1a cosmos/app/v1alpha1/module.proto"\xd4\x02\n\x06Module\x12\x10\n\x08app_name\x18\x01 \x01(\t\x12\x16\n\x0ebegin_blockers\x18\x02 \x03(\t\x12\x14\n\x0cend_blockers\x18\x03 \x03(\t\x12\x14\n\x0cinit_genesis\x18\x04 \x03(\t\x12\x16\n\x0eexport_genesis\x18\x05 \x03(\t\x12H\n\x13override_store_keys\x18\x06 \x03(\x0b2+.cosmos.app.runtime.v1alpha1.StoreKeyConfig\x12\x18\n\x10order_migrations\x18\x07 \x03(\t\x12\x14\n\x0cprecommiters\x18\x08 \x03(\t\x12\x1d\n\x15prepare_check_staters\x18\t \x03(\t:C\xba\xc0\x96\xda\x01=\n$github.com/cosmos/cosmos-sdk/runtime\x12\x15\n\x13cosmos.app.v1alpha1";\n\x0eStoreKeyConfig\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x14\n\x0ckv_store_key\x18\x02 \x01(\tb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.runtime.v1alpha1.module_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_MODULE']._options = None
    _globals['_MODULE']._serialized_options = b'\xba\xc0\x96\xda\x01=\n$github.com/cosmos/cosmos-sdk/runtime\x12\x15\n\x13cosmos.app.v1alpha1'
    _globals['_MODULE']._serialized_start = 108
    _globals['_MODULE']._serialized_end = 448
    _globals['_STOREKEYCONFIG']._serialized_start = 450
    _globals['_STOREKEYCONFIG']._serialized_end = 509
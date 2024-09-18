"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/applications/fee/v1/ack.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto"\xe3\x01\n\x1bIncentivizedAcknowledgement\x12;\n\x13app_acknowledgement\x18\x01 \x01(\x0cB\x1e\xf2\xde\x1f\x1ayaml:"app_acknowledgement"\x12C\n\x17forward_relayer_address\x18\x02 \x01(\tB"\xf2\xde\x1f\x1eyaml:"forward_relayer_address"\x12B\n\x16underlying_app_success\x18\x03 \x01(\x08B"\xf2\xde\x1f\x1eyaml:"underlying_app_successl"B7Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.ack_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/types'
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['app_acknowledgement']._options = None
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['app_acknowledgement']._serialized_options = b'\xf2\xde\x1f\x1ayaml:"app_acknowledgement"'
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['forward_relayer_address']._options = None
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['forward_relayer_address']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"forward_relayer_address"'
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['underlying_app_success']._options = None
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT'].fields_by_name['underlying_app_success']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"underlying_app_successl"'
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT']._serialized_start = 85
    _globals['_INCENTIVIZEDACKNOWLEDGEMENT']._serialized_end = 312
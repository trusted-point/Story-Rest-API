"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ibc/applications/transfer/v1/query.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1cgoogle/api/annotations.proto"&\n\x16QueryDenomTraceRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t"X\n\x17QueryDenomTraceResponse\x12=\n\x0bdenom_trace\x18\x01 \x01(\x0b2(.ibc.applications.transfer.v1.DenomTrace"U\n\x17QueryDenomTracesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xa7\x01\n\x18QueryDenomTracesResponse\x12N\n\x0cdenom_traces\x18\x01 \x03(\x0b2(.ibc.applications.transfer.v1.DenomTraceB\x0e\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Traces\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x14\n\x12QueryParamsRequest"K\n\x13QueryParamsResponse\x124\n\x06params\x18\x01 \x01(\x0b2$.ibc.applications.transfer.v1.Params"&\n\x15QueryDenomHashRequest\x12\r\n\x05trace\x18\x01 \x01(\t"&\n\x16QueryDenomHashResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t"@\n\x19QueryEscrowAddressRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t"4\n\x1aQueryEscrowAddressResponse\x12\x16\n\x0eescrow_address\x18\x01 \x01(\t2\xfd\x06\n\x05Query\x12\xac\x01\n\nDenomTrace\x124.ibc.applications.transfer.v1.QueryDenomTraceRequest\x1a5.ibc.applications.transfer.v1.QueryDenomTraceResponse"1\x82\xd3\xe4\x93\x02+\x12)/ibc/apps/transfer/v1/denom_traces/{hash}\x12\xa8\x01\n\x0bDenomTraces\x125.ibc.applications.transfer.v1.QueryDenomTracesRequest\x1a6.ibc.applications.transfer.v1.QueryDenomTracesResponse"*\x82\xd3\xe4\x93\x02$\x12"/ibc/apps/transfer/v1/denom_traces\x12\x93\x01\n\x06Params\x120.ibc.applications.transfer.v1.QueryParamsRequest\x1a1.ibc.applications.transfer.v1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/transfer/v1/params\x12\xaa\x01\n\tDenomHash\x123.ibc.applications.transfer.v1.QueryDenomHashRequest\x1a4.ibc.applications.transfer.v1.QueryDenomHashResponse"2\x82\xd3\xe4\x93\x02,\x12*/ibc/apps/transfer/v1/denom_hashes/{trace}\x12\xd6\x01\n\rEscrowAddress\x127.ibc.applications.transfer.v1.QueryEscrowAddressRequest\x1a8.ibc.applications.transfer.v1.QueryEscrowAddressResponse"R\x82\xd3\xe4\x93\x02L\x12J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_addressB9Z7github.com/cosmos/ibc-go/v4/modules/apps/transfer/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cosmos/ibc-go/v4/modules/apps/transfer/types'
    _globals['_QUERYDENOMTRACESRESPONSE'].fields_by_name['denom_traces']._options = None
    _globals['_QUERYDENOMTRACESRESPONSE'].fields_by_name['denom_traces']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Traces'
    _globals['_QUERY'].methods_by_name['DenomTrace']._options = None
    _globals['_QUERY'].methods_by_name['DenomTrace']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/ibc/apps/transfer/v1/denom_traces/{hash}'
    _globals['_QUERY'].methods_by_name['DenomTraces']._options = None
    _globals['_QUERY'].methods_by_name['DenomTraces']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/ibc/apps/transfer/v1/denom_traces'
    _globals['_QUERY'].methods_by_name['Params']._options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/transfer/v1/params'
    _globals['_QUERY'].methods_by_name['DenomHash']._options = None
    _globals['_QUERY'].methods_by_name['DenomHash']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/ibc/apps/transfer/v1/denom_hashes/{trace}'
    _globals['_QUERY'].methods_by_name['EscrowAddress']._options = None
    _globals['_QUERY'].methods_by_name['EscrowAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02L\x12J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_address'
    _globals['_QUERYDENOMTRACEREQUEST']._serialized_start = 215
    _globals['_QUERYDENOMTRACEREQUEST']._serialized_end = 253
    _globals['_QUERYDENOMTRACERESPONSE']._serialized_start = 255
    _globals['_QUERYDENOMTRACERESPONSE']._serialized_end = 343
    _globals['_QUERYDENOMTRACESREQUEST']._serialized_start = 345
    _globals['_QUERYDENOMTRACESREQUEST']._serialized_end = 430
    _globals['_QUERYDENOMTRACESRESPONSE']._serialized_start = 433
    _globals['_QUERYDENOMTRACESRESPONSE']._serialized_end = 600
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 602
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 622
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 624
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 699
    _globals['_QUERYDENOMHASHREQUEST']._serialized_start = 701
    _globals['_QUERYDENOMHASHREQUEST']._serialized_end = 739
    _globals['_QUERYDENOMHASHRESPONSE']._serialized_start = 741
    _globals['_QUERYDENOMHASHRESPONSE']._serialized_end = 779
    _globals['_QUERYESCROWADDRESSREQUEST']._serialized_start = 781
    _globals['_QUERYESCROWADDRESSREQUEST']._serialized_end = 845
    _globals['_QUERYESCROWADDRESSRESPONSE']._serialized_start = 847
    _globals['_QUERYESCROWADDRESSRESPONSE']._serialized_end = 899
    _globals['_QUERY']._serialized_start = 902
    _globals['_QUERY']._serialized_end = 1795
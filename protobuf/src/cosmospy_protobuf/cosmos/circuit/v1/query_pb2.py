"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....cosmos.circuit.v1 import types_pb2 as cosmos_dot_circuit_dot_v1_dot_types__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcosmos/circuit/v1/query.proto\x12\x11cosmos.circuit.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1dcosmos/circuit/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bcosmos/query/v1/query.proto"&\n\x13QueryAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"E\n\x0fAccountResponse\x122\n\npermission\x18\x01 \x01(\x0b2\x1e.cosmos.circuit.v1.Permissions"R\n\x14QueryAccountsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8f\x01\n\x10AccountsResponse\x12>\n\x08accounts\x18\x01 \x03(\x0b2,.cosmos.circuit.v1.GenesisAccountPermissions\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x1a\n\x18QueryDisabledListRequest"-\n\x14DisabledListResponse\x12\x15\n\rdisabled_list\x18\x01 \x03(\t2\xad\x03\n\x05Query\x12\x89\x01\n\x07Account\x12&.cosmos.circuit.v1.QueryAccountRequest\x1a".cosmos.circuit.v1.AccountResponse"2\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\'\x12%/cosmos/circuit/v1/accounts/{address}\x12\x82\x01\n\x08Accounts\x12\'.cosmos.circuit.v1.QueryAccountsRequest\x1a#.cosmos.circuit.v1.AccountsResponse"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/circuit/v1/accounts\x12\x92\x01\n\x0cDisabledList\x12+.cosmos.circuit.v1.QueryDisabledListRequest\x1a\'.cosmos.circuit.v1.DisabledListResponse",\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/circuit/v1/disable_listB\x1eZ\x1ccosmossdk.io/x/circuit/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.circuit.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1ccosmossdk.io/x/circuit/types'
    _globals['_QUERY'].methods_by_name['Account']._options = None
    _globals['_QUERY'].methods_by_name['Account']._serialized_options = b"\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02'\x12%/cosmos/circuit/v1/accounts/{address}"
    _globals['_QUERY'].methods_by_name['Accounts']._options = None
    _globals['_QUERY'].methods_by_name['Accounts']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/circuit/v1/accounts'
    _globals['_QUERY'].methods_by_name['DisabledList']._options = None
    _globals['_QUERY'].methods_by_name['DisabledList']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/circuit/v1/disable_list'
    _globals['_QUERYACCOUNTREQUEST']._serialized_start = 186
    _globals['_QUERYACCOUNTREQUEST']._serialized_end = 224
    _globals['_ACCOUNTRESPONSE']._serialized_start = 226
    _globals['_ACCOUNTRESPONSE']._serialized_end = 295
    _globals['_QUERYACCOUNTSREQUEST']._serialized_start = 297
    _globals['_QUERYACCOUNTSREQUEST']._serialized_end = 379
    _globals['_ACCOUNTSRESPONSE']._serialized_start = 382
    _globals['_ACCOUNTSRESPONSE']._serialized_end = 525
    _globals['_QUERYDISABLEDLISTREQUEST']._serialized_start = 527
    _globals['_QUERYDISABLEDLISTREQUEST']._serialized_end = 553
    _globals['_DISABLEDLISTRESPONSE']._serialized_start = 555
    _globals['_DISABLEDLISTRESPONSE']._serialized_end = 600
    _globals['_QUERY']._serialized_start = 603
    _globals['_QUERY']._serialized_end = 1032
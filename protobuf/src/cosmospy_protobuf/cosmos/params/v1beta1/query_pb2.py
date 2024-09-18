"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.params.v1beta1 import params_pb2 as cosmos_dot_params_dot_v1beta1_dot_params__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/params/v1beta1/query.proto\x12\x15cosmos.params.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a"cosmos/params/v1beta1/params.proto\x1a\x11amino/amino.proto"3\n\x12QueryParamsRequest\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"S\n\x13QueryParamsResponse\x12<\n\x05param\x18\x01 \x01(\x0b2".cosmos.params.v1beta1.ParamChangeB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x17\n\x15QuerySubspacesRequest"L\n\x16QuerySubspacesResponse\x122\n\tsubspaces\x18\x01 \x03(\x0b2\x1f.cosmos.params.v1beta1.Subspace"*\n\x08Subspace\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t2\xa5\x02\n\x05Query\x12\x86\x01\n\x06Params\x12).cosmos.params.v1beta1.QueryParamsRequest\x1a*.cosmos.params.v1beta1.QueryParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/params\x12\x92\x01\n\tSubspaces\x12,.cosmos.params.v1beta1.QuerySubspacesRequest\x1a-.cosmos.params.v1beta1.QuerySubspacesResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmos/params/v1beta1/subspacesB6Z4github.com/cosmos/cosmos-sdk/x/params/types/proposalb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.params.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['param']._options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['param']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERY'].methods_by_name['Params']._options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/params'
    _globals['_QUERY'].methods_by_name['Subspaces']._options = None
    _globals['_QUERY'].methods_by_name['Subspaces']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmos/params/v1beta1/subspaces'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 167
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 218
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 220
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 303
    _globals['_QUERYSUBSPACESREQUEST']._serialized_start = 305
    _globals['_QUERYSUBSPACESREQUEST']._serialized_end = 328
    _globals['_QUERYSUBSPACESRESPONSE']._serialized_start = 330
    _globals['_QUERYSUBSPACESRESPONSE']._serialized_end = 406
    _globals['_SUBSPACE']._serialized_start = 408
    _globals['_SUBSPACE']._serialized_end = 450
    _globals['_QUERY']._serialized_start = 453
    _globals['_QUERY']._serialized_end = 746
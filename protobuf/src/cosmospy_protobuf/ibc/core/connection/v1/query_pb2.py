"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"ibc/core/connection/v1/query.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/connection/v1/connection.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto"/\n\x16QueryConnectionRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\t"\x9b\x01\n\x17QueryConnectionResponse\x129\n\nconnection\x18\x01 \x01(\x0b2%.ibc.core.connection.v1.ConnectionEnd\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"U\n\x17QueryConnectionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xcc\x01\n\x18QueryConnectionsResponse\x12A\n\x0bconnections\x18\x01 \x03(\x0b2,.ibc.core.connection.v1.IdentifiedConnection\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse\x120\n\x06height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"2\n\x1dQueryClientConnectionsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t"\x81\x01\n\x1eQueryClientConnectionsResponse\x12\x18\n\x10connection_paths\x18\x01 \x03(\t\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"T\n!QueryConnectionClientStateRequest\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id""\xb7\x01\n"QueryConnectionClientStateResponse\x12J\n\x17identified_client_state\x18\x01 \x01(\x0b2).ibc.core.client.v1.IdentifiedClientState\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"\x89\x01\n$QueryConnectionConsensusStateRequest\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04"\xb0\x01\n%QueryConnectionConsensusStateResponse\x12-\n\x0fconsensus_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\r\n\x05proof\x18\x03 \x01(\x0c\x126\n\x0cproof_height\x18\x04 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x002\x8f\x08\n\x05Query\x12\xaa\x01\n\nConnection\x12..ibc.core.connection.v1.QueryConnectionRequest\x1a/.ibc.core.connection.v1.QueryConnectionResponse";\x82\xd3\xe4\x93\x025\x123/ibc/core/connection/v1/connections/{connection_id}\x12\x9d\x01\n\x0bConnections\x12/.ibc.core.connection.v1.QueryConnectionsRequest\x1a0.ibc.core.connection.v1.QueryConnectionsResponse"+\x82\xd3\xe4\x93\x02%\x12#/ibc/core/connection/v1/connections\x12\xc2\x01\n\x11ClientConnections\x125.ibc.core.connection.v1.QueryClientConnectionsRequest\x1a6.ibc.core.connection.v1.QueryClientConnectionsResponse">\x82\xd3\xe4\x93\x028\x126/ibc/core/connection/v1/client_connections/{client_id}\x12\xd8\x01\n\x15ConnectionClientState\x129.ibc.core.connection.v1.QueryConnectionClientStateRequest\x1a:.ibc.core.connection.v1.QueryConnectionClientStateResponse"H\x82\xd3\xe4\x93\x02B\x12@/ibc/core/connection/v1/connections/{connection_id}/client_state\x12\x98\x02\n\x18ConnectionConsensusState\x12<.ibc.core.connection.v1.QueryConnectionConsensusStateRequest\x1a=.ibc.core.connection.v1.QueryConnectionConsensusStateResponse"\x7f\x82\xd3\xe4\x93\x02y\x12w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}B>Z<github.com/cosmos/ibc-go/v4/modules/core/03-connection/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.connection.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/cosmos/ibc-go/v4/modules/core/03-connection/types'
    _globals['_QUERYCONNECTIONRESPONSE'].fields_by_name['proof_height']._options = None
    _globals['_QUERYCONNECTIONRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYCONNECTIONSRESPONSE'].fields_by_name['height']._options = None
    _globals['_QUERYCONNECTIONSRESPONSE'].fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYCLIENTCONNECTIONSRESPONSE'].fields_by_name['proof_height']._options = None
    _globals['_QUERYCLIENTCONNECTIONSRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST'].fields_by_name['connection_id']._options = None
    _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST'].fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE'].fields_by_name['proof_height']._options = None
    _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST'].fields_by_name['connection_id']._options = None
    _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST'].fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._options = None
    _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERY'].methods_by_name['Connection']._options = None
    _globals['_QUERY'].methods_by_name['Connection']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/ibc/core/connection/v1/connections/{connection_id}'
    _globals['_QUERY'].methods_by_name['Connections']._options = None
    _globals['_QUERY'].methods_by_name['Connections']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/ibc/core/connection/v1/connections'
    _globals['_QUERY'].methods_by_name['ClientConnections']._options = None
    _globals['_QUERY'].methods_by_name['ClientConnections']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/ibc/core/connection/v1/client_connections/{client_id}'
    _globals['_QUERY'].methods_by_name['ConnectionClientState']._options = None
    _globals['_QUERY'].methods_by_name['ConnectionClientState']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x12@/ibc/core/connection/v1/connections/{connection_id}/client_state'
    _globals['_QUERY'].methods_by_name['ConnectionConsensusState']._options = None
    _globals['_QUERY'].methods_by_name['ConnectionConsensusState']._serialized_options = b'\x82\xd3\xe4\x93\x02y\x12w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}'
    _globals['_QUERYCONNECTIONREQUEST']._serialized_start = 259
    _globals['_QUERYCONNECTIONREQUEST']._serialized_end = 306
    _globals['_QUERYCONNECTIONRESPONSE']._serialized_start = 309
    _globals['_QUERYCONNECTIONRESPONSE']._serialized_end = 464
    _globals['_QUERYCONNECTIONSREQUEST']._serialized_start = 466
    _globals['_QUERYCONNECTIONSREQUEST']._serialized_end = 551
    _globals['_QUERYCONNECTIONSRESPONSE']._serialized_start = 554
    _globals['_QUERYCONNECTIONSRESPONSE']._serialized_end = 758
    _globals['_QUERYCLIENTCONNECTIONSREQUEST']._serialized_start = 760
    _globals['_QUERYCLIENTCONNECTIONSREQUEST']._serialized_end = 810
    _globals['_QUERYCLIENTCONNECTIONSRESPONSE']._serialized_start = 813
    _globals['_QUERYCLIENTCONNECTIONSRESPONSE']._serialized_end = 942
    _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST']._serialized_start = 944
    _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST']._serialized_end = 1028
    _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE']._serialized_start = 1031
    _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE']._serialized_end = 1214
    _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST']._serialized_start = 1217
    _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST']._serialized_end = 1354
    _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE']._serialized_start = 1357
    _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE']._serialized_end = 1533
    _globals['_QUERY']._serialized_start = 1536
    _globals['_QUERY']._serialized_end = 2575
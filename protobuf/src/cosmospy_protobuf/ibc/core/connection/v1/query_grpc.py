import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import gogoproto
from ..... import cosmos
from ..... import ibc
from ..... import google
import google.protobuf.any_pb2

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Connection(self, stream: 'grpclib.server.Stream[ibc.core.connection.v1.query_pb2.QueryConnectionRequest, ibc.core.connection.v1.query_pb2.QueryConnectionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Connections(self, stream: 'grpclib.server.Stream[ibc.core.connection.v1.query_pb2.QueryConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryConnectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientConnections(self, stream: 'grpclib.server.Stream[ibc.core.connection.v1.query_pb2.QueryClientConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryClientConnectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConnectionClientState(self, stream: 'grpclib.server.Stream[ibc.core.connection.v1.query_pb2.QueryConnectionClientStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionClientStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConnectionConsensusState(self, stream: 'grpclib.server.Stream[ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.core.connection.v1.Query/Connection': grpclib.const.Handler(self.Connection, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.connection.v1.query_pb2.QueryConnectionRequest, ibc.core.connection.v1.query_pb2.QueryConnectionResponse), '/ibc.core.connection.v1.Query/Connections': grpclib.const.Handler(self.Connections, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.connection.v1.query_pb2.QueryConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryConnectionsResponse), '/ibc.core.connection.v1.Query/ClientConnections': grpclib.const.Handler(self.ClientConnections, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.connection.v1.query_pb2.QueryClientConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryClientConnectionsResponse), '/ibc.core.connection.v1.Query/ConnectionClientState': grpclib.const.Handler(self.ConnectionClientState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.connection.v1.query_pb2.QueryConnectionClientStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionClientStateResponse), '/ibc.core.connection.v1.Query/ConnectionConsensusState': grpclib.const.Handler(self.ConnectionConsensusState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Connection = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.connection.v1.Query/Connection', ibc.core.connection.v1.query_pb2.QueryConnectionRequest, ibc.core.connection.v1.query_pb2.QueryConnectionResponse)
        self.Connections = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.connection.v1.Query/Connections', ibc.core.connection.v1.query_pb2.QueryConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryConnectionsResponse)
        self.ClientConnections = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.connection.v1.Query/ClientConnections', ibc.core.connection.v1.query_pb2.QueryClientConnectionsRequest, ibc.core.connection.v1.query_pb2.QueryClientConnectionsResponse)
        self.ConnectionClientState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.connection.v1.Query/ConnectionClientState', ibc.core.connection.v1.query_pb2.QueryConnectionClientStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionClientStateResponse)
        self.ConnectionConsensusState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.connection.v1.Query/ConnectionConsensusState', ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateRequest, ibc.core.connection.v1.query_pb2.QueryConnectionConsensusStateResponse)
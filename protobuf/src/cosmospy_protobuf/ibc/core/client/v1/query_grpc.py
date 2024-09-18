import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import cosmos
from ..... import ibc
import google.protobuf.any_pb2
from ..... import google
from ..... import gogoproto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def ClientState(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryClientStateRequest, ibc.core.client.v1.query_pb2.QueryClientStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientStates(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryClientStatesRequest, ibc.core.client.v1.query_pb2.QueryClientStatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConsensusState(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConsensusStates(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryConsensusStatesRequest, ibc.core.client.v1.query_pb2.QueryConsensusStatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConsensusStateHeights(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientStatus(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryClientStatusRequest, ibc.core.client.v1.query_pb2.QueryClientStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientParams(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryClientParamsRequest, ibc.core.client.v1.query_pb2.QueryClientParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpgradedClientState(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryUpgradedClientStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedClientStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpgradedConsensusState(self, stream: 'grpclib.server.Stream[ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.core.client.v1.Query/ClientState': grpclib.const.Handler(self.ClientState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryClientStateRequest, ibc.core.client.v1.query_pb2.QueryClientStateResponse), '/ibc.core.client.v1.Query/ClientStates': grpclib.const.Handler(self.ClientStates, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryClientStatesRequest, ibc.core.client.v1.query_pb2.QueryClientStatesResponse), '/ibc.core.client.v1.Query/ConsensusState': grpclib.const.Handler(self.ConsensusState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateResponse), '/ibc.core.client.v1.Query/ConsensusStates': grpclib.const.Handler(self.ConsensusStates, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryConsensusStatesRequest, ibc.core.client.v1.query_pb2.QueryConsensusStatesResponse), '/ibc.core.client.v1.Query/ConsensusStateHeights': grpclib.const.Handler(self.ConsensusStateHeights, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsResponse), '/ibc.core.client.v1.Query/ClientStatus': grpclib.const.Handler(self.ClientStatus, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryClientStatusRequest, ibc.core.client.v1.query_pb2.QueryClientStatusResponse), '/ibc.core.client.v1.Query/ClientParams': grpclib.const.Handler(self.ClientParams, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryClientParamsRequest, ibc.core.client.v1.query_pb2.QueryClientParamsResponse), '/ibc.core.client.v1.Query/UpgradedClientState': grpclib.const.Handler(self.UpgradedClientState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryUpgradedClientStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedClientStateResponse), '/ibc.core.client.v1.Query/UpgradedConsensusState': grpclib.const.Handler(self.UpgradedConsensusState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ClientState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ClientState', ibc.core.client.v1.query_pb2.QueryClientStateRequest, ibc.core.client.v1.query_pb2.QueryClientStateResponse)
        self.ClientStates = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ClientStates', ibc.core.client.v1.query_pb2.QueryClientStatesRequest, ibc.core.client.v1.query_pb2.QueryClientStatesResponse)
        self.ConsensusState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ConsensusState', ibc.core.client.v1.query_pb2.QueryConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateResponse)
        self.ConsensusStates = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ConsensusStates', ibc.core.client.v1.query_pb2.QueryConsensusStatesRequest, ibc.core.client.v1.query_pb2.QueryConsensusStatesResponse)
        self.ConsensusStateHeights = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ConsensusStateHeights', ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsRequest, ibc.core.client.v1.query_pb2.QueryConsensusStateHeightsResponse)
        self.ClientStatus = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ClientStatus', ibc.core.client.v1.query_pb2.QueryClientStatusRequest, ibc.core.client.v1.query_pb2.QueryClientStatusResponse)
        self.ClientParams = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/ClientParams', ibc.core.client.v1.query_pb2.QueryClientParamsRequest, ibc.core.client.v1.query_pb2.QueryClientParamsResponse)
        self.UpgradedClientState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/UpgradedClientState', ibc.core.client.v1.query_pb2.QueryUpgradedClientStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedClientStateResponse)
        self.UpgradedConsensusState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.client.v1.Query/UpgradedConsensusState', ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateRequest, ibc.core.client.v1.query_pb2.QueryUpgradedConsensusStateResponse)
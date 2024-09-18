import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import google
from .... import cosmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def CurrentPlan(self, stream: 'grpclib.server.Stream[cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppliedPlan(self, stream: 'grpclib.server.Stream[cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpgradedConsensusState(self, stream: 'grpclib.server.Stream[cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateRequest, cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ModuleVersions(self, stream: 'grpclib.server.Stream[cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsRequest, cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Authority(self, stream: 'grpclib.server.Stream[cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.upgrade.v1beta1.Query/CurrentPlan': grpclib.const.Handler(self.CurrentPlan, grpclib.const.Cardinality.UNARY_UNARY, cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanResponse), '/cosmos.upgrade.v1beta1.Query/AppliedPlan': grpclib.const.Handler(self.AppliedPlan, grpclib.const.Cardinality.UNARY_UNARY, cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanResponse), '/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState': grpclib.const.Handler(self.UpgradedConsensusState, grpclib.const.Cardinality.UNARY_UNARY, cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateRequest, cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateResponse), '/cosmos.upgrade.v1beta1.Query/ModuleVersions': grpclib.const.Handler(self.ModuleVersions, grpclib.const.Cardinality.UNARY_UNARY, cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsRequest, cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsResponse), '/cosmos.upgrade.v1beta1.Query/Authority': grpclib.const.Handler(self.Authority, grpclib.const.Cardinality.UNARY_UNARY, cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CurrentPlan = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.upgrade.v1beta1.Query/CurrentPlan', cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryCurrentPlanResponse)
        self.AppliedPlan = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.upgrade.v1beta1.Query/AppliedPlan', cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAppliedPlanResponse)
        self.UpgradedConsensusState = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState', cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateRequest, cosmos.upgrade.v1beta1.query_pb2.QueryUpgradedConsensusStateResponse)
        self.ModuleVersions = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.upgrade.v1beta1.Query/ModuleVersions', cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsRequest, cosmos.upgrade.v1beta1.query_pb2.QueryModuleVersionsResponse)
        self.Authority = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.upgrade.v1beta1.Query/Authority', cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityRequest, cosmos.upgrade.v1beta1.query_pb2.QueryAuthorityResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import gogoproto
from .... import google
from .... import cosmos_proto
from .... import amino

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryParamsRequest, cosmos.distribution.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorDistributionInfo(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorOutstandingRewards(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorCommission(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorSlashes(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegationRewards(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegationTotalRewards(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorValidators(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorWithdrawAddress(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CommunityPool(self, stream: 'grpclib.server.Stream[cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolRequest, cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.distribution.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryParamsRequest, cosmos.distribution.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.distribution.v1beta1.Query/ValidatorDistributionInfo': grpclib.const.Handler(self.ValidatorDistributionInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoResponse), '/cosmos.distribution.v1beta1.Query/ValidatorOutstandingRewards': grpclib.const.Handler(self.ValidatorOutstandingRewards, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsResponse), '/cosmos.distribution.v1beta1.Query/ValidatorCommission': grpclib.const.Handler(self.ValidatorCommission, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionResponse), '/cosmos.distribution.v1beta1.Query/ValidatorSlashes': grpclib.const.Handler(self.ValidatorSlashes, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesResponse), '/cosmos.distribution.v1beta1.Query/DelegationRewards': grpclib.const.Handler(self.DelegationRewards, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsResponse), '/cosmos.distribution.v1beta1.Query/DelegationTotalRewards': grpclib.const.Handler(self.DelegationTotalRewards, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsResponse), '/cosmos.distribution.v1beta1.Query/DelegatorValidators': grpclib.const.Handler(self.DelegatorValidators, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsResponse), '/cosmos.distribution.v1beta1.Query/DelegatorWithdrawAddress': grpclib.const.Handler(self.DelegatorWithdrawAddress, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressResponse), '/cosmos.distribution.v1beta1.Query/CommunityPool': grpclib.const.Handler(self.CommunityPool, grpclib.const.Cardinality.UNARY_UNARY, cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolRequest, cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/Params', cosmos.distribution.v1beta1.query_pb2.QueryParamsRequest, cosmos.distribution.v1beta1.query_pb2.QueryParamsResponse)
        self.ValidatorDistributionInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/ValidatorDistributionInfo', cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorDistributionInfoResponse)
        self.ValidatorOutstandingRewards = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/ValidatorOutstandingRewards', cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorOutstandingRewardsResponse)
        self.ValidatorCommission = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/ValidatorCommission', cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorCommissionResponse)
        self.ValidatorSlashes = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/ValidatorSlashes', cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesRequest, cosmos.distribution.v1beta1.query_pb2.QueryValidatorSlashesResponse)
        self.DelegationRewards = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/DelegationRewards', cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationRewardsResponse)
        self.DelegationTotalRewards = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/DelegationTotalRewards', cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegationTotalRewardsResponse)
        self.DelegatorValidators = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/DelegatorValidators', cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorValidatorsResponse)
        self.DelegatorWithdrawAddress = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/DelegatorWithdrawAddress', cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressRequest, cosmos.distribution.v1beta1.query_pb2.QueryDelegatorWithdrawAddressResponse)
        self.CommunityPool = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.distribution.v1beta1.Query/CommunityPool', cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolRequest, cosmos.distribution.v1beta1.query_pb2.QueryCommunityPoolResponse)
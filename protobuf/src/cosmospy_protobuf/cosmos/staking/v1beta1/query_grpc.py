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
    async def Validators(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Validator(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorDelegations(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorUnbondingDelegations(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Delegation(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UnbondingDelegation(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorDelegations(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorUnbondingDelegations(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Redelegations(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryRedelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryRedelegationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorValidators(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DelegatorValidator(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def HistoricalInfo(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoRequest, cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Pool(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryPoolRequest, cosmos.staking.v1beta1.query_pb2.QueryPoolResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.staking.v1beta1.query_pb2.QueryParamsRequest, cosmos.staking.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.staking.v1beta1.Query/Validators': grpclib.const.Handler(self.Validators, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorsResponse), '/cosmos.staking.v1beta1.Query/Validator': grpclib.const.Handler(self.Validator, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorResponse), '/cosmos.staking.v1beta1.Query/ValidatorDelegations': grpclib.const.Handler(self.ValidatorDelegations, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsResponse), '/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations': grpclib.const.Handler(self.ValidatorUnbondingDelegations, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsResponse), '/cosmos.staking.v1beta1.Query/Delegation': grpclib.const.Handler(self.Delegation, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegationResponse), '/cosmos.staking.v1beta1.Query/UnbondingDelegation': grpclib.const.Handler(self.UnbondingDelegation, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationResponse), '/cosmos.staking.v1beta1.Query/DelegatorDelegations': grpclib.const.Handler(self.DelegatorDelegations, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsResponse), '/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations': grpclib.const.Handler(self.DelegatorUnbondingDelegations, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsResponse), '/cosmos.staking.v1beta1.Query/Redelegations': grpclib.const.Handler(self.Redelegations, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryRedelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryRedelegationsResponse), '/cosmos.staking.v1beta1.Query/DelegatorValidators': grpclib.const.Handler(self.DelegatorValidators, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsResponse), '/cosmos.staking.v1beta1.Query/DelegatorValidator': grpclib.const.Handler(self.DelegatorValidator, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorResponse), '/cosmos.staking.v1beta1.Query/HistoricalInfo': grpclib.const.Handler(self.HistoricalInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoRequest, cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoResponse), '/cosmos.staking.v1beta1.Query/Pool': grpclib.const.Handler(self.Pool, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryPoolRequest, cosmos.staking.v1beta1.query_pb2.QueryPoolResponse), '/cosmos.staking.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.staking.v1beta1.query_pb2.QueryParamsRequest, cosmos.staking.v1beta1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Validators = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Validators', cosmos.staking.v1beta1.query_pb2.QueryValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorsResponse)
        self.Validator = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Validator', cosmos.staking.v1beta1.query_pb2.QueryValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorResponse)
        self.ValidatorDelegations = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/ValidatorDelegations', cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorDelegationsResponse)
        self.ValidatorUnbondingDelegations = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations', cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryValidatorUnbondingDelegationsResponse)
        self.Delegation = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Delegation', cosmos.staking.v1beta1.query_pb2.QueryDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegationResponse)
        self.UnbondingDelegation = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/UnbondingDelegation', cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationRequest, cosmos.staking.v1beta1.query_pb2.QueryUnbondingDelegationResponse)
        self.DelegatorDelegations = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/DelegatorDelegations', cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorDelegationsResponse)
        self.DelegatorUnbondingDelegations = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations', cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorUnbondingDelegationsResponse)
        self.Redelegations = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Redelegations', cosmos.staking.v1beta1.query_pb2.QueryRedelegationsRequest, cosmos.staking.v1beta1.query_pb2.QueryRedelegationsResponse)
        self.DelegatorValidators = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/DelegatorValidators', cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorsResponse)
        self.DelegatorValidator = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/DelegatorValidator', cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorRequest, cosmos.staking.v1beta1.query_pb2.QueryDelegatorValidatorResponse)
        self.HistoricalInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/HistoricalInfo', cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoRequest, cosmos.staking.v1beta1.query_pb2.QueryHistoricalInfoResponse)
        self.Pool = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Pool', cosmos.staking.v1beta1.query_pb2.QueryPoolRequest, cosmos.staking.v1beta1.query_pb2.QueryPoolResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.staking.v1beta1.Query/Params', cosmos.staking.v1beta1.query_pb2.QueryParamsRequest, cosmos.staking.v1beta1.query_pb2.QueryParamsResponse)
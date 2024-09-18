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
    async def Balance(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryBalanceRequest, cosmos.bank.v1beta1.query_pb2.QueryBalanceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AllBalances(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryAllBalancesRequest, cosmos.bank.v1beta1.query_pb2.QueryAllBalancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SpendableBalances(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SpendableBalanceByDenom(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TotalSupply(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyRequest, cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SupplyOf(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QuerySupplyOfRequest, cosmos.bank.v1beta1.query_pb2.QuerySupplyOfResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryParamsRequest, cosmos.bank.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomMetadata(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomMetadataByQueryString(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomsMetadata(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomOwners(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomOwnersByQuery(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SendEnabled(self, stream: 'grpclib.server.Stream[cosmos.bank.v1beta1.query_pb2.QuerySendEnabledRequest, cosmos.bank.v1beta1.query_pb2.QuerySendEnabledResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.bank.v1beta1.Query/Balance': grpclib.const.Handler(self.Balance, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryBalanceRequest, cosmos.bank.v1beta1.query_pb2.QueryBalanceResponse), '/cosmos.bank.v1beta1.Query/AllBalances': grpclib.const.Handler(self.AllBalances, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryAllBalancesRequest, cosmos.bank.v1beta1.query_pb2.QueryAllBalancesResponse), '/cosmos.bank.v1beta1.Query/SpendableBalances': grpclib.const.Handler(self.SpendableBalances, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesResponse), '/cosmos.bank.v1beta1.Query/SpendableBalanceByDenom': grpclib.const.Handler(self.SpendableBalanceByDenom, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomResponse), '/cosmos.bank.v1beta1.Query/TotalSupply': grpclib.const.Handler(self.TotalSupply, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyRequest, cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyResponse), '/cosmos.bank.v1beta1.Query/SupplyOf': grpclib.const.Handler(self.SupplyOf, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QuerySupplyOfRequest, cosmos.bank.v1beta1.query_pb2.QuerySupplyOfResponse), '/cosmos.bank.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryParamsRequest, cosmos.bank.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.bank.v1beta1.Query/DenomMetadata': grpclib.const.Handler(self.DenomMetadata, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataResponse), '/cosmos.bank.v1beta1.Query/DenomMetadataByQueryString': grpclib.const.Handler(self.DenomMetadataByQueryString, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringResponse), '/cosmos.bank.v1beta1.Query/DenomsMetadata': grpclib.const.Handler(self.DenomsMetadata, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataResponse), '/cosmos.bank.v1beta1.Query/DenomOwners': grpclib.const.Handler(self.DenomOwners, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersResponse), '/cosmos.bank.v1beta1.Query/DenomOwnersByQuery': grpclib.const.Handler(self.DenomOwnersByQuery, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryResponse), '/cosmos.bank.v1beta1.Query/SendEnabled': grpclib.const.Handler(self.SendEnabled, grpclib.const.Cardinality.UNARY_UNARY, cosmos.bank.v1beta1.query_pb2.QuerySendEnabledRequest, cosmos.bank.v1beta1.query_pb2.QuerySendEnabledResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Balance = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/Balance', cosmos.bank.v1beta1.query_pb2.QueryBalanceRequest, cosmos.bank.v1beta1.query_pb2.QueryBalanceResponse)
        self.AllBalances = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/AllBalances', cosmos.bank.v1beta1.query_pb2.QueryAllBalancesRequest, cosmos.bank.v1beta1.query_pb2.QueryAllBalancesResponse)
        self.SpendableBalances = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/SpendableBalances', cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalancesResponse)
        self.SpendableBalanceByDenom = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/SpendableBalanceByDenom', cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomRequest, cosmos.bank.v1beta1.query_pb2.QuerySpendableBalanceByDenomResponse)
        self.TotalSupply = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/TotalSupply', cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyRequest, cosmos.bank.v1beta1.query_pb2.QueryTotalSupplyResponse)
        self.SupplyOf = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/SupplyOf', cosmos.bank.v1beta1.query_pb2.QuerySupplyOfRequest, cosmos.bank.v1beta1.query_pb2.QuerySupplyOfResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/Params', cosmos.bank.v1beta1.query_pb2.QueryParamsRequest, cosmos.bank.v1beta1.query_pb2.QueryParamsResponse)
        self.DenomMetadata = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/DenomMetadata', cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataResponse)
        self.DenomMetadataByQueryString = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/DenomMetadataByQueryString', cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomMetadataByQueryStringResponse)
        self.DenomsMetadata = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/DenomsMetadata', cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomsMetadataResponse)
        self.DenomOwners = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/DenomOwners', cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersResponse)
        self.DenomOwnersByQuery = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/DenomOwnersByQuery', cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryRequest, cosmos.bank.v1beta1.query_pb2.QueryDenomOwnersByQueryResponse)
        self.SendEnabled = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.bank.v1beta1.Query/SendEnabled', cosmos.bank.v1beta1.query_pb2.QuerySendEnabledRequest, cosmos.bank.v1beta1.query_pb2.QuerySendEnabledResponse)
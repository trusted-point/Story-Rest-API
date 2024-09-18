import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import google
from .... import cosmos_proto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Allowance(self, stream: 'grpclib.server.Stream[cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Allowances(self, stream: 'grpclib.server.Stream[cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AllowancesByGranter(self, stream: 'grpclib.server.Stream[cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.feegrant.v1beta1.Query/Allowance': grpclib.const.Handler(self.Allowance, grpclib.const.Cardinality.UNARY_UNARY, cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceResponse), '/cosmos.feegrant.v1beta1.Query/Allowances': grpclib.const.Handler(self.Allowances, grpclib.const.Cardinality.UNARY_UNARY, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesResponse), '/cosmos.feegrant.v1beta1.Query/AllowancesByGranter': grpclib.const.Handler(self.AllowancesByGranter, grpclib.const.Cardinality.UNARY_UNARY, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Allowance = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.feegrant.v1beta1.Query/Allowance', cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceResponse)
        self.Allowances = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.feegrant.v1beta1.Query/Allowances', cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesResponse)
        self.AllowancesByGranter = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.feegrant.v1beta1.Query/AllowancesByGranter', cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterRequest, cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesByGranterResponse)
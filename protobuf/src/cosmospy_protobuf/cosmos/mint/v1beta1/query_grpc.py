import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import cosmos
from .... import amino
from .... import cosmos_proto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.mint.v1beta1.query_pb2.QueryParamsRequest, cosmos.mint.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Inflation(self, stream: 'grpclib.server.Stream[cosmos.mint.v1beta1.query_pb2.QueryInflationRequest, cosmos.mint.v1beta1.query_pb2.QueryInflationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnnualProvisions(self, stream: 'grpclib.server.Stream[cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsRequest, cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.mint.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.mint.v1beta1.query_pb2.QueryParamsRequest, cosmos.mint.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.mint.v1beta1.Query/Inflation': grpclib.const.Handler(self.Inflation, grpclib.const.Cardinality.UNARY_UNARY, cosmos.mint.v1beta1.query_pb2.QueryInflationRequest, cosmos.mint.v1beta1.query_pb2.QueryInflationResponse), '/cosmos.mint.v1beta1.Query/AnnualProvisions': grpclib.const.Handler(self.AnnualProvisions, grpclib.const.Cardinality.UNARY_UNARY, cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsRequest, cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.mint.v1beta1.Query/Params', cosmos.mint.v1beta1.query_pb2.QueryParamsRequest, cosmos.mint.v1beta1.query_pb2.QueryParamsResponse)
        self.Inflation = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.mint.v1beta1.Query/Inflation', cosmos.mint.v1beta1.query_pb2.QueryInflationRequest, cosmos.mint.v1beta1.query_pb2.QueryInflationResponse)
        self.AnnualProvisions = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.mint.v1beta1.Query/AnnualProvisions', cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsRequest, cosmos.mint.v1beta1.query_pb2.QueryAnnualProvisionsResponse)
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
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.slashing.v1beta1.query_pb2.QueryParamsRequest, cosmos.slashing.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SigningInfo(self, stream: 'grpclib.server.Stream[cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SigningInfos(self, stream: 'grpclib.server.Stream[cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.slashing.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.slashing.v1beta1.query_pb2.QueryParamsRequest, cosmos.slashing.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.slashing.v1beta1.Query/SigningInfo': grpclib.const.Handler(self.SigningInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoResponse), '/cosmos.slashing.v1beta1.Query/SigningInfos': grpclib.const.Handler(self.SigningInfos, grpclib.const.Cardinality.UNARY_UNARY, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.slashing.v1beta1.Query/Params', cosmos.slashing.v1beta1.query_pb2.QueryParamsRequest, cosmos.slashing.v1beta1.query_pb2.QueryParamsResponse)
        self.SigningInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.slashing.v1beta1.Query/SigningInfo', cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfoResponse)
        self.SigningInfos = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.slashing.v1beta1.Query/SigningInfos', cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosRequest, cosmos.slashing.v1beta1.query_pb2.QuerySigningInfosResponse)
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

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.params.v1beta1.query_pb2.QueryParamsRequest, cosmos.params.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Subspaces(self, stream: 'grpclib.server.Stream[cosmos.params.v1beta1.query_pb2.QuerySubspacesRequest, cosmos.params.v1beta1.query_pb2.QuerySubspacesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.params.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.params.v1beta1.query_pb2.QueryParamsRequest, cosmos.params.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.params.v1beta1.Query/Subspaces': grpclib.const.Handler(self.Subspaces, grpclib.const.Cardinality.UNARY_UNARY, cosmos.params.v1beta1.query_pb2.QuerySubspacesRequest, cosmos.params.v1beta1.query_pb2.QuerySubspacesResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.params.v1beta1.Query/Params', cosmos.params.v1beta1.query_pb2.QueryParamsRequest, cosmos.params.v1beta1.query_pb2.QueryParamsResponse)
        self.Subspaces = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.params.v1beta1.Query/Subspaces', cosmos.params.v1beta1.query_pb2.QuerySubspacesRequest, cosmos.params.v1beta1.query_pb2.QuerySubspacesResponse)
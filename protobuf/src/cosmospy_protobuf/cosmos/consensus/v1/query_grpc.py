import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import google
from .... import tendermint
from .... import cosmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.consensus.v1.query_pb2.QueryParamsRequest, cosmos.consensus.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.consensus.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.consensus.v1.query_pb2.QueryParamsRequest, cosmos.consensus.v1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.consensus.v1.Query/Params', cosmos.consensus.v1.query_pb2.QueryParamsRequest, cosmos.consensus.v1.query_pb2.QueryParamsResponse)
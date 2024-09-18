import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def AppOptions(self, stream: 'grpclib.server.Stream[cosmos.autocli.v1.query_pb2.AppOptionsRequest, cosmos.autocli.v1.query_pb2.AppOptionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.autocli.v1.Query/AppOptions': grpclib.const.Handler(self.AppOptions, grpclib.const.Cardinality.UNARY_UNARY, cosmos.autocli.v1.query_pb2.AppOptionsRequest, cosmos.autocli.v1.query_pb2.AppOptionsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AppOptions = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.autocli.v1.Query/AppOptions', cosmos.autocli.v1.query_pb2.AppOptionsRequest, cosmos.autocli.v1.query_pb2.AppOptionsResponse)
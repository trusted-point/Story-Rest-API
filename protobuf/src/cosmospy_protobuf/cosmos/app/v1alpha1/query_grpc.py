import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[cosmos.app.v1alpha1.query_pb2.QueryConfigRequest, cosmos.app.v1alpha1.query_pb2.QueryConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.app.v1alpha1.Query/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, cosmos.app.v1alpha1.query_pb2.QueryConfigRequest, cosmos.app.v1alpha1.query_pb2.QueryConfigResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.app.v1alpha1.Query/Config', cosmos.app.v1alpha1.query_pb2.QueryConfigRequest, cosmos.app.v1alpha1.query_pb2.QueryConfigResponse)
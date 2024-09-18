import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import google
import google.protobuf.timestamp_pb2
from ..... import gogoproto
from ..... import cosmos

class ServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[cosmos.base.node.v1beta1.query_pb2.ConfigRequest, cosmos.base.node.v1beta1.query_pb2.ConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Status(self, stream: 'grpclib.server.Stream[cosmos.base.node.v1beta1.query_pb2.StatusRequest, cosmos.base.node.v1beta1.query_pb2.StatusResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.base.node.v1beta1.Service/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.node.v1beta1.query_pb2.ConfigRequest, cosmos.base.node.v1beta1.query_pb2.ConfigResponse), '/cosmos.base.node.v1beta1.Service/Status': grpclib.const.Handler(self.Status, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.node.v1beta1.query_pb2.StatusRequest, cosmos.base.node.v1beta1.query_pb2.StatusResponse)}

class ServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.node.v1beta1.Service/Config', cosmos.base.node.v1beta1.query_pb2.ConfigRequest, cosmos.base.node.v1beta1.query_pb2.ConfigResponse)
        self.Status = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.node.v1beta1.Service/Status', cosmos.base.node.v1beta1.query_pb2.StatusRequest, cosmos.base.node.v1beta1.query_pb2.StatusResponse)
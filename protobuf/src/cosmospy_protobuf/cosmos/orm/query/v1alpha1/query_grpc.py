import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
import google.protobuf.duration_pb2
import google.protobuf.any_pb2
from ..... import cosmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Get(self, stream: 'grpclib.server.Stream[cosmos.orm.query.v1alpha1.query_pb2.GetRequest, cosmos.orm.query.v1alpha1.query_pb2.GetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def List(self, stream: 'grpclib.server.Stream[cosmos.orm.query.v1alpha1.query_pb2.ListRequest, cosmos.orm.query.v1alpha1.query_pb2.ListResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.orm.query.v1alpha1.Query/Get': grpclib.const.Handler(self.Get, grpclib.const.Cardinality.UNARY_UNARY, cosmos.orm.query.v1alpha1.query_pb2.GetRequest, cosmos.orm.query.v1alpha1.query_pb2.GetResponse), '/cosmos.orm.query.v1alpha1.Query/List': grpclib.const.Handler(self.List, grpclib.const.Cardinality.UNARY_UNARY, cosmos.orm.query.v1alpha1.query_pb2.ListRequest, cosmos.orm.query.v1alpha1.query_pb2.ListResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Get = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.orm.query.v1alpha1.Query/Get', cosmos.orm.query.v1alpha1.query_pb2.GetRequest, cosmos.orm.query.v1alpha1.query_pb2.GetResponse)
        self.List = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.orm.query.v1alpha1.Query/List', cosmos.orm.query.v1alpha1.query_pb2.ListRequest, cosmos.orm.query.v1alpha1.query_pb2.ListResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import google
from .... import cosmos
from .... import cosmos_proto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Grants(self, stream: 'grpclib.server.Stream[cosmos.authz.v1beta1.query_pb2.QueryGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGrantsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GranterGrants(self, stream: 'grpclib.server.Stream[cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GranteeGrants(self, stream: 'grpclib.server.Stream[cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.authz.v1beta1.Query/Grants': grpclib.const.Handler(self.Grants, grpclib.const.Cardinality.UNARY_UNARY, cosmos.authz.v1beta1.query_pb2.QueryGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGrantsResponse), '/cosmos.authz.v1beta1.Query/GranterGrants': grpclib.const.Handler(self.GranterGrants, grpclib.const.Cardinality.UNARY_UNARY, cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsResponse), '/cosmos.authz.v1beta1.Query/GranteeGrants': grpclib.const.Handler(self.GranteeGrants, grpclib.const.Cardinality.UNARY_UNARY, cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Grants = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.authz.v1beta1.Query/Grants', cosmos.authz.v1beta1.query_pb2.QueryGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGrantsResponse)
        self.GranterGrants = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.authz.v1beta1.Query/GranterGrants', cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranterGrantsResponse)
        self.GranteeGrants = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.authz.v1beta1.Query/GranteeGrants', cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsRequest, cosmos.authz.v1beta1.query_pb2.QueryGranteeGrantsResponse)
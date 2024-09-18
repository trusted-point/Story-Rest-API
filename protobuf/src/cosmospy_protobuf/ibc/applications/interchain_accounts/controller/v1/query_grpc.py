import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ...... import ibc
from ...... import gogoproto
from ...... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def InterchainAccount(self, stream: 'grpclib.server.Stream[ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.applications.interchain_accounts.controller.v1.Query/InterchainAccount': grpclib.const.Handler(self.InterchainAccount, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountResponse), '/ibc.applications.interchain_accounts.controller.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.InterchainAccount = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.interchain_accounts.controller.v1.Query/InterchainAccount', ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryInterchainAccountResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.interchain_accounts.controller.v1.Query/Params', ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsRequest, ibc.applications.interchain_accounts.controller.v1.query_pb2.QueryParamsResponse)
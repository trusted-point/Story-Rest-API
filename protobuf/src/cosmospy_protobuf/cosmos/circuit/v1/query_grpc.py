import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Account(self, stream: 'grpclib.server.Stream[cosmos.circuit.v1.query_pb2.QueryAccountRequest, cosmos.circuit.v1.query_pb2.AccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Accounts(self, stream: 'grpclib.server.Stream[cosmos.circuit.v1.query_pb2.QueryAccountsRequest, cosmos.circuit.v1.query_pb2.AccountsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DisabledList(self, stream: 'grpclib.server.Stream[cosmos.circuit.v1.query_pb2.QueryDisabledListRequest, cosmos.circuit.v1.query_pb2.DisabledListResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.circuit.v1.Query/Account': grpclib.const.Handler(self.Account, grpclib.const.Cardinality.UNARY_UNARY, cosmos.circuit.v1.query_pb2.QueryAccountRequest, cosmos.circuit.v1.query_pb2.AccountResponse), '/cosmos.circuit.v1.Query/Accounts': grpclib.const.Handler(self.Accounts, grpclib.const.Cardinality.UNARY_UNARY, cosmos.circuit.v1.query_pb2.QueryAccountsRequest, cosmos.circuit.v1.query_pb2.AccountsResponse), '/cosmos.circuit.v1.Query/DisabledList': grpclib.const.Handler(self.DisabledList, grpclib.const.Cardinality.UNARY_UNARY, cosmos.circuit.v1.query_pb2.QueryDisabledListRequest, cosmos.circuit.v1.query_pb2.DisabledListResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Account = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.circuit.v1.Query/Account', cosmos.circuit.v1.query_pb2.QueryAccountRequest, cosmos.circuit.v1.query_pb2.AccountResponse)
        self.Accounts = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.circuit.v1.Query/Accounts', cosmos.circuit.v1.query_pb2.QueryAccountsRequest, cosmos.circuit.v1.query_pb2.AccountsResponse)
        self.DisabledList = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.circuit.v1.Query/DisabledList', cosmos.circuit.v1.query_pb2.QueryDisabledListRequest, cosmos.circuit.v1.query_pb2.DisabledListResponse)
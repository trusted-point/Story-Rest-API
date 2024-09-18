import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import gogoproto
import google.protobuf.any_pb2
from .... import google
from .... import cosmos_proto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Accounts(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Account(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryAccountRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AccountAddressByID(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryParamsRequest, cosmos.auth.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ModuleAccounts(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ModuleAccountByName(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Bech32Prefix(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.Bech32PrefixRequest, cosmos.auth.v1beta1.query_pb2.Bech32PrefixResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddressBytesToString(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.AddressBytesToStringRequest, cosmos.auth.v1beta1.query_pb2.AddressBytesToStringResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddressStringToBytes(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.AddressStringToBytesRequest, cosmos.auth.v1beta1.query_pb2.AddressStringToBytesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AccountInfo(self, stream: 'grpclib.server.Stream[cosmos.auth.v1beta1.query_pb2.QueryAccountInfoRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountInfoResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.auth.v1beta1.Query/Accounts': grpclib.const.Handler(self.Accounts, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountsResponse), '/cosmos.auth.v1beta1.Query/Account': grpclib.const.Handler(self.Account, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryAccountRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountResponse), '/cosmos.auth.v1beta1.Query/AccountAddressByID': grpclib.const.Handler(self.AccountAddressByID, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDResponse), '/cosmos.auth.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryParamsRequest, cosmos.auth.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.auth.v1beta1.Query/ModuleAccounts': grpclib.const.Handler(self.ModuleAccounts, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsResponse), '/cosmos.auth.v1beta1.Query/ModuleAccountByName': grpclib.const.Handler(self.ModuleAccountByName, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameResponse), '/cosmos.auth.v1beta1.Query/Bech32Prefix': grpclib.const.Handler(self.Bech32Prefix, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.Bech32PrefixRequest, cosmos.auth.v1beta1.query_pb2.Bech32PrefixResponse), '/cosmos.auth.v1beta1.Query/AddressBytesToString': grpclib.const.Handler(self.AddressBytesToString, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.AddressBytesToStringRequest, cosmos.auth.v1beta1.query_pb2.AddressBytesToStringResponse), '/cosmos.auth.v1beta1.Query/AddressStringToBytes': grpclib.const.Handler(self.AddressStringToBytes, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.AddressStringToBytesRequest, cosmos.auth.v1beta1.query_pb2.AddressStringToBytesResponse), '/cosmos.auth.v1beta1.Query/AccountInfo': grpclib.const.Handler(self.AccountInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.auth.v1beta1.query_pb2.QueryAccountInfoRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountInfoResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Accounts = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/Accounts', cosmos.auth.v1beta1.query_pb2.QueryAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountsResponse)
        self.Account = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/Account', cosmos.auth.v1beta1.query_pb2.QueryAccountRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountResponse)
        self.AccountAddressByID = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/AccountAddressByID', cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountAddressByIDResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/Params', cosmos.auth.v1beta1.query_pb2.QueryParamsRequest, cosmos.auth.v1beta1.query_pb2.QueryParamsResponse)
        self.ModuleAccounts = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/ModuleAccounts', cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountsResponse)
        self.ModuleAccountByName = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/ModuleAccountByName', cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameRequest, cosmos.auth.v1beta1.query_pb2.QueryModuleAccountByNameResponse)
        self.Bech32Prefix = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/Bech32Prefix', cosmos.auth.v1beta1.query_pb2.Bech32PrefixRequest, cosmos.auth.v1beta1.query_pb2.Bech32PrefixResponse)
        self.AddressBytesToString = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/AddressBytesToString', cosmos.auth.v1beta1.query_pb2.AddressBytesToStringRequest, cosmos.auth.v1beta1.query_pb2.AddressBytesToStringResponse)
        self.AddressStringToBytes = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/AddressStringToBytes', cosmos.auth.v1beta1.query_pb2.AddressStringToBytesRequest, cosmos.auth.v1beta1.query_pb2.AddressStringToBytesResponse)
        self.AccountInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.auth.v1beta1.Query/AccountInfo', cosmos.auth.v1beta1.query_pb2.QueryAccountInfoRequest, cosmos.auth.v1beta1.query_pb2.QueryAccountInfoResponse)
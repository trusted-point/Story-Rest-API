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
    async def Balance(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryBalanceRequest, cosmos.nft.v1beta1.query_pb2.QueryBalanceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Owner(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryOwnerRequest, cosmos.nft.v1beta1.query_pb2.QueryOwnerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Supply(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QuerySupplyRequest, cosmos.nft.v1beta1.query_pb2.QuerySupplyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NFTs(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryNFTsRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NFT(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryNFTRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Class(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryClassRequest, cosmos.nft.v1beta1.query_pb2.QueryClassResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Classes(self, stream: 'grpclib.server.Stream[cosmos.nft.v1beta1.query_pb2.QueryClassesRequest, cosmos.nft.v1beta1.query_pb2.QueryClassesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.nft.v1beta1.Query/Balance': grpclib.const.Handler(self.Balance, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryBalanceRequest, cosmos.nft.v1beta1.query_pb2.QueryBalanceResponse), '/cosmos.nft.v1beta1.Query/Owner': grpclib.const.Handler(self.Owner, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryOwnerRequest, cosmos.nft.v1beta1.query_pb2.QueryOwnerResponse), '/cosmos.nft.v1beta1.Query/Supply': grpclib.const.Handler(self.Supply, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QuerySupplyRequest, cosmos.nft.v1beta1.query_pb2.QuerySupplyResponse), '/cosmos.nft.v1beta1.Query/NFTs': grpclib.const.Handler(self.NFTs, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryNFTsRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTsResponse), '/cosmos.nft.v1beta1.Query/NFT': grpclib.const.Handler(self.NFT, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryNFTRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTResponse), '/cosmos.nft.v1beta1.Query/Class': grpclib.const.Handler(self.Class, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryClassRequest, cosmos.nft.v1beta1.query_pb2.QueryClassResponse), '/cosmos.nft.v1beta1.Query/Classes': grpclib.const.Handler(self.Classes, grpclib.const.Cardinality.UNARY_UNARY, cosmos.nft.v1beta1.query_pb2.QueryClassesRequest, cosmos.nft.v1beta1.query_pb2.QueryClassesResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Balance = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/Balance', cosmos.nft.v1beta1.query_pb2.QueryBalanceRequest, cosmos.nft.v1beta1.query_pb2.QueryBalanceResponse)
        self.Owner = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/Owner', cosmos.nft.v1beta1.query_pb2.QueryOwnerRequest, cosmos.nft.v1beta1.query_pb2.QueryOwnerResponse)
        self.Supply = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/Supply', cosmos.nft.v1beta1.query_pb2.QuerySupplyRequest, cosmos.nft.v1beta1.query_pb2.QuerySupplyResponse)
        self.NFTs = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/NFTs', cosmos.nft.v1beta1.query_pb2.QueryNFTsRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTsResponse)
        self.NFT = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/NFT', cosmos.nft.v1beta1.query_pb2.QueryNFTRequest, cosmos.nft.v1beta1.query_pb2.QueryNFTResponse)
        self.Class = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/Class', cosmos.nft.v1beta1.query_pb2.QueryClassRequest, cosmos.nft.v1beta1.query_pb2.QueryClassResponse)
        self.Classes = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.nft.v1beta1.Query/Classes', cosmos.nft.v1beta1.query_pb2.QueryClassesRequest, cosmos.nft.v1beta1.query_pb2.QueryClassesResponse)
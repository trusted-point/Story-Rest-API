import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import gogoproto
import google.protobuf.any_pb2
from ..... import google
from ..... import tendermint
from ..... import cosmos
from ..... import cosmos_proto
from ..... import amino

class ServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetNodeInfo(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSyncing(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLatestBlock(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetBlockByHeight(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLatestValidatorSet(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetValidatorSetByHeight(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ABCIQuery(self, stream: 'grpclib.server.Stream[cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryRequest, cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.base.tendermint.v1beta1.Service/GetNodeInfo': grpclib.const.Handler(self.GetNodeInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoResponse), '/cosmos.base.tendermint.v1beta1.Service/GetSyncing': grpclib.const.Handler(self.GetSyncing, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingResponse), '/cosmos.base.tendermint.v1beta1.Service/GetLatestBlock': grpclib.const.Handler(self.GetLatestBlock, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockResponse), '/cosmos.base.tendermint.v1beta1.Service/GetBlockByHeight': grpclib.const.Handler(self.GetBlockByHeight, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightResponse), '/cosmos.base.tendermint.v1beta1.Service/GetLatestValidatorSet': grpclib.const.Handler(self.GetLatestValidatorSet, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetResponse), '/cosmos.base.tendermint.v1beta1.Service/GetValidatorSetByHeight': grpclib.const.Handler(self.GetValidatorSetByHeight, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightResponse), '/cosmos.base.tendermint.v1beta1.Service/ABCIQuery': grpclib.const.Handler(self.ABCIQuery, grpclib.const.Cardinality.UNARY_UNARY, cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryRequest, cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryResponse)}

class ServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetNodeInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetNodeInfo', cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetNodeInfoResponse)
        self.GetSyncing = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetSyncing', cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetSyncingResponse)
        self.GetLatestBlock = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetLatestBlock', cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestBlockResponse)
        self.GetBlockByHeight = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetBlockByHeight', cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetBlockByHeightResponse)
        self.GetLatestValidatorSet = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetLatestValidatorSet', cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetLatestValidatorSetResponse)
        self.GetValidatorSetByHeight = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/GetValidatorSetByHeight', cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightRequest, cosmos.base.tendermint.v1beta1.query_pb2.GetValidatorSetByHeightResponse)
        self.ABCIQuery = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.base.tendermint.v1beta1.Service/ABCIQuery', cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryRequest, cosmos.base.tendermint.v1beta1.query_pb2.ABCIQueryResponse)
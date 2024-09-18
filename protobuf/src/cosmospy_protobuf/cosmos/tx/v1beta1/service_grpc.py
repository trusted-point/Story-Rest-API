import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import google
from .... import cosmos
from .... import tendermint

class ServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Simulate(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.SimulateRequest, cosmos.tx.v1beta1.service_pb2.SimulateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTx(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.GetTxRequest, cosmos.tx.v1beta1.service_pb2.GetTxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BroadcastTx(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.BroadcastTxRequest, cosmos.tx.v1beta1.service_pb2.BroadcastTxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTxsEvent(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.GetTxsEventRequest, cosmos.tx.v1beta1.service_pb2.GetTxsEventResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetBlockWithTxs(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsRequest, cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TxDecode(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.TxDecodeRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TxEncode(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.TxEncodeRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TxEncodeAmino(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.TxEncodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeAminoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TxDecodeAmino(self, stream: 'grpclib.server.Stream[cosmos.tx.v1beta1.service_pb2.TxDecodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeAminoResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.tx.v1beta1.Service/Simulate': grpclib.const.Handler(self.Simulate, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.SimulateRequest, cosmos.tx.v1beta1.service_pb2.SimulateResponse), '/cosmos.tx.v1beta1.Service/GetTx': grpclib.const.Handler(self.GetTx, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.GetTxRequest, cosmos.tx.v1beta1.service_pb2.GetTxResponse), '/cosmos.tx.v1beta1.Service/BroadcastTx': grpclib.const.Handler(self.BroadcastTx, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.BroadcastTxRequest, cosmos.tx.v1beta1.service_pb2.BroadcastTxResponse), '/cosmos.tx.v1beta1.Service/GetTxsEvent': grpclib.const.Handler(self.GetTxsEvent, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.GetTxsEventRequest, cosmos.tx.v1beta1.service_pb2.GetTxsEventResponse), '/cosmos.tx.v1beta1.Service/GetBlockWithTxs': grpclib.const.Handler(self.GetBlockWithTxs, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsRequest, cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsResponse), '/cosmos.tx.v1beta1.Service/TxDecode': grpclib.const.Handler(self.TxDecode, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.TxDecodeRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeResponse), '/cosmos.tx.v1beta1.Service/TxEncode': grpclib.const.Handler(self.TxEncode, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.TxEncodeRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeResponse), '/cosmos.tx.v1beta1.Service/TxEncodeAmino': grpclib.const.Handler(self.TxEncodeAmino, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.TxEncodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeAminoResponse), '/cosmos.tx.v1beta1.Service/TxDecodeAmino': grpclib.const.Handler(self.TxDecodeAmino, grpclib.const.Cardinality.UNARY_UNARY, cosmos.tx.v1beta1.service_pb2.TxDecodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeAminoResponse)}

class ServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Simulate = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/Simulate', cosmos.tx.v1beta1.service_pb2.SimulateRequest, cosmos.tx.v1beta1.service_pb2.SimulateResponse)
        self.GetTx = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/GetTx', cosmos.tx.v1beta1.service_pb2.GetTxRequest, cosmos.tx.v1beta1.service_pb2.GetTxResponse)
        self.BroadcastTx = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/BroadcastTx', cosmos.tx.v1beta1.service_pb2.BroadcastTxRequest, cosmos.tx.v1beta1.service_pb2.BroadcastTxResponse)
        self.GetTxsEvent = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/GetTxsEvent', cosmos.tx.v1beta1.service_pb2.GetTxsEventRequest, cosmos.tx.v1beta1.service_pb2.GetTxsEventResponse)
        self.GetBlockWithTxs = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/GetBlockWithTxs', cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsRequest, cosmos.tx.v1beta1.service_pb2.GetBlockWithTxsResponse)
        self.TxDecode = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/TxDecode', cosmos.tx.v1beta1.service_pb2.TxDecodeRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeResponse)
        self.TxEncode = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/TxEncode', cosmos.tx.v1beta1.service_pb2.TxEncodeRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeResponse)
        self.TxEncodeAmino = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/TxEncodeAmino', cosmos.tx.v1beta1.service_pb2.TxEncodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxEncodeAminoResponse)
        self.TxDecodeAmino = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.tx.v1beta1.Service/TxDecodeAmino', cosmos.tx.v1beta1.service_pb2.TxDecodeAminoRequest, cosmos.tx.v1beta1.service_pb2.TxDecodeAminoResponse)
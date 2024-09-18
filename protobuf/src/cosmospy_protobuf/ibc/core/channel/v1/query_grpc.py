import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import ibc
from ..... import cosmos
from ..... import google
import google.protobuf.any_pb2
from ..... import gogoproto

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Channel(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryChannelRequest, ibc.core.channel.v1.query_pb2.QueryChannelResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Channels(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryChannelsRequest, ibc.core.channel.v1.query_pb2.QueryChannelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConnectionChannels(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryConnectionChannelsRequest, ibc.core.channel.v1.query_pb2.QueryConnectionChannelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChannelClientState(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryChannelClientStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelClientStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChannelConsensusState(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PacketCommitment(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryPacketCommitmentRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PacketCommitments(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PacketReceipt(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryPacketReceiptRequest, ibc.core.channel.v1.query_pb2.QueryPacketReceiptResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PacketAcknowledgement(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PacketAcknowledgements(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UnreceivedPackets(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UnreceivedAcks(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NextSequenceReceive(self, stream: 'grpclib.server.Stream[ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveRequest, ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.core.channel.v1.Query/Channel': grpclib.const.Handler(self.Channel, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryChannelRequest, ibc.core.channel.v1.query_pb2.QueryChannelResponse), '/ibc.core.channel.v1.Query/Channels': grpclib.const.Handler(self.Channels, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryChannelsRequest, ibc.core.channel.v1.query_pb2.QueryChannelsResponse), '/ibc.core.channel.v1.Query/ConnectionChannels': grpclib.const.Handler(self.ConnectionChannels, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryConnectionChannelsRequest, ibc.core.channel.v1.query_pb2.QueryConnectionChannelsResponse), '/ibc.core.channel.v1.Query/ChannelClientState': grpclib.const.Handler(self.ChannelClientState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryChannelClientStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelClientStateResponse), '/ibc.core.channel.v1.Query/ChannelConsensusState': grpclib.const.Handler(self.ChannelConsensusState, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateResponse), '/ibc.core.channel.v1.Query/PacketCommitment': grpclib.const.Handler(self.PacketCommitment, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentResponse), '/ibc.core.channel.v1.Query/PacketCommitments': grpclib.const.Handler(self.PacketCommitments, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsResponse), '/ibc.core.channel.v1.Query/PacketReceipt': grpclib.const.Handler(self.PacketReceipt, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryPacketReceiptRequest, ibc.core.channel.v1.query_pb2.QueryPacketReceiptResponse), '/ibc.core.channel.v1.Query/PacketAcknowledgement': grpclib.const.Handler(self.PacketAcknowledgement, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementResponse), '/ibc.core.channel.v1.Query/PacketAcknowledgements': grpclib.const.Handler(self.PacketAcknowledgements, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsResponse), '/ibc.core.channel.v1.Query/UnreceivedPackets': grpclib.const.Handler(self.UnreceivedPackets, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsResponse), '/ibc.core.channel.v1.Query/UnreceivedAcks': grpclib.const.Handler(self.UnreceivedAcks, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksResponse), '/ibc.core.channel.v1.Query/NextSequenceReceive': grpclib.const.Handler(self.NextSequenceReceive, grpclib.const.Cardinality.UNARY_UNARY, ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveRequest, ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Channel = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/Channel', ibc.core.channel.v1.query_pb2.QueryChannelRequest, ibc.core.channel.v1.query_pb2.QueryChannelResponse)
        self.Channels = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/Channels', ibc.core.channel.v1.query_pb2.QueryChannelsRequest, ibc.core.channel.v1.query_pb2.QueryChannelsResponse)
        self.ConnectionChannels = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/ConnectionChannels', ibc.core.channel.v1.query_pb2.QueryConnectionChannelsRequest, ibc.core.channel.v1.query_pb2.QueryConnectionChannelsResponse)
        self.ChannelClientState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/ChannelClientState', ibc.core.channel.v1.query_pb2.QueryChannelClientStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelClientStateResponse)
        self.ChannelConsensusState = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/ChannelConsensusState', ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateRequest, ibc.core.channel.v1.query_pb2.QueryChannelConsensusStateResponse)
        self.PacketCommitment = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/PacketCommitment', ibc.core.channel.v1.query_pb2.QueryPacketCommitmentRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentResponse)
        self.PacketCommitments = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/PacketCommitments', ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsRequest, ibc.core.channel.v1.query_pb2.QueryPacketCommitmentsResponse)
        self.PacketReceipt = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/PacketReceipt', ibc.core.channel.v1.query_pb2.QueryPacketReceiptRequest, ibc.core.channel.v1.query_pb2.QueryPacketReceiptResponse)
        self.PacketAcknowledgement = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/PacketAcknowledgement', ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementResponse)
        self.PacketAcknowledgements = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/PacketAcknowledgements', ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsRequest, ibc.core.channel.v1.query_pb2.QueryPacketAcknowledgementsResponse)
        self.UnreceivedPackets = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/UnreceivedPackets', ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedPacketsResponse)
        self.UnreceivedAcks = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/UnreceivedAcks', ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksRequest, ibc.core.channel.v1.query_pb2.QueryUnreceivedAcksResponse)
        self.NextSequenceReceive = grpclib.client.UnaryUnaryMethod(channel, '/ibc.core.channel.v1.Query/NextSequenceReceive', ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveRequest, ibc.core.channel.v1.query_pb2.QueryNextSequenceReceiveResponse)
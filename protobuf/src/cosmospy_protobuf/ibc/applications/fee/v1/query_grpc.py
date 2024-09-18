import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import gogoproto
from ..... import google
from ..... import cosmos
from ..... import ibc

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def IncentivizedPackets(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IncentivizedPacket(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IncentivizedPacketsForChannel(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TotalRecvFees(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TotalAckFees(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TotalTimeoutFees(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Payee(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryPayeeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CounterpartyPayee(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FeeEnabledChannels(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FeeEnabledChannel(self, stream: 'grpclib.server.Stream[ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.applications.fee.v1.Query/IncentivizedPackets': grpclib.const.Handler(self.IncentivizedPackets, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsResponse), '/ibc.applications.fee.v1.Query/IncentivizedPacket': grpclib.const.Handler(self.IncentivizedPacket, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketResponse), '/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel': grpclib.const.Handler(self.IncentivizedPacketsForChannel, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelResponse), '/ibc.applications.fee.v1.Query/TotalRecvFees': grpclib.const.Handler(self.TotalRecvFees, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesResponse), '/ibc.applications.fee.v1.Query/TotalAckFees': grpclib.const.Handler(self.TotalAckFees, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesResponse), '/ibc.applications.fee.v1.Query/TotalTimeoutFees': grpclib.const.Handler(self.TotalTimeoutFees, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesResponse), '/ibc.applications.fee.v1.Query/Payee': grpclib.const.Handler(self.Payee, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryPayeeResponse), '/ibc.applications.fee.v1.Query/CounterpartyPayee': grpclib.const.Handler(self.CounterpartyPayee, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeResponse), '/ibc.applications.fee.v1.Query/FeeEnabledChannels': grpclib.const.Handler(self.FeeEnabledChannels, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsResponse), '/ibc.applications.fee.v1.Query/FeeEnabledChannel': grpclib.const.Handler(self.FeeEnabledChannel, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.IncentivizedPackets = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/IncentivizedPackets', ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsResponse)
        self.IncentivizedPacket = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/IncentivizedPacket', ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketResponse)
        self.IncentivizedPacketsForChannel = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel', ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelRequest, ibc.applications.fee.v1.query_pb2.QueryIncentivizedPacketsForChannelResponse)
        self.TotalRecvFees = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/TotalRecvFees', ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalRecvFeesResponse)
        self.TotalAckFees = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/TotalAckFees', ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalAckFeesResponse)
        self.TotalTimeoutFees = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/TotalTimeoutFees', ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesRequest, ibc.applications.fee.v1.query_pb2.QueryTotalTimeoutFeesResponse)
        self.Payee = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/Payee', ibc.applications.fee.v1.query_pb2.QueryPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryPayeeResponse)
        self.CounterpartyPayee = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/CounterpartyPayee', ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeRequest, ibc.applications.fee.v1.query_pb2.QueryCounterpartyPayeeResponse)
        self.FeeEnabledChannels = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/FeeEnabledChannels', ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelsResponse)
        self.FeeEnabledChannel = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.fee.v1.Query/FeeEnabledChannel', ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelRequest, ibc.applications.fee.v1.query_pb2.QueryFeeEnabledChannelResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ..... import gogoproto
from ..... import cosmos
from ..... import ibc
from ..... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def DenomTrace(self, stream: 'grpclib.server.Stream[ibc.applications.transfer.v1.query_pb2.QueryDenomTraceRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTraceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomTraces(self, stream: 'grpclib.server.Stream[ibc.applications.transfer.v1.query_pb2.QueryDenomTracesRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTracesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[ibc.applications.transfer.v1.query_pb2.QueryParamsRequest, ibc.applications.transfer.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DenomHash(self, stream: 'grpclib.server.Stream[ibc.applications.transfer.v1.query_pb2.QueryDenomHashRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomHashResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EscrowAddress(self, stream: 'grpclib.server.Stream[ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressRequest, ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ibc.applications.transfer.v1.Query/DenomTrace': grpclib.const.Handler(self.DenomTrace, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.transfer.v1.query_pb2.QueryDenomTraceRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTraceResponse), '/ibc.applications.transfer.v1.Query/DenomTraces': grpclib.const.Handler(self.DenomTraces, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.transfer.v1.query_pb2.QueryDenomTracesRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTracesResponse), '/ibc.applications.transfer.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.transfer.v1.query_pb2.QueryParamsRequest, ibc.applications.transfer.v1.query_pb2.QueryParamsResponse), '/ibc.applications.transfer.v1.Query/DenomHash': grpclib.const.Handler(self.DenomHash, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.transfer.v1.query_pb2.QueryDenomHashRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomHashResponse), '/ibc.applications.transfer.v1.Query/EscrowAddress': grpclib.const.Handler(self.EscrowAddress, grpclib.const.Cardinality.UNARY_UNARY, ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressRequest, ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DenomTrace = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.transfer.v1.Query/DenomTrace', ibc.applications.transfer.v1.query_pb2.QueryDenomTraceRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTraceResponse)
        self.DenomTraces = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.transfer.v1.Query/DenomTraces', ibc.applications.transfer.v1.query_pb2.QueryDenomTracesRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomTracesResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.transfer.v1.Query/Params', ibc.applications.transfer.v1.query_pb2.QueryParamsRequest, ibc.applications.transfer.v1.query_pb2.QueryParamsResponse)
        self.DenomHash = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.transfer.v1.Query/DenomHash', ibc.applications.transfer.v1.query_pb2.QueryDenomHashRequest, ibc.applications.transfer.v1.query_pb2.QueryDenomHashResponse)
        self.EscrowAddress = grpclib.client.UnaryUnaryMethod(channel, '/ibc.applications.transfer.v1.Query/EscrowAddress', ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressRequest, ibc.applications.transfer.v1.query_pb2.QueryEscrowAddressResponse)
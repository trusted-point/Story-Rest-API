import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
import google.protobuf.any_pb2
from .... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Evidence(self, stream: 'grpclib.server.Stream[cosmos.evidence.v1beta1.query_pb2.QueryEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryEvidenceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AllEvidence(self, stream: 'grpclib.server.Stream[cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.evidence.v1beta1.Query/Evidence': grpclib.const.Handler(self.Evidence, grpclib.const.Cardinality.UNARY_UNARY, cosmos.evidence.v1beta1.query_pb2.QueryEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryEvidenceResponse), '/cosmos.evidence.v1beta1.Query/AllEvidence': grpclib.const.Handler(self.AllEvidence, grpclib.const.Cardinality.UNARY_UNARY, cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Evidence = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.evidence.v1beta1.Query/Evidence', cosmos.evidence.v1beta1.query_pb2.QueryEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryEvidenceResponse)
        self.AllEvidence = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.evidence.v1beta1.Query/AllEvidence', cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceRequest, cosmos.evidence.v1beta1.query_pb2.QueryAllEvidenceResponse)
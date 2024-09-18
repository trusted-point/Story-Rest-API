import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import gogoproto
from .... import google
from .... import cosmos_proto
from .... import amino

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Proposal(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryProposalRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Proposals(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryProposalsRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Vote(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryVoteRequest, cosmos.gov.v1beta1.query_pb2.QueryVoteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Votes(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryVotesRequest, cosmos.gov.v1beta1.query_pb2.QueryVotesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryParamsRequest, cosmos.gov.v1beta1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Deposit(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryDepositRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Deposits(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryDepositsRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TallyResult(self, stream: 'grpclib.server.Stream[cosmos.gov.v1beta1.query_pb2.QueryTallyResultRequest, cosmos.gov.v1beta1.query_pb2.QueryTallyResultResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.gov.v1beta1.Query/Proposal': grpclib.const.Handler(self.Proposal, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryProposalRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalResponse), '/cosmos.gov.v1beta1.Query/Proposals': grpclib.const.Handler(self.Proposals, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryProposalsRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalsResponse), '/cosmos.gov.v1beta1.Query/Vote': grpclib.const.Handler(self.Vote, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryVoteRequest, cosmos.gov.v1beta1.query_pb2.QueryVoteResponse), '/cosmos.gov.v1beta1.Query/Votes': grpclib.const.Handler(self.Votes, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryVotesRequest, cosmos.gov.v1beta1.query_pb2.QueryVotesResponse), '/cosmos.gov.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryParamsRequest, cosmos.gov.v1beta1.query_pb2.QueryParamsResponse), '/cosmos.gov.v1beta1.Query/Deposit': grpclib.const.Handler(self.Deposit, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryDepositRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositResponse), '/cosmos.gov.v1beta1.Query/Deposits': grpclib.const.Handler(self.Deposits, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryDepositsRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositsResponse), '/cosmos.gov.v1beta1.Query/TallyResult': grpclib.const.Handler(self.TallyResult, grpclib.const.Cardinality.UNARY_UNARY, cosmos.gov.v1beta1.query_pb2.QueryTallyResultRequest, cosmos.gov.v1beta1.query_pb2.QueryTallyResultResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Proposal = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Proposal', cosmos.gov.v1beta1.query_pb2.QueryProposalRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalResponse)
        self.Proposals = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Proposals', cosmos.gov.v1beta1.query_pb2.QueryProposalsRequest, cosmos.gov.v1beta1.query_pb2.QueryProposalsResponse)
        self.Vote = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Vote', cosmos.gov.v1beta1.query_pb2.QueryVoteRequest, cosmos.gov.v1beta1.query_pb2.QueryVoteResponse)
        self.Votes = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Votes', cosmos.gov.v1beta1.query_pb2.QueryVotesRequest, cosmos.gov.v1beta1.query_pb2.QueryVotesResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Params', cosmos.gov.v1beta1.query_pb2.QueryParamsRequest, cosmos.gov.v1beta1.query_pb2.QueryParamsResponse)
        self.Deposit = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Deposit', cosmos.gov.v1beta1.query_pb2.QueryDepositRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositResponse)
        self.Deposits = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/Deposits', cosmos.gov.v1beta1.query_pb2.QueryDepositsRequest, cosmos.gov.v1beta1.query_pb2.QueryDepositsResponse)
        self.TallyResult = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.gov.v1beta1.Query/TallyResult', cosmos.gov.v1beta1.query_pb2.QueryTallyResultRequest, cosmos.gov.v1beta1.query_pb2.QueryTallyResultResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import cosmos
from .... import cosmos_proto
from .... import amino

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def GroupInfo(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupInfoRequest, cosmos.group.v1.query_pb2.QueryGroupInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupPolicyInfo(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupPolicyInfoRequest, cosmos.group.v1.query_pb2.QueryGroupPolicyInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupMembers(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupMembersRequest, cosmos.group.v1.query_pb2.QueryGroupMembersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupsByAdmin(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupsByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupsByAdminResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupPoliciesByGroup(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupPoliciesByAdmin(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Proposal(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryProposalRequest, cosmos.group.v1.query_pb2.QueryProposalResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ProposalsByGroupPolicy(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyRequest, cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def VoteByProposalVoter(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryVoteByProposalVoterRequest, cosmos.group.v1.query_pb2.QueryVoteByProposalVoterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def VotesByProposal(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryVotesByProposalRequest, cosmos.group.v1.query_pb2.QueryVotesByProposalResponse]') -> None:
        pass

    @abc.abstractmethod
    async def VotesByVoter(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryVotesByVoterRequest, cosmos.group.v1.query_pb2.QueryVotesByVoterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupsByMember(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupsByMemberRequest, cosmos.group.v1.query_pb2.QueryGroupsByMemberResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TallyResult(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryTallyResultRequest, cosmos.group.v1.query_pb2.QueryTallyResultResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Groups(self, stream: 'grpclib.server.Stream[cosmos.group.v1.query_pb2.QueryGroupsRequest, cosmos.group.v1.query_pb2.QueryGroupsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/cosmos.group.v1.Query/GroupInfo': grpclib.const.Handler(self.GroupInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupInfoRequest, cosmos.group.v1.query_pb2.QueryGroupInfoResponse), '/cosmos.group.v1.Query/GroupPolicyInfo': grpclib.const.Handler(self.GroupPolicyInfo, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupPolicyInfoRequest, cosmos.group.v1.query_pb2.QueryGroupPolicyInfoResponse), '/cosmos.group.v1.Query/GroupMembers': grpclib.const.Handler(self.GroupMembers, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupMembersRequest, cosmos.group.v1.query_pb2.QueryGroupMembersResponse), '/cosmos.group.v1.Query/GroupsByAdmin': grpclib.const.Handler(self.GroupsByAdmin, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupsByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupsByAdminResponse), '/cosmos.group.v1.Query/GroupPoliciesByGroup': grpclib.const.Handler(self.GroupPoliciesByGroup, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupResponse), '/cosmos.group.v1.Query/GroupPoliciesByAdmin': grpclib.const.Handler(self.GroupPoliciesByAdmin, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminResponse), '/cosmos.group.v1.Query/Proposal': grpclib.const.Handler(self.Proposal, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryProposalRequest, cosmos.group.v1.query_pb2.QueryProposalResponse), '/cosmos.group.v1.Query/ProposalsByGroupPolicy': grpclib.const.Handler(self.ProposalsByGroupPolicy, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyRequest, cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyResponse), '/cosmos.group.v1.Query/VoteByProposalVoter': grpclib.const.Handler(self.VoteByProposalVoter, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryVoteByProposalVoterRequest, cosmos.group.v1.query_pb2.QueryVoteByProposalVoterResponse), '/cosmos.group.v1.Query/VotesByProposal': grpclib.const.Handler(self.VotesByProposal, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryVotesByProposalRequest, cosmos.group.v1.query_pb2.QueryVotesByProposalResponse), '/cosmos.group.v1.Query/VotesByVoter': grpclib.const.Handler(self.VotesByVoter, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryVotesByVoterRequest, cosmos.group.v1.query_pb2.QueryVotesByVoterResponse), '/cosmos.group.v1.Query/GroupsByMember': grpclib.const.Handler(self.GroupsByMember, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupsByMemberRequest, cosmos.group.v1.query_pb2.QueryGroupsByMemberResponse), '/cosmos.group.v1.Query/TallyResult': grpclib.const.Handler(self.TallyResult, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryTallyResultRequest, cosmos.group.v1.query_pb2.QueryTallyResultResponse), '/cosmos.group.v1.Query/Groups': grpclib.const.Handler(self.Groups, grpclib.const.Cardinality.UNARY_UNARY, cosmos.group.v1.query_pb2.QueryGroupsRequest, cosmos.group.v1.query_pb2.QueryGroupsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GroupInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupInfo', cosmos.group.v1.query_pb2.QueryGroupInfoRequest, cosmos.group.v1.query_pb2.QueryGroupInfoResponse)
        self.GroupPolicyInfo = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupPolicyInfo', cosmos.group.v1.query_pb2.QueryGroupPolicyInfoRequest, cosmos.group.v1.query_pb2.QueryGroupPolicyInfoResponse)
        self.GroupMembers = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupMembers', cosmos.group.v1.query_pb2.QueryGroupMembersRequest, cosmos.group.v1.query_pb2.QueryGroupMembersResponse)
        self.GroupsByAdmin = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupsByAdmin', cosmos.group.v1.query_pb2.QueryGroupsByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupsByAdminResponse)
        self.GroupPoliciesByGroup = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupPoliciesByGroup', cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByGroupResponse)
        self.GroupPoliciesByAdmin = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupPoliciesByAdmin', cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminRequest, cosmos.group.v1.query_pb2.QueryGroupPoliciesByAdminResponse)
        self.Proposal = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/Proposal', cosmos.group.v1.query_pb2.QueryProposalRequest, cosmos.group.v1.query_pb2.QueryProposalResponse)
        self.ProposalsByGroupPolicy = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/ProposalsByGroupPolicy', cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyRequest, cosmos.group.v1.query_pb2.QueryProposalsByGroupPolicyResponse)
        self.VoteByProposalVoter = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/VoteByProposalVoter', cosmos.group.v1.query_pb2.QueryVoteByProposalVoterRequest, cosmos.group.v1.query_pb2.QueryVoteByProposalVoterResponse)
        self.VotesByProposal = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/VotesByProposal', cosmos.group.v1.query_pb2.QueryVotesByProposalRequest, cosmos.group.v1.query_pb2.QueryVotesByProposalResponse)
        self.VotesByVoter = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/VotesByVoter', cosmos.group.v1.query_pb2.QueryVotesByVoterRequest, cosmos.group.v1.query_pb2.QueryVotesByVoterResponse)
        self.GroupsByMember = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/GroupsByMember', cosmos.group.v1.query_pb2.QueryGroupsByMemberRequest, cosmos.group.v1.query_pb2.QueryGroupsByMemberResponse)
        self.TallyResult = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/TallyResult', cosmos.group.v1.query_pb2.QueryTallyResultRequest, cosmos.group.v1.query_pb2.QueryTallyResultResponse)
        self.Groups = grpclib.client.UnaryUnaryMethod(channel, '/cosmos.group.v1.Query/Groups', cosmos.group.v1.query_pb2.QueryGroupsRequest, cosmos.group.v1.query_pb2.QueryGroupsResponse)
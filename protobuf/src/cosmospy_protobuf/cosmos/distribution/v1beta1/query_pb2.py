"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/distribution/v1beta1/query.proto\x12\x1bcosmos.distribution.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\x14\n\x12QueryParamsRequest"U\n\x13QueryParamsResponse\x12>\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"e\n%QueryValidatorDistributionInfoRequest\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString"\xbf\x02\n&QueryValidatorDistributionInfoResponse\x12;\n\x10operator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString\x12q\n\x11self_bond_rewards\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01\x12e\n\ncommission\x18\x03 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"g\n\'QueryValidatorOutstandingRewardsRequest\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString"\x80\x01\n(QueryValidatorOutstandingRewardsResponse\x12T\n\x07rewards\x18\x01 \x01(\x0b28.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"_\n\x1fQueryValidatorCommissionRequest\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString"~\n QueryValidatorCommissionResponse\x12Z\n\ncommission\x18\x01 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\xce\x01\n\x1cQueryValidatorSlashesRequest\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString\x12\x17\n\x0fstarting_height\x18\x02 \x01(\x04\x12\x15\n\rending_height\x18\x03 \x01(\x04\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x04\x88\xa0\x1f\x00"\xaa\x01\n\x1dQueryValidatorSlashesResponse\x12L\n\x07slashes\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x9c\x01\n\x1dQueryDelegationRewardsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x89\x01\n\x1eQueryDelegationRewardsResponse\x12g\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01"c\n"QueryDelegationTotalRewardsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xe0\x01\n#QueryDelegationTotalRewardsResponse\x12R\n\x07rewards\x18\x01 \x03(\x0b26.cosmos.distribution.v1beta1.DelegationDelegatorRewardB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12e\n\x05total\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01"`\n\x1fQueryDelegatorValidatorsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"@\n QueryDelegatorValidatorsResponse\x12\x12\n\nvalidators\x18\x01 \x03(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"e\n$QueryDelegatorWithdrawAddressRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"e\n%QueryDelegatorWithdrawAddressResponse\x122\n\x10withdraw_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1b\n\x19QueryCommunityPoolRequest"\x82\x01\n\x1aQueryCommunityPoolResponse\x12d\n\x04pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x012\xc4\x11\n\x05Query\x12\x98\x01\n\x06Params\x12/.cosmos.distribution.v1beta1.QueryParamsRequest\x1a0.cosmos.distribution.v1beta1.QueryParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params\x12\xe9\x01\n\x19ValidatorDistributionInfo\x12B.cosmos.distribution.v1beta1.QueryValidatorDistributionInfoRequest\x1aC.cosmos.distribution.v1beta1.QueryValidatorDistributionInfoResponse"C\x82\xd3\xe4\x93\x02=\x12;/cosmos/distribution/v1beta1/validators/{validator_address}\x12\x83\x02\n\x1bValidatorOutstandingRewards\x12D.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsRequest\x1aE.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsResponse"W\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards\x12\xe2\x01\n\x13ValidatorCommission\x12<.cosmos.distribution.v1beta1.QueryValidatorCommissionRequest\x1a=.cosmos.distribution.v1beta1.QueryValidatorCommissionResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission\x12\xd6\x01\n\x10ValidatorSlashes\x129.cosmos.distribution.v1beta1.QueryValidatorSlashesRequest\x1a:.cosmos.distribution.v1beta1.QueryValidatorSlashesResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes\x12\xed\x01\n\x11DelegationRewards\x12:.cosmos.distribution.v1beta1.QueryDelegationRewardsRequest\x1a;.cosmos.distribution.v1beta1.QueryDelegationRewardsResponse"_\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}\x12\xe8\x01\n\x16DelegationTotalRewards\x12?.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsRequest\x1a@.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards\x12\xe2\x01\n\x13DelegatorValidators\x12<.cosmos.distribution.v1beta1.QueryDelegatorValidatorsRequest\x1a=.cosmos.distribution.v1beta1.QueryDelegatorValidatorsResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators\x12\xf7\x01\n\x18DelegatorWithdrawAddress\x12A.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressRequest\x1aB.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressResponse"T\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address\x12\xb5\x01\n\rCommunityPool\x126.cosmos.distribution.v1beta1.QueryCommunityPoolRequest\x1a7.cosmos.distribution.v1beta1.QueryCommunityPoolResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_poolB3Z1github.com/cosmos/cosmos-sdk/x/distribution/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORDISTRIBUTIONINFOREQUEST'].fields_by_name['validator_address']._options = None
    _globals['_QUERYVALIDATORDISTRIBUTIONINFOREQUEST'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['operator_address']._options = None
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['operator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['self_bond_rewards']._options = None
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['self_bond_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['commission']._options = None
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE'].fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST'].fields_by_name['validator_address']._options = None
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE'].fields_by_name['rewards']._options = None
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST'].fields_by_name['validator_address']._options = None
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE'].fields_by_name['commission']._options = None
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE'].fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORSLASHESREQUEST'].fields_by_name['validator_address']._options = None
    _globals['_QUERYVALIDATORSLASHESREQUEST'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYVALIDATORSLASHESREQUEST']._options = None
    _globals['_QUERYVALIDATORSLASHESREQUEST']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_QUERYVALIDATORSLASHESRESPONSE'].fields_by_name['slashes']._options = None
    _globals['_QUERYVALIDATORSLASHESRESPONSE'].fields_by_name['slashes']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATIONREWARDSREQUEST'].fields_by_name['delegator_address']._options = None
    _globals['_QUERYDELEGATIONREWARDSREQUEST'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATIONREWARDSREQUEST'].fields_by_name['validator_address']._options = None
    _globals['_QUERYDELEGATIONREWARDSREQUEST'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._options = None
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATIONREWARDSRESPONSE'].fields_by_name['rewards']._options = None
    _globals['_QUERYDELEGATIONREWARDSRESPONSE'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST'].fields_by_name['delegator_address']._options = None
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._options = None
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE'].fields_by_name['rewards']._options = None
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE'].fields_by_name['total']._options = None
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE'].fields_by_name['total']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATORVALIDATORSREQUEST'].fields_by_name['delegator_address']._options = None
    _globals['_QUERYDELEGATORVALIDATORSREQUEST'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._options = None
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._options = None
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST'].fields_by_name['delegator_address']._options = None
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST'].fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._options = None
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE'].fields_by_name['withdraw_address']._options = None
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE'].fields_by_name['withdraw_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._options = None
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYCOMMUNITYPOOLRESPONSE'].fields_by_name['pool']._options = None
    _globals['_QUERYCOMMUNITYPOOLRESPONSE'].fields_by_name['pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_QUERY'].methods_by_name['Params']._options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params'
    _globals['_QUERY'].methods_by_name['ValidatorDistributionInfo']._options = None
    _globals['_QUERY'].methods_by_name['ValidatorDistributionInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/cosmos/distribution/v1beta1/validators/{validator_address}'
    _globals['_QUERY'].methods_by_name['ValidatorOutstandingRewards']._options = None
    _globals['_QUERY'].methods_by_name['ValidatorOutstandingRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards'
    _globals['_QUERY'].methods_by_name['ValidatorCommission']._options = None
    _globals['_QUERY'].methods_by_name['ValidatorCommission']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission'
    _globals['_QUERY'].methods_by_name['ValidatorSlashes']._options = None
    _globals['_QUERY'].methods_by_name['ValidatorSlashes']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes'
    _globals['_QUERY'].methods_by_name['DelegationRewards']._options = None
    _globals['_QUERY'].methods_by_name['DelegationRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}'
    _globals['_QUERY'].methods_by_name['DelegationTotalRewards']._options = None
    _globals['_QUERY'].methods_by_name['DelegationTotalRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards'
    _globals['_QUERY'].methods_by_name['DelegatorValidators']._options = None
    _globals['_QUERY'].methods_by_name['DelegatorValidators']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators'
    _globals['_QUERY'].methods_by_name['DelegatorWithdrawAddress']._options = None
    _globals['_QUERY'].methods_by_name['DelegatorWithdrawAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address'
    _globals['_QUERY'].methods_by_name['CommunityPool']._options = None
    _globals['_QUERY'].methods_by_name['CommunityPool']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_pool'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 294
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 314
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 316
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 401
    _globals['_QUERYVALIDATORDISTRIBUTIONINFOREQUEST']._serialized_start = 403
    _globals['_QUERYVALIDATORDISTRIBUTIONINFOREQUEST']._serialized_end = 504
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE']._serialized_start = 507
    _globals['_QUERYVALIDATORDISTRIBUTIONINFORESPONSE']._serialized_end = 826
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST']._serialized_start = 828
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST']._serialized_end = 931
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE']._serialized_start = 934
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE']._serialized_end = 1062
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST']._serialized_start = 1064
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST']._serialized_end = 1159
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE']._serialized_start = 1161
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE']._serialized_end = 1287
    _globals['_QUERYVALIDATORSLASHESREQUEST']._serialized_start = 1290
    _globals['_QUERYVALIDATORSLASHESREQUEST']._serialized_end = 1496
    _globals['_QUERYVALIDATORSLASHESRESPONSE']._serialized_start = 1499
    _globals['_QUERYVALIDATORSLASHESRESPONSE']._serialized_end = 1669
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._serialized_start = 1672
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._serialized_end = 1828
    _globals['_QUERYDELEGATIONREWARDSRESPONSE']._serialized_start = 1831
    _globals['_QUERYDELEGATIONREWARDSRESPONSE']._serialized_end = 1968
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._serialized_start = 1970
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._serialized_end = 2069
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE']._serialized_start = 2072
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE']._serialized_end = 2296
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_start = 2298
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_end = 2394
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_start = 2396
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_end = 2460
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._serialized_start = 2462
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._serialized_end = 2563
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._serialized_start = 2565
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._serialized_end = 2666
    _globals['_QUERYCOMMUNITYPOOLREQUEST']._serialized_start = 2668
    _globals['_QUERYCOMMUNITYPOOLREQUEST']._serialized_end = 2695
    _globals['_QUERYCOMMUNITYPOOLRESPONSE']._serialized_start = 2698
    _globals['_QUERYCOMMUNITYPOOLRESPONSE']._serialized_end = 2828
    _globals['_QUERY']._serialized_start = 2831
    _globals['_QUERY']._serialized_end = 5075
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\xce\x02\n\x06Params\x12M\n\rcommunity_tax\x18\x01 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12V\n\x14base_proposer_reward\x18\x02 \x01(\tB8\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12W\n\x15bonus_proposer_reward\x18\x03 \x01(\tB8\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12\x1d\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08:%\x8a\xe7\xb0* cosmos-sdk/x/distribution/Params"\xae\x01\n\x1aValidatorHistoricalRewards\x12w\n\x17cumulative_reward_ratio\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01\x12\x17\n\x0freference_count\x18\x02 \x01(\r"\x92\x01\n\x17ValidatorCurrentRewards\x12g\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01\x12\x0e\n\x06period\x18\x02 \x01(\x04"\x8c\x01\n\x1eValidatorAccumulatedCommission\x12j\n\ncommission\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01"\x86\x01\n\x1bValidatorOutstandingRewards\x12g\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01"t\n\x13ValidatorSlashEvent\x12\x18\n\x10validator_period\x18\x01 \x01(\x04\x12C\n\x08fraction\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec"s\n\x14ValidatorSlashEvents\x12[\n\x16validator_slash_events\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"y\n\x07FeePool\x12n\n\x0ecommunity_pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01"\xf0\x01\n\x1aCommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12q\n\x06amount\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01:(\x18\x01\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content"\xb5\x01\n\x15DelegatorStartingInfo\x12\x17\n\x0fprevious_period\x18\x01 \x01(\x04\x12E\n\x05stake\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\x12<\n\x06height\x18\x03 \x01(\x04B,\xea\xde\x1f\x0fcreation_height\xa2\xe7\xb0*\x0fcreation_height\xa8\xe7\xb0*\x01"\xc7\x01\n\x19DelegationDelegatorReward\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1dcosmos.ValidatorAddressString\x12f\n\x06reward\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01:\x04\x88\xa0\x1f\x00"\xa3\x01\n%CommunityPoolSpendProposalWithDeposit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x0e\n\x06amount\x18\x04 \x01(\t\x12\x0f\n\x07deposit\x18\x05 \x01(\t:"\x88\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.ContentB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.distribution_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _globals['_PARAMS'].fields_by_name['community_tax']._options = None
    _globals['_PARAMS'].fields_by_name['community_tax']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS'].fields_by_name['base_proposer_reward']._options = None
    _globals['_PARAMS'].fields_by_name['base_proposer_reward']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS'].fields_by_name['bonus_proposer_reward']._options = None
    _globals['_PARAMS'].fields_by_name['bonus_proposer_reward']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_PARAMS']._options = None
    _globals['_PARAMS']._serialized_options = b'\x8a\xe7\xb0* cosmos-sdk/x/distribution/Params'
    _globals['_VALIDATORHISTORICALREWARDS'].fields_by_name['cumulative_reward_ratio']._options = None
    _globals['_VALIDATORHISTORICALREWARDS'].fields_by_name['cumulative_reward_ratio']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_VALIDATORCURRENTREWARDS'].fields_by_name['rewards']._options = None
    _globals['_VALIDATORCURRENTREWARDS'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_VALIDATORACCUMULATEDCOMMISSION'].fields_by_name['commission']._options = None
    _globals['_VALIDATORACCUMULATEDCOMMISSION'].fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_VALIDATOROUTSTANDINGREWARDS'].fields_by_name['rewards']._options = None
    _globals['_VALIDATOROUTSTANDINGREWARDS'].fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_VALIDATORSLASHEVENT'].fields_by_name['fraction']._options = None
    _globals['_VALIDATORSLASHEVENT'].fields_by_name['fraction']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec'
    _globals['_VALIDATORSLASHEVENTS'].fields_by_name['validator_slash_events']._options = None
    _globals['_VALIDATORSLASHEVENTS'].fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_FEEPOOL'].fields_by_name['community_pool']._options = None
    _globals['_FEEPOOL'].fields_by_name['community_pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_COMMUNITYPOOLSPENDPROPOSAL'].fields_by_name['amount']._options = None
    _globals['_COMMUNITYPOOLSPENDPROPOSAL'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._options = None
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._serialized_options = b'\x18\x01\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _globals['_DELEGATORSTARTINGINFO'].fields_by_name['stake']._options = None
    _globals['_DELEGATORSTARTINGINFO'].fields_by_name['stake']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01'
    _globals['_DELEGATORSTARTINGINFO'].fields_by_name['height']._options = None
    _globals['_DELEGATORSTARTINGINFO'].fields_by_name['height']._serialized_options = b'\xea\xde\x1f\x0fcreation_height\xa2\xe7\xb0*\x0fcreation_height\xa8\xe7\xb0*\x01'
    _globals['_DELEGATIONDELEGATORREWARD'].fields_by_name['validator_address']._options = None
    _globals['_DELEGATIONDELEGATORREWARD'].fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x1dcosmos.ValidatorAddressString'
    _globals['_DELEGATIONDELEGATORREWARD'].fields_by_name['reward']._options = None
    _globals['_DELEGATIONDELEGATORREWARD'].fields_by_name['reward']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _globals['_DELEGATIONDELEGATORREWARD']._options = None
    _globals['_DELEGATIONDELEGATORREWARD']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._options = None
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _globals['_PARAMS']._serialized_start = 180
    _globals['_PARAMS']._serialized_end = 514
    _globals['_VALIDATORHISTORICALREWARDS']._serialized_start = 517
    _globals['_VALIDATORHISTORICALREWARDS']._serialized_end = 691
    _globals['_VALIDATORCURRENTREWARDS']._serialized_start = 694
    _globals['_VALIDATORCURRENTREWARDS']._serialized_end = 840
    _globals['_VALIDATORACCUMULATEDCOMMISSION']._serialized_start = 843
    _globals['_VALIDATORACCUMULATEDCOMMISSION']._serialized_end = 983
    _globals['_VALIDATOROUTSTANDINGREWARDS']._serialized_start = 986
    _globals['_VALIDATOROUTSTANDINGREWARDS']._serialized_end = 1120
    _globals['_VALIDATORSLASHEVENT']._serialized_start = 1122
    _globals['_VALIDATORSLASHEVENT']._serialized_end = 1238
    _globals['_VALIDATORSLASHEVENTS']._serialized_start = 1240
    _globals['_VALIDATORSLASHEVENTS']._serialized_end = 1355
    _globals['_FEEPOOL']._serialized_start = 1357
    _globals['_FEEPOOL']._serialized_end = 1478
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._serialized_start = 1481
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._serialized_end = 1721
    _globals['_DELEGATORSTARTINGINFO']._serialized_start = 1724
    _globals['_DELEGATORSTARTINGINFO']._serialized_end = 1905
    _globals['_DELEGATIONDELEGATORREWARD']._serialized_start = 1908
    _globals['_DELEGATIONDELEGATORREWARD']._serialized_end = 2107
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._serialized_start = 2110
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._serialized_end = 2273
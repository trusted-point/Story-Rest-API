"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....ibc.lightclients.tendermint.v1 import tendermint_pb2 as ibc_dot_lightclients_dot_tendermint_dot_v1_dot_tendermint__pb2
from .....tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2
from .....cosmos.evidence.v1beta1 import evidence_pb2 as cosmos_dot_evidence_dot_v1beta1_dot_evidence__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2interchain_security/ccv/provider/v1/provider.proto\x12#interchain_security.ccv.provider.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fibc/core/client/v1/client.proto\x1a/ibc/lightclients/tendermint/v1/tendermint.proto\x1a\x1ctendermint/crypto/keys.proto\x1a&cosmos/evidence/v1beta1/evidence.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xde\x04\n\x18ConsumerAdditionProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x128\n\x0einitial_height\x18\x04 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cgenesis_hash\x18\x05 \x01(\x0c\x12\x13\n\x0bbinary_hash\x18\x06 \x01(\x0c\x128\n\nspawn_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12=\n\x10unbonding_period\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12?\n\x12ccv_timeout_period\x18\t \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12D\n\x17transfer_timeout_period\x18\n \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12(\n consumer_redistribution_fraction\x18\x0b \x01(\t\x12,\n$blocks_per_distribution_transmission\x18\x0c \x01(\x03\x12\x1a\n\x12historical_entries\x18\r \x01(\x03\x12)\n!distribution_transmission_channel\x18\x0e \x01(\t:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\x88\x01\n\x17ConsumerRemovalProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x127\n\tstop_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"x\n\x14EquivocationProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12<\n\requivocations\x18\x03 \x03(\x0b2%.cosmos.evidence.v1beta1.Equivocation"\xb0\x01\n\x10GlobalSlashEntry\x127\n\trecv_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12.\n\x11consumer_chain_id\x18\x02 \x01(\tB\x13\xe2\xde\x1f\x0fConsumerChainID\x12\x13\n\x0bibc_seq_num\x18\x03 \x01(\x04\x12\x1e\n\x16provider_val_cons_addr\x18\x04 \x01(\x0c"\x97\x04\n\x06Params\x12D\n\x0ftemplate_client\x18\x01 \x01(\x0b2+.ibc.lightclients.tendermint.v1.ClientState\x12 \n\x18trusting_period_fraction\x18\x02 \x01(\t\x12?\n\x12ccv_timeout_period\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12@\n\x13init_timeout_period\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12?\n\x12vsc_timeout_period\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12I\n\x1cslash_meter_replenish_period\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12&\n\x1eslash_meter_replenish_fraction\x18\x07 \x01(\t\x12\x1d\n\x15max_throttled_packets\x18\x08 \x01(\x03\x12O\n&consumer_reward_denom_registration_fee\x18\t \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"D\n\x11HandshakeMetadata\x12\x1e\n\x16provider_fee_pool_addr\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t"\x1e\n\tSlashAcks\x12\x11\n\taddresses\x18\x01 \x03(\t"k\n\x19ConsumerAdditionProposals\x12N\n\x07pending\x18\x01 \x03(\x0b2=.interchain_security.ccv.provider.v1.ConsumerAdditionProposal"i\n\x18ConsumerRemovalProposals\x12M\n\x07pending\x18\x01 \x03(\x0b2<.interchain_security.ccv.provider.v1.ConsumerRemovalProposal" \n\x0bAddressList\x12\x11\n\taddresses\x18\x01 \x03(\x0c"6\n\x0eChannelToChain\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x10\n\x08chain_id\x18\x02 \x01(\t";\n\x0fVscUnbondingOps\x12\x0e\n\x06vsc_id\x18\x01 \x01(\x04\x12\x18\n\x10unbonding_op_ids\x18\x02 \x03(\x04"<\n\x0bUnbondingOp\x12\n\n\x02id\x18\x01 \x01(\x04\x12!\n\x19unbonding_consumer_chains\x18\x02 \x03(\t";\n\x14InitTimeoutTimestamp\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04"[\n\x10VscSendTimestamp\x12\x0e\n\x06vsc_id\x18\x01 \x01(\x04\x127\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"r\n\x18KeyAssignmentReplacement\x12\x15\n\rprovider_addr\x18\x01 \x01(\x0c\x120\n\nprev_c_key\x18\x02 \x01(\x0b2\x1c.tendermint.crypto.PublicKey\x12\r\n\x05power\x18\x03 \x01(\x03"v\n\x17ValidatorConsumerPubKey\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12\x15\n\rprovider_addr\x18\x02 \x01(\x0c\x122\n\x0cconsumer_key\x18\x03 \x01(\x0b2\x1c.tendermint.crypto.PublicKey"Y\n\x17ValidatorByConsumerAddr\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12\x15\n\rconsumer_addr\x18\x02 \x01(\x0c\x12\x15\n\rprovider_addr\x18\x03 \x01(\x0c"\x82\x01\n\x14ConsumerAddrsToPrune\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12\x0e\n\x06vsc_id\x18\x02 \x01(\x04\x12H\n\x0econsumer_addrs\x18\x03 \x01(\x0b20.interchain_security.ccv.provider.v1.AddressListB?Z=github.com/cosmos/interchain-security/v2/x/ccv/provider/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'interchain_security.ccv.provider.v1.provider_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cosmos/interchain-security/v2/x/ccv/provider/types'
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['initial_height']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['initial_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['spawn_time']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['spawn_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['unbonding_period']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['unbonding_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['ccv_timeout_period']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['ccv_timeout_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['transfer_timeout_period']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL'].fields_by_name['transfer_timeout_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_CONSUMERADDITIONPROPOSAL']._options = None
    _globals['_CONSUMERADDITIONPROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_CONSUMERREMOVALPROPOSAL'].fields_by_name['stop_time']._options = None
    _globals['_CONSUMERREMOVALPROPOSAL'].fields_by_name['stop_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_GLOBALSLASHENTRY'].fields_by_name['recv_time']._options = None
    _globals['_GLOBALSLASHENTRY'].fields_by_name['recv_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_GLOBALSLASHENTRY'].fields_by_name['consumer_chain_id']._options = None
    _globals['_GLOBALSLASHENTRY'].fields_by_name['consumer_chain_id']._serialized_options = b'\xe2\xde\x1f\x0fConsumerChainID'
    _globals['_PARAMS'].fields_by_name['ccv_timeout_period']._options = None
    _globals['_PARAMS'].fields_by_name['ccv_timeout_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS'].fields_by_name['init_timeout_period']._options = None
    _globals['_PARAMS'].fields_by_name['init_timeout_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS'].fields_by_name['vsc_timeout_period']._options = None
    _globals['_PARAMS'].fields_by_name['vsc_timeout_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS'].fields_by_name['slash_meter_replenish_period']._options = None
    _globals['_PARAMS'].fields_by_name['slash_meter_replenish_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS'].fields_by_name['consumer_reward_denom_registration_fee']._options = None
    _globals['_PARAMS'].fields_by_name['consumer_reward_denom_registration_fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VSCSENDTIMESTAMP'].fields_by_name['timestamp']._options = None
    _globals['_VSCSENDTIMESTAMP'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_CONSUMERADDITIONPROPOSAL']._serialized_start = 363
    _globals['_CONSUMERADDITIONPROPOSAL']._serialized_end = 969
    _globals['_CONSUMERREMOVALPROPOSAL']._serialized_start = 972
    _globals['_CONSUMERREMOVALPROPOSAL']._serialized_end = 1108
    _globals['_EQUIVOCATIONPROPOSAL']._serialized_start = 1110
    _globals['_EQUIVOCATIONPROPOSAL']._serialized_end = 1230
    _globals['_GLOBALSLASHENTRY']._serialized_start = 1233
    _globals['_GLOBALSLASHENTRY']._serialized_end = 1409
    _globals['_PARAMS']._serialized_start = 1412
    _globals['_PARAMS']._serialized_end = 1947
    _globals['_HANDSHAKEMETADATA']._serialized_start = 1949
    _globals['_HANDSHAKEMETADATA']._serialized_end = 2017
    _globals['_SLASHACKS']._serialized_start = 2019
    _globals['_SLASHACKS']._serialized_end = 2049
    _globals['_CONSUMERADDITIONPROPOSALS']._serialized_start = 2051
    _globals['_CONSUMERADDITIONPROPOSALS']._serialized_end = 2158
    _globals['_CONSUMERREMOVALPROPOSALS']._serialized_start = 2160
    _globals['_CONSUMERREMOVALPROPOSALS']._serialized_end = 2265
    _globals['_ADDRESSLIST']._serialized_start = 2267
    _globals['_ADDRESSLIST']._serialized_end = 2299
    _globals['_CHANNELTOCHAIN']._serialized_start = 2301
    _globals['_CHANNELTOCHAIN']._serialized_end = 2355
    _globals['_VSCUNBONDINGOPS']._serialized_start = 2357
    _globals['_VSCUNBONDINGOPS']._serialized_end = 2416
    _globals['_UNBONDINGOP']._serialized_start = 2418
    _globals['_UNBONDINGOP']._serialized_end = 2478
    _globals['_INITTIMEOUTTIMESTAMP']._serialized_start = 2480
    _globals['_INITTIMEOUTTIMESTAMP']._serialized_end = 2539
    _globals['_VSCSENDTIMESTAMP']._serialized_start = 2541
    _globals['_VSCSENDTIMESTAMP']._serialized_end = 2632
    _globals['_KEYASSIGNMENTREPLACEMENT']._serialized_start = 2634
    _globals['_KEYASSIGNMENTREPLACEMENT']._serialized_end = 2748
    _globals['_VALIDATORCONSUMERPUBKEY']._serialized_start = 2750
    _globals['_VALIDATORCONSUMERPUBKEY']._serialized_end = 2868
    _globals['_VALIDATORBYCONSUMERADDR']._serialized_start = 2870
    _globals['_VALIDATORBYCONSUMERADDR']._serialized_end = 2959
    _globals['_CONSUMERADDRSTOPRUNE']._serialized_start = 2962
    _globals['_CONSUMERADDRSTOPRUNE']._serialized_end = 3092
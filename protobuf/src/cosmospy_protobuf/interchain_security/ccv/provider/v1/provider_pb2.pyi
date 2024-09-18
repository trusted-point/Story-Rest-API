from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from ibc.core.client.v1 import client_pb2 as _client_pb2
from ibc.lightclients.tendermint.v1 import tendermint_pb2 as _tendermint_pb2
from tendermint.crypto import keys_pb2 as _keys_pb2
from cosmos.evidence.v1beta1 import evidence_pb2 as _evidence_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerAdditionProposal(_message.Message):
    __slots__ = ('title', 'description', 'chain_id', 'initial_height', 'genesis_hash', 'binary_hash', 'spawn_time', 'unbonding_period', 'ccv_timeout_period', 'transfer_timeout_period', 'consumer_redistribution_fraction', 'blocks_per_distribution_transmission', 'historical_entries', 'distribution_transmission_channel')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    GENESIS_HASH_FIELD_NUMBER: _ClassVar[int]
    BINARY_HASH_FIELD_NUMBER: _ClassVar[int]
    SPAWN_TIME_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CCV_TIMEOUT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TIMEOUT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_REDISTRIBUTION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_PER_DISTRIBUTION_TRANSMISSION_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_TRANSMISSION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    chain_id: str
    initial_height: _client_pb2.Height
    genesis_hash: bytes
    binary_hash: bytes
    spawn_time: _timestamp_pb2.Timestamp
    unbonding_period: _duration_pb2.Duration
    ccv_timeout_period: _duration_pb2.Duration
    transfer_timeout_period: _duration_pb2.Duration
    consumer_redistribution_fraction: str
    blocks_per_distribution_transmission: int
    historical_entries: int
    distribution_transmission_channel: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., chain_id: _Optional[str]=..., initial_height: _Optional[_Union[_client_pb2.Height, _Mapping]]=..., genesis_hash: _Optional[bytes]=..., binary_hash: _Optional[bytes]=..., spawn_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., unbonding_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., ccv_timeout_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., transfer_timeout_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., consumer_redistribution_fraction: _Optional[str]=..., blocks_per_distribution_transmission: _Optional[int]=..., historical_entries: _Optional[int]=..., distribution_transmission_channel: _Optional[str]=...) -> None:
        ...

class ConsumerRemovalProposal(_message.Message):
    __slots__ = ('title', 'description', 'chain_id', 'stop_time')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    chain_id: str
    stop_time: _timestamp_pb2.Timestamp

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., chain_id: _Optional[str]=..., stop_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EquivocationProposal(_message.Message):
    __slots__ = ('title', 'description', 'equivocations')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EQUIVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    equivocations: _containers.RepeatedCompositeFieldContainer[_evidence_pb2.Equivocation]

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., equivocations: _Optional[_Iterable[_Union[_evidence_pb2.Equivocation, _Mapping]]]=...) -> None:
        ...

class GlobalSlashEntry(_message.Message):
    __slots__ = ('recv_time', 'consumer_chain_id', 'ibc_seq_num', 'provider_val_cons_addr')
    RECV_TIME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IBC_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VAL_CONS_ADDR_FIELD_NUMBER: _ClassVar[int]
    recv_time: _timestamp_pb2.Timestamp
    consumer_chain_id: str
    ibc_seq_num: int
    provider_val_cons_addr: bytes

    def __init__(self, recv_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., consumer_chain_id: _Optional[str]=..., ibc_seq_num: _Optional[int]=..., provider_val_cons_addr: _Optional[bytes]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ('template_client', 'trusting_period_fraction', 'ccv_timeout_period', 'init_timeout_period', 'vsc_timeout_period', 'slash_meter_replenish_period', 'slash_meter_replenish_fraction', 'max_throttled_packets', 'consumer_reward_denom_registration_fee')
    TEMPLATE_CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRUSTING_PERIOD_FRACTION_FIELD_NUMBER: _ClassVar[int]
    CCV_TIMEOUT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    INIT_TIMEOUT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    VSC_TIMEOUT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SLASH_METER_REPLENISH_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SLASH_METER_REPLENISH_FRACTION_FIELD_NUMBER: _ClassVar[int]
    MAX_THROTTLED_PACKETS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_REWARD_DENOM_REGISTRATION_FEE_FIELD_NUMBER: _ClassVar[int]
    template_client: _tendermint_pb2.ClientState
    trusting_period_fraction: str
    ccv_timeout_period: _duration_pb2.Duration
    init_timeout_period: _duration_pb2.Duration
    vsc_timeout_period: _duration_pb2.Duration
    slash_meter_replenish_period: _duration_pb2.Duration
    slash_meter_replenish_fraction: str
    max_throttled_packets: int
    consumer_reward_denom_registration_fee: _coin_pb2.Coin

    def __init__(self, template_client: _Optional[_Union[_tendermint_pb2.ClientState, _Mapping]]=..., trusting_period_fraction: _Optional[str]=..., ccv_timeout_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., init_timeout_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., vsc_timeout_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., slash_meter_replenish_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., slash_meter_replenish_fraction: _Optional[str]=..., max_throttled_packets: _Optional[int]=..., consumer_reward_denom_registration_fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class HandshakeMetadata(_message.Message):
    __slots__ = ('provider_fee_pool_addr', 'version')
    PROVIDER_FEE_POOL_ADDR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    provider_fee_pool_addr: str
    version: str

    def __init__(self, provider_fee_pool_addr: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class SlashAcks(_message.Message):
    __slots__ = ('addresses',)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, addresses: _Optional[_Iterable[str]]=...) -> None:
        ...

class ConsumerAdditionProposals(_message.Message):
    __slots__ = ('pending',)
    PENDING_FIELD_NUMBER: _ClassVar[int]
    pending: _containers.RepeatedCompositeFieldContainer[ConsumerAdditionProposal]

    def __init__(self, pending: _Optional[_Iterable[_Union[ConsumerAdditionProposal, _Mapping]]]=...) -> None:
        ...

class ConsumerRemovalProposals(_message.Message):
    __slots__ = ('pending',)
    PENDING_FIELD_NUMBER: _ClassVar[int]
    pending: _containers.RepeatedCompositeFieldContainer[ConsumerRemovalProposal]

    def __init__(self, pending: _Optional[_Iterable[_Union[ConsumerRemovalProposal, _Mapping]]]=...) -> None:
        ...

class AddressList(_message.Message):
    __slots__ = ('addresses',)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, addresses: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class ChannelToChain(_message.Message):
    __slots__ = ('channel_id', 'chain_id')
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    chain_id: str

    def __init__(self, channel_id: _Optional[str]=..., chain_id: _Optional[str]=...) -> None:
        ...

class VscUnbondingOps(_message.Message):
    __slots__ = ('vsc_id', 'unbonding_op_ids')
    VSC_ID_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_OP_IDS_FIELD_NUMBER: _ClassVar[int]
    vsc_id: int
    unbonding_op_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, vsc_id: _Optional[int]=..., unbonding_op_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class UnbondingOp(_message.Message):
    __slots__ = ('id', 'unbonding_consumer_chains')
    ID_FIELD_NUMBER: _ClassVar[int]
    UNBONDING_CONSUMER_CHAINS_FIELD_NUMBER: _ClassVar[int]
    id: int
    unbonding_consumer_chains: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[int]=..., unbonding_consumer_chains: _Optional[_Iterable[str]]=...) -> None:
        ...

class InitTimeoutTimestamp(_message.Message):
    __slots__ = ('chain_id', 'timestamp')
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    timestamp: int

    def __init__(self, chain_id: _Optional[str]=..., timestamp: _Optional[int]=...) -> None:
        ...

class VscSendTimestamp(_message.Message):
    __slots__ = ('vsc_id', 'timestamp')
    VSC_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    vsc_id: int
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, vsc_id: _Optional[int]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class KeyAssignmentReplacement(_message.Message):
    __slots__ = ('provider_addr', 'prev_c_key', 'power')
    PROVIDER_ADDR_FIELD_NUMBER: _ClassVar[int]
    PREV_C_KEY_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    provider_addr: bytes
    prev_c_key: _keys_pb2.PublicKey
    power: int

    def __init__(self, provider_addr: _Optional[bytes]=..., prev_c_key: _Optional[_Union[_keys_pb2.PublicKey, _Mapping]]=..., power: _Optional[int]=...) -> None:
        ...

class ValidatorConsumerPubKey(_message.Message):
    __slots__ = ('chain_id', 'provider_addr', 'consumer_key')
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ADDR_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_KEY_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    provider_addr: bytes
    consumer_key: _keys_pb2.PublicKey

    def __init__(self, chain_id: _Optional[str]=..., provider_addr: _Optional[bytes]=..., consumer_key: _Optional[_Union[_keys_pb2.PublicKey, _Mapping]]=...) -> None:
        ...

class ValidatorByConsumerAddr(_message.Message):
    __slots__ = ('chain_id', 'consumer_addr', 'provider_addr')
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ADDR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ADDR_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    consumer_addr: bytes
    provider_addr: bytes

    def __init__(self, chain_id: _Optional[str]=..., consumer_addr: _Optional[bytes]=..., provider_addr: _Optional[bytes]=...) -> None:
        ...

class ConsumerAddrsToPrune(_message.Message):
    __slots__ = ('chain_id', 'vsc_id', 'consumer_addrs')
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VSC_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ADDRS_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    vsc_id: int
    consumer_addrs: AddressList

    def __init__(self, chain_id: _Optional[str]=..., vsc_id: _Optional[int]=..., consumer_addrs: _Optional[_Union[AddressList, _Mapping]]=...) -> None:
        ...
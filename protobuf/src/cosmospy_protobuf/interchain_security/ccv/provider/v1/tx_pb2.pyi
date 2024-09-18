from google.api import annotations_pb2 as _annotations_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class MsgAssignConsumerKey(_message.Message):
    __slots__ = ('chain_id', 'provider_addr', 'consumer_key')
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ADDR_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_KEY_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    provider_addr: str
    consumer_key: str

    def __init__(self, chain_id: _Optional[str]=..., provider_addr: _Optional[str]=..., consumer_key: _Optional[str]=...) -> None:
        ...

class MsgAssignConsumerKeyResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgRegisterConsumerRewardDenom(_message.Message):
    __slots__ = ('denom', 'depositor')
    DENOM_FIELD_NUMBER: _ClassVar[int]
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    denom: str
    depositor: str

    def __init__(self, denom: _Optional[str]=..., depositor: _Optional[str]=...) -> None:
        ...

class MsgRegisterConsumerRewardDenomResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...
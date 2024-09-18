"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,interchain_security/ccv/provider/v1/tx.proto\x12#interchain_security.ccv.provider.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto"s\n\x14MsgAssignConsumerKey\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12)\n\rprovider_addr\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x14\n\x0cconsumer_key\x18\x03 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1e\n\x1cMsgAssignConsumerKeyResponse"L\n\x1eMsgRegisterConsumerRewardDenom\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x11\n\tdepositor\x18\x02 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"(\n&MsgRegisterConsumerRewardDenomResponse2\xcb\x02\n\x03Msg\x12\x91\x01\n\x11AssignConsumerKey\x129.interchain_security.ccv.provider.v1.MsgAssignConsumerKey\x1aA.interchain_security.ccv.provider.v1.MsgAssignConsumerKeyResponse\x12\xaf\x01\n\x1bRegisterConsumerRewardDenom\x12C.interchain_security.ccv.provider.v1.MsgRegisterConsumerRewardDenom\x1aK.interchain_security.ccv.provider.v1.MsgRegisterConsumerRewardDenomResponseB?Z=github.com/cosmos/interchain-security/v2/x/ccv/provider/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'interchain_security.ccv.provider.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cosmos/interchain-security/v2/x/ccv/provider/types'
    _globals['_MSGASSIGNCONSUMERKEY'].fields_by_name['provider_addr']._options = None
    _globals['_MSGASSIGNCONSUMERKEY'].fields_by_name['provider_addr']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_MSGASSIGNCONSUMERKEY']._options = None
    _globals['_MSGASSIGNCONSUMERKEY']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_MSGREGISTERCONSUMERREWARDDENOM']._options = None
    _globals['_MSGREGISTERCONSUMERREWARDDENOM']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_MSGASSIGNCONSUMERKEY']._serialized_start = 191
    _globals['_MSGASSIGNCONSUMERKEY']._serialized_end = 306
    _globals['_MSGASSIGNCONSUMERKEYRESPONSE']._serialized_start = 308
    _globals['_MSGASSIGNCONSUMERKEYRESPONSE']._serialized_end = 338
    _globals['_MSGREGISTERCONSUMERREWARDDENOM']._serialized_start = 340
    _globals['_MSGREGISTERCONSUMERREWARDDENOM']._serialized_end = 416
    _globals['_MSGREGISTERCONSUMERREWARDDENOMRESPONSE']._serialized_start = 418
    _globals['_MSGREGISTERCONSUMERREWARDDENOMRESPONSE']._serialized_end = 458
    _globals['_MSG']._serialized_start = 461
    _globals['_MSG']._serialized_end = 792
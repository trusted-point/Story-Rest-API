"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/nft/v1beta1/tx.proto\x12\x12cosmos.nft.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto"\x8a\x01\n\x07MsgSend\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12(\n\x06sender\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12*\n\x08receiver\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0b\x82\xe7\xb0*\x06sender"\x11\n\x0fMsgSendResponse2V\n\x03Msg\x12H\n\x04Send\x12\x1b.cosmos.nft.v1beta1.MsgSend\x1a#.cosmos.nft.v1beta1.MsgSendResponse\x1a\x05\x80\xe7\xb0*\x01B\x14Z\x12cosmossdk.io/x/nftb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x12cosmossdk.io/x/nft'
    _globals['_MSGSEND'].fields_by_name['sender']._options = None
    _globals['_MSGSEND'].fields_by_name['sender']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGSEND'].fields_by_name['receiver']._options = None
    _globals['_MSGSEND'].fields_by_name['receiver']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGSEND']._options = None
    _globals['_MSGSEND']._serialized_options = b'\x82\xe7\xb0*\x06sender'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGSEND']._serialized_start = 104
    _globals['_MSGSEND']._serialized_end = 242
    _globals['_MSGSENDRESPONSE']._serialized_start = 244
    _globals['_MSGSENDRESPONSE']._serialized_end = 261
    _globals['_MSG']._serialized_start = 263
    _globals['_MSG']._serialized_end = 349
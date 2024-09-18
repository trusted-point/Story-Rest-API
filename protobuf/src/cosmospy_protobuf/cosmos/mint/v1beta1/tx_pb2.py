"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....cosmos.mint.v1beta1 import mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/mint/v1beta1/tx.proto\x12\x13cosmos.mint.v1beta1\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto\x1a\x1ecosmos/mint/v1beta1/mint.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto"\xac\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x06params\x18\x02 \x01(\x0b2\x1b.cosmos.mint.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:4\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/mint/MsgUpdateParams"\x19\n\x17MsgUpdateParamsResponse2p\n\x03Msg\x12b\n\x0cUpdateParams\x12$.cosmos.mint.v1beta1.MsgUpdateParams\x1a,.cosmos.mint.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01B+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
    _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._options = None
    _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._options = None
    _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_MSGUPDATEPARAMS']._options = None
    _globals['_MSGUPDATEPARAMS']._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/mint/MsgUpdateParams'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGUPDATEPARAMS']._serialized_start = 179
    _globals['_MSGUPDATEPARAMS']._serialized_end = 351
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 353
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 378
    _globals['_MSG']._serialized_start = 380
    _globals['_MSG']._serialized_end = 492
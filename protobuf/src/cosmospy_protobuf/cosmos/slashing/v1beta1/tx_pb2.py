"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/slashing/v1beta1/tx.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\x94\x01\n\tMsgUnjail\x12U\n\x0evalidator_addr\x18\x01 \x01(\tB=\xea\xde\x1f\x07address\xd2\xb4-\x1dcosmos.ValidatorAddressString\xa2\xe7\xb0*\x07address\xa8\xe7\xb0*\x01:0\x88\xa0\x1f\x00\x82\xe7\xb0*\x0evalidator_addr\x8a\xe7\xb0*\x14cosmos-sdk/MsgUnjail"\x13\n\x11MsgUnjailResponse"\xb4\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\x06params\x18\x02 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:8\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*%cosmos-sdk/x/slashing/MsgUpdateParams"\x19\n\x17MsgUpdateParamsResponse2\xd2\x01\n\x03Msg\x12X\n\x06Unjail\x12".cosmos.slashing.v1beta1.MsgUnjail\x1a*.cosmos.slashing.v1beta1.MsgUnjailResponse\x12j\n\x0cUpdateParams\x12(.cosmos.slashing.v1beta1.MsgUpdateParams\x1a0.cosmos.slashing.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01B3Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01'
    _globals['_MSGUNJAIL'].fields_by_name['validator_addr']._options = None
    _globals['_MSGUNJAIL'].fields_by_name['validator_addr']._serialized_options = b'\xea\xde\x1f\x07address\xd2\xb4-\x1dcosmos.ValidatorAddressString\xa2\xe7\xb0*\x07address\xa8\xe7\xb0*\x01'
    _globals['_MSGUNJAIL']._options = None
    _globals['_MSGUNJAIL']._serialized_options = b'\x88\xa0\x1f\x00\x82\xe7\xb0*\x0evalidator_addr\x8a\xe7\xb0*\x14cosmos-sdk/MsgUnjail'
    _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._options = None
    _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._options = None
    _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_MSGUPDATEPARAMS']._options = None
    _globals['_MSGUPDATEPARAMS']._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*%cosmos-sdk/x/slashing/MsgUpdateParams'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGUNJAIL']._serialized_start = 195
    _globals['_MSGUNJAIL']._serialized_end = 343
    _globals['_MSGUNJAILRESPONSE']._serialized_start = 345
    _globals['_MSGUNJAILRESPONSE']._serialized_end = 364
    _globals['_MSGUPDATEPARAMS']._serialized_start = 367
    _globals['_MSGUPDATEPARAMS']._serialized_end = 547
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 549
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 574
    _globals['_MSG']._serialized_start = 577
    _globals['_MSG']._serialized_end = 787
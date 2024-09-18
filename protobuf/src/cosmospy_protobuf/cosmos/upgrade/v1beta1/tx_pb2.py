"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/upgrade/v1beta1/tx.proto\x12\x16cosmos.upgrade.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xaa\x01\n\x12MsgSoftwareUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x125\n\x04plan\x18\x02 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.PlanB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:0\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1dcosmos-sdk/MsgSoftwareUpgrade"\x1c\n\x1aMsgSoftwareUpgradeResponse"o\n\x10MsgCancelUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:.\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1bcosmos-sdk/MsgCancelUpgrade"\x1a\n\x18MsgCancelUpgradeResponse2\xec\x01\n\x03Msg\x12q\n\x0fSoftwareUpgrade\x12*.cosmos.upgrade.v1beta1.MsgSoftwareUpgrade\x1a2.cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse\x12k\n\rCancelUpgrade\x12(.cosmos.upgrade.v1beta1.MsgCancelUpgrade\x1a0.cosmos.upgrade.v1beta1.MsgCancelUpgradeResponse\x1a\x05\x80\xe7\xb0*\x01B\x1eZ\x1ccosmossdk.io/x/upgrade/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1ccosmossdk.io/x/upgrade/types'
    _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['authority']._options = None
    _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['plan']._options = None
    _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_MSGSOFTWAREUPGRADE']._options = None
    _globals['_MSGSOFTWAREUPGRADE']._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1dcosmos-sdk/MsgSoftwareUpgrade'
    _globals['_MSGCANCELUPGRADE'].fields_by_name['authority']._options = None
    _globals['_MSGCANCELUPGRADE'].fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCANCELUPGRADE']._options = None
    _globals['_MSGCANCELUPGRADE']._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1bcosmos-sdk/MsgCancelUpgrade'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGSOFTWAREUPGRADE']._serialized_start = 191
    _globals['_MSGSOFTWAREUPGRADE']._serialized_end = 361
    _globals['_MSGSOFTWAREUPGRADERESPONSE']._serialized_start = 363
    _globals['_MSGSOFTWAREUPGRADERESPONSE']._serialized_end = 391
    _globals['_MSGCANCELUPGRADE']._serialized_start = 393
    _globals['_MSGCANCELUPGRADE']._serialized_end = 504
    _globals['_MSGCANCELUPGRADERESPONSE']._serialized_start = 506
    _globals['_MSGCANCELUPGRADERESPONSE']._serialized_end = 532
    _globals['_MSG']._serialized_start = 535
    _globals['_MSG']._serialized_end = 771
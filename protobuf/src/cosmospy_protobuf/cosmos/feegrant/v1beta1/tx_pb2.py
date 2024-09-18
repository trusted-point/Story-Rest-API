"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/feegrant/v1beta1/tx.proto\x12\x17cosmos.feegrant.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xec\x01\n\x11MsgGrantAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12R\n\tallowance\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB)\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI:-\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1ccosmos-sdk/MsgGrantAllowance"\x1b\n\x19MsgGrantAllowanceResponse"\x9a\x01\n\x12MsgRevokeAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:.\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1dcosmos-sdk/MsgRevokeAllowance"\x1c\n\x1aMsgRevokeAllowanceResponse"K\n\x12MsgPruneAllowances\x12(\n\x06pruner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0b\x82\xe7\xb0*\x06pruner"\x1c\n\x1aMsgPruneAllowancesResponse2\xe8\x02\n\x03Msg\x12p\n\x0eGrantAllowance\x12*.cosmos.feegrant.v1beta1.MsgGrantAllowance\x1a2.cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse\x12s\n\x0fRevokeAllowance\x12+.cosmos.feegrant.v1beta1.MsgRevokeAllowance\x1a3.cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponse\x12s\n\x0fPruneAllowances\x12+.cosmos.feegrant.v1beta1.MsgPruneAllowances\x1a3.cosmos.feegrant.v1beta1.MsgPruneAllowancesResponse\x1a\x05\x80\xe7\xb0*\x01B\x19Z\x17cosmossdk.io/x/feegrantb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x17cosmossdk.io/x/feegrant'
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['granter']._options = None
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['grantee']._options = None
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['allowance']._options = None
    _globals['_MSGGRANTALLOWANCE'].fields_by_name['allowance']._serialized_options = b'\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI'
    _globals['_MSGGRANTALLOWANCE']._options = None
    _globals['_MSGGRANTALLOWANCE']._serialized_options = b'\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1ccosmos-sdk/MsgGrantAllowance'
    _globals['_MSGREVOKEALLOWANCE'].fields_by_name['granter']._options = None
    _globals['_MSGREVOKEALLOWANCE'].fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGREVOKEALLOWANCE'].fields_by_name['grantee']._options = None
    _globals['_MSGREVOKEALLOWANCE'].fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGREVOKEALLOWANCE']._options = None
    _globals['_MSGREVOKEALLOWANCE']._serialized_options = b'\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1dcosmos-sdk/MsgRevokeAllowance'
    _globals['_MSGPRUNEALLOWANCES'].fields_by_name['pruner']._options = None
    _globals['_MSGPRUNEALLOWANCES'].fields_by_name['pruner']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGPRUNEALLOWANCES']._options = None
    _globals['_MSGPRUNEALLOWANCES']._serialized_options = b'\x82\xe7\xb0*\x06pruner'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGGRANTALLOWANCE']._serialized_start = 160
    _globals['_MSGGRANTALLOWANCE']._serialized_end = 396
    _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_start = 398
    _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_end = 425
    _globals['_MSGREVOKEALLOWANCE']._serialized_start = 428
    _globals['_MSGREVOKEALLOWANCE']._serialized_end = 582
    _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_start = 584
    _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_end = 612
    _globals['_MSGPRUNEALLOWANCES']._serialized_start = 614
    _globals['_MSGPRUNEALLOWANCES']._serialized_end = 689
    _globals['_MSGPRUNEALLOWANCESRESPONSE']._serialized_start = 691
    _globals['_MSGPRUNEALLOWANCESRESPONSE']._serialized_end = 719
    _globals['_MSG']._serialized_start = 722
    _globals['_MSG']._serialized_end = 1082
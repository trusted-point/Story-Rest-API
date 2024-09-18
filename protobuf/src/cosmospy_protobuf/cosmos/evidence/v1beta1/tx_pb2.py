"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/evidence/v1beta1/tx.proto\x12\x17cosmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xc7\x01\n\x11MsgSubmitEvidence\x12+\n\tsubmitter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12L\n\x08evidence\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB$\xca\xb4- cosmos.evidence.v1beta1.Evidence:7\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tsubmitter\x8a\xe7\xb0*\x1ccosmos-sdk/MsgSubmitEvidence")\n\x19MsgSubmitEvidenceResponse\x12\x0c\n\x04hash\x18\x04 \x01(\x0c2~\n\x03Msg\x12p\n\x0eSubmitEvidence\x12*.cosmos.evidence.v1beta1.MsgSubmitEvidence\x1a2.cosmos.evidence.v1beta1.MsgSubmitEvidenceResponse\x1a\x05\x80\xe7\xb0*\x01B#Z\x1dcosmossdk.io/x/evidence/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1dcosmossdk.io/x/evidence/types\xa8\xe2\x1e\x01'
    _globals['_MSGSUBMITEVIDENCE'].fields_by_name['submitter']._options = None
    _globals['_MSGSUBMITEVIDENCE'].fields_by_name['submitter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGSUBMITEVIDENCE'].fields_by_name['evidence']._options = None
    _globals['_MSGSUBMITEVIDENCE'].fields_by_name['evidence']._serialized_options = b'\xca\xb4- cosmos.evidence.v1beta1.Evidence'
    _globals['_MSGSUBMITEVIDENCE']._options = None
    _globals['_MSGSUBMITEVIDENCE']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tsubmitter\x8a\xe7\xb0*\x1ccosmos-sdk/MsgSubmitEvidence'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGSUBMITEVIDENCE']._serialized_start = 182
    _globals['_MSGSUBMITEVIDENCE']._serialized_end = 381
    _globals['_MSGSUBMITEVIDENCERESPONSE']._serialized_start = 383
    _globals['_MSGSUBMITEVIDENCERESPONSE']._serialized_end = 424
    _globals['_MSG']._serialized_start = 426
    _globals['_MSG']._serialized_end = 552
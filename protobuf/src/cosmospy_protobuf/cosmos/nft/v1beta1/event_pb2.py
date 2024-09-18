"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/nft/v1beta1/event.proto\x12\x12cosmos.nft.v1beta1"K\n\tEventSend\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t"8\n\tEventMint\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t"8\n\tEventBurn\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\tB\x14Z\x12cosmossdk.io/x/nftb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x12cosmossdk.io/x/nft'
    _globals['_EVENTSEND']._serialized_start = 54
    _globals['_EVENTSEND']._serialized_end = 129
    _globals['_EVENTMINT']._serialized_start = 131
    _globals['_EVENTMINT']._serialized_end = 187
    _globals['_EVENTBURN']._serialized_start = 189
    _globals['_EVENTBURN']._serialized_end = 245
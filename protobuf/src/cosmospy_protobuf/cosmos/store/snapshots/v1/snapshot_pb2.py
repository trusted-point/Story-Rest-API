"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cosmos/store/snapshots/v1/snapshot.proto\x12\x19cosmos.store.snapshots.v1\x1a\x14gogoproto/gogo.proto"\x85\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06format\x18\x02 \x01(\r\x12\x0e\n\x06chunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12;\n\x08metadata\x18\x05 \x01(\x0b2#.cosmos.store.snapshots.v1.MetadataB\x04\xc8\xde\x1f\x00" \n\x08Metadata\x12\x14\n\x0cchunk_hashes\x18\x01 \x03(\x0c"\xb5\x02\n\x0cSnapshotItem\x12=\n\x05store\x18\x01 \x01(\x0b2,.cosmos.store.snapshots.v1.SnapshotStoreItemH\x00\x12E\n\x04iavl\x18\x02 \x01(\x0b2+.cosmos.store.snapshots.v1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x12E\n\textension\x18\x03 \x01(\x0b20.cosmos.store.snapshots.v1.SnapshotExtensionMetaH\x00\x12P\n\x11extension_payload\x18\x04 \x01(\x0b23.cosmos.store.snapshots.v1.SnapshotExtensionPayloadH\x00B\x06\n\x04item"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05"5\n\x15SnapshotExtensionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06format\x18\x02 \x01(\r"+\n\x18SnapshotExtensionPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0cB$Z"cosmossdk.io/store/snapshots/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.snapshots.v1.snapshot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z"cosmossdk.io/store/snapshots/types'
    _globals['_SNAPSHOT'].fields_by_name['metadata']._options = None
    _globals['_SNAPSHOT'].fields_by_name['metadata']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SNAPSHOTITEM'].fields_by_name['iavl']._options = None
    _globals['_SNAPSHOTITEM'].fields_by_name['iavl']._serialized_options = b'\xe2\xde\x1f\x04IAVL'
    _globals['_SNAPSHOT']._serialized_start = 94
    _globals['_SNAPSHOT']._serialized_end = 227
    _globals['_METADATA']._serialized_start = 229
    _globals['_METADATA']._serialized_end = 261
    _globals['_SNAPSHOTITEM']._serialized_start = 264
    _globals['_SNAPSHOTITEM']._serialized_end = 573
    _globals['_SNAPSHOTSTOREITEM']._serialized_start = 575
    _globals['_SNAPSHOTSTOREITEM']._serialized_end = 608
    _globals['_SNAPSHOTIAVLITEM']._serialized_start = 610
    _globals['_SNAPSHOTIAVLITEM']._serialized_end = 689
    _globals['_SNAPSHOTEXTENSIONMETA']._serialized_start = 691
    _globals['_SNAPSHOTEXTENSIONMETA']._serialized_end = 744
    _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_start = 746
    _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_end = 789
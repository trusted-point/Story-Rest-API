"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cproofs.proto\x12\x05ics23"g\n\x0eExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b2\r.ics23.LeafOp\x12\x1c\n\x04path\x18\x04 \x03(\x0b2\x0e.ics23.InnerOp"k\n\x11NonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12#\n\x04left\x18\x02 \x01(\x0b2\x15.ics23.ExistenceProof\x12$\n\x05right\x18\x03 \x01(\x0b2\x15.ics23.ExistenceProof"\xc7\x01\n\x0fCommitmentProof\x12&\n\x05exist\x18\x01 \x01(\x0b2\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b2\x18.ics23.NonExistenceProofH\x00\x12"\n\x05batch\x18\x03 \x01(\x0b2\x11.ics23.BatchProofH\x00\x121\n\ncompressed\x18\x04 \x01(\x0b2\x1b.ics23.CompressedBatchProofH\x00B\x07\n\x05proof"\xa0\x01\n\x06LeafOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e2\r.ics23.HashOp\x12"\n\x0bprehash_key\x18\x02 \x01(\x0e2\r.ics23.HashOp\x12$\n\rprehash_value\x18\x03 \x01(\x0e2\r.ics23.HashOp\x12\x1f\n\x06length\x18\x04 \x01(\x0e2\x0f.ics23.LengthOp\x12\x0e\n\x06prefix\x18\x05 \x01(\x0c"F\n\x07InnerOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e2\r.ics23.HashOp\x12\x0e\n\x06prefix\x18\x02 \x01(\x0c\x12\x0e\n\x06suffix\x18\x03 \x01(\x0c"y\n\tProofSpec\x12 \n\tleaf_spec\x18\x01 \x01(\x0b2\r.ics23.LeafOp\x12$\n\ninner_spec\x18\x02 \x01(\x0b2\x10.ics23.InnerSpec\x12\x11\n\tmax_depth\x18\x03 \x01(\x05\x12\x11\n\tmin_depth\x18\x04 \x01(\x05"\x9c\x01\n\tInnerSpec\x12\x13\n\x0bchild_order\x18\x01 \x03(\x05\x12\x12\n\nchild_size\x18\x02 \x01(\x05\x12\x19\n\x11min_prefix_length\x18\x03 \x01(\x05\x12\x19\n\x11max_prefix_length\x18\x04 \x01(\x05\x12\x13\n\x0bempty_child\x18\x05 \x01(\x0c\x12\x1b\n\x04hash\x18\x06 \x01(\x0e2\r.ics23.HashOp"0\n\nBatchProof\x12"\n\x07entries\x18\x01 \x03(\x0b2\x11.ics23.BatchEntry"k\n\nBatchEntry\x12&\n\x05exist\x18\x01 \x01(\x0b2\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b2\x18.ics23.NonExistenceProofH\x00B\x07\n\x05proof"k\n\x14CompressedBatchProof\x12,\n\x07entries\x18\x01 \x03(\x0b2\x1b.ics23.CompressedBatchEntry\x12%\n\rlookup_inners\x18\x02 \x03(\x0b2\x0e.ics23.InnerOp"\x89\x01\n\x14CompressedBatchEntry\x120\n\x05exist\x18\x01 \x01(\x0b2\x1f.ics23.CompressedExistenceProofH\x00\x126\n\x08nonexist\x18\x02 \x01(\x0b2".ics23.CompressedNonExistenceProofH\x00B\x07\n\x05proof"a\n\x18CompressedExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b2\r.ics23.LeafOp\x12\x0c\n\x04path\x18\x04 \x03(\x05"\x89\x01\n\x1bCompressedNonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12-\n\x04left\x18\x02 \x01(\x0b2\x1f.ics23.CompressedExistenceProof\x12.\n\x05right\x18\x03 \x01(\x0b2\x1f.ics23.CompressedExistenceProof*e\n\x06HashOp\x12\x0b\n\x07NO_HASH\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\n\n\x06SHA512\x10\x02\x12\n\n\x06KECCAK\x10\x03\x12\r\n\tRIPEMD160\x10\x04\x12\x0b\n\x07BITCOIN\x10\x05\x12\x0e\n\nSHA512_256\x10\x06*\xab\x01\n\x08LengthOp\x12\r\n\tNO_PREFIX\x10\x00\x12\r\n\tVAR_PROTO\x10\x01\x12\x0b\n\x07VAR_RLP\x10\x02\x12\x0f\n\x0bFIXED32_BIG\x10\x03\x12\x12\n\x0eFIXED32_LITTLE\x10\x04\x12\x0f\n\x0bFIXED64_BIG\x10\x05\x12\x12\n\x0eFIXED64_LITTLE\x10\x06\x12\x14\n\x10REQUIRE_32_BYTES\x10\x07\x12\x14\n\x10REQUIRE_64_BYTES\x10\x08b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proofs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_HASHOP']._serialized_start = 1603
    _globals['_HASHOP']._serialized_end = 1704
    _globals['_LENGTHOP']._serialized_start = 1707
    _globals['_LENGTHOP']._serialized_end = 1878
    _globals['_EXISTENCEPROOF']._serialized_start = 23
    _globals['_EXISTENCEPROOF']._serialized_end = 126
    _globals['_NONEXISTENCEPROOF']._serialized_start = 128
    _globals['_NONEXISTENCEPROOF']._serialized_end = 235
    _globals['_COMMITMENTPROOF']._serialized_start = 238
    _globals['_COMMITMENTPROOF']._serialized_end = 437
    _globals['_LEAFOP']._serialized_start = 440
    _globals['_LEAFOP']._serialized_end = 600
    _globals['_INNEROP']._serialized_start = 602
    _globals['_INNEROP']._serialized_end = 672
    _globals['_PROOFSPEC']._serialized_start = 674
    _globals['_PROOFSPEC']._serialized_end = 795
    _globals['_INNERSPEC']._serialized_start = 798
    _globals['_INNERSPEC']._serialized_end = 954
    _globals['_BATCHPROOF']._serialized_start = 956
    _globals['_BATCHPROOF']._serialized_end = 1004
    _globals['_BATCHENTRY']._serialized_start = 1006
    _globals['_BATCHENTRY']._serialized_end = 1113
    _globals['_COMPRESSEDBATCHPROOF']._serialized_start = 1115
    _globals['_COMPRESSEDBATCHPROOF']._serialized_end = 1222
    _globals['_COMPRESSEDBATCHENTRY']._serialized_start = 1225
    _globals['_COMPRESSEDBATCHENTRY']._serialized_end = 1362
    _globals['_COMPRESSEDEXISTENCEPROOF']._serialized_start = 1364
    _globals['_COMPRESSEDEXISTENCEPROOF']._serialized_end = 1461
    _globals['_COMPRESSEDNONEXISTENCEPROOF']._serialized_start = 1464
    _globals['_COMPRESSEDNONEXISTENCEPROOF']._serialized_end = 1601
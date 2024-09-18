"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.tx.signing.v1beta1 import signing_pb2 as cosmos_dot_tx_dot_signing_dot_v1beta1_dot_signing__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acosmos/tx/v1beta1/tx.proto\x12\x11cosmos.tx.v1beta1\x1a\x11amino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\'cosmos/tx/signing/v1beta1/signing.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto"q\n\x02Tx\x12\'\n\x04body\x18\x01 \x01(\x0b2\x19.cosmos.tx.v1beta1.TxBody\x12.\n\tauth_info\x18\x02 \x01(\x0b2\x1b.cosmos.tx.v1beta1.AuthInfo\x12\x12\n\nsignatures\x18\x03 \x03(\x0c"H\n\x05TxRaw\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0fauth_info_bytes\x18\x02 \x01(\x0c\x12\x12\n\nsignatures\x18\x03 \x03(\x0c"`\n\x07SignDoc\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12\x17\n\x0fauth_info_bytes\x18\x02 \x01(\x0c\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x12\x16\n\x0eaccount_number\x18\x04 \x01(\x04"\xb5\x01\n\x10SignDocDirectAux\x12\x12\n\nbody_bytes\x18\x01 \x01(\x0c\x12(\n\npublic_key\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x10\n\x08chain_id\x18\x03 \x01(\t\x12\x16\n\x0eaccount_number\x18\x04 \x01(\x04\x12\x10\n\x08sequence\x18\x05 \x01(\x04\x12\'\n\x03tip\x18\x06 \x01(\x0b2\x16.cosmos.tx.v1beta1.TipB\x02\x18\x01"\xc7\x01\n\x06TxBody\x12&\n\x08messages\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x16\n\x0etimeout_height\x18\x03 \x01(\x04\x120\n\x11extension_options\x18\xff\x07 \x03(\x0b2\x14.google.protobuf.Any\x12=\n\x1enon_critical_extension_options\x18\xff\x0f \x03(\x0b2\x14.google.protobuf.Any"\x8d\x01\n\x08AuthInfo\x123\n\x0csigner_infos\x18\x01 \x03(\x0b2\x1d.cosmos.tx.v1beta1.SignerInfo\x12#\n\x03fee\x18\x02 \x01(\x0b2\x16.cosmos.tx.v1beta1.Fee\x12\'\n\x03tip\x18\x03 \x01(\x0b2\x16.cosmos.tx.v1beta1.TipB\x02\x18\x01"x\n\nSignerInfo\x12(\n\npublic_key\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12.\n\tmode_info\x18\x02 \x01(\x0b2\x1b.cosmos.tx.v1beta1.ModeInfo\x12\x10\n\x08sequence\x18\x03 \x01(\x04"\xb5\x02\n\x08ModeInfo\x124\n\x06single\x18\x01 \x01(\x0b2".cosmos.tx.v1beta1.ModeInfo.SingleH\x00\x122\n\x05multi\x18\x02 \x01(\x0b2!.cosmos.tx.v1beta1.ModeInfo.MultiH\x00\x1a;\n\x06Single\x121\n\x04mode\x18\x01 \x01(\x0e2#.cosmos.tx.signing.v1beta1.SignMode\x1a{\n\x05Multi\x12A\n\x08bitarray\x18\x01 \x01(\x0b2/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12/\n\nmode_infos\x18\x02 \x03(\x0b2\x1b.cosmos.tx.v1beta1.ModeInfoB\x05\n\x03sum"\xdf\x01\n\x03Fee\x12q\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12\x11\n\tgas_limit\x18\x02 \x01(\x04\x12\'\n\x05payer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07granter\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"\xa6\x01\n\x03Tip\x12q\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12(\n\x06tipper\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x02\x18\x01"\xb1\x01\n\rAuxSignerData\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x125\n\x08sign_doc\x18\x02 \x01(\x0b2#.cosmos.tx.v1beta1.SignDocDirectAux\x121\n\x04mode\x18\x03 \x01(\x0e2#.cosmos.tx.signing.v1beta1.SignMode\x12\x0b\n\x03sig\x18\x04 \x01(\x0cB\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
    _globals['_SIGNDOCDIRECTAUX'].fields_by_name['tip']._options = None
    _globals['_SIGNDOCDIRECTAUX'].fields_by_name['tip']._serialized_options = b'\x18\x01'
    _globals['_AUTHINFO'].fields_by_name['tip']._options = None
    _globals['_AUTHINFO'].fields_by_name['tip']._serialized_options = b'\x18\x01'
    _globals['_FEE'].fields_by_name['amount']._options = None
    _globals['_FEE'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_FEE'].fields_by_name['payer']._options = None
    _globals['_FEE'].fields_by_name['payer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_FEE'].fields_by_name['granter']._options = None
    _globals['_FEE'].fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_TIP'].fields_by_name['amount']._options = None
    _globals['_TIP'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_TIP'].fields_by_name['tipper']._options = None
    _globals['_TIP'].fields_by_name['tipper']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_TIP']._options = None
    _globals['_TIP']._serialized_options = b'\x18\x01'
    _globals['_AUXSIGNERDATA'].fields_by_name['address']._options = None
    _globals['_AUXSIGNERDATA'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_TX']._serialized_start = 264
    _globals['_TX']._serialized_end = 377
    _globals['_TXRAW']._serialized_start = 379
    _globals['_TXRAW']._serialized_end = 451
    _globals['_SIGNDOC']._serialized_start = 453
    _globals['_SIGNDOC']._serialized_end = 549
    _globals['_SIGNDOCDIRECTAUX']._serialized_start = 552
    _globals['_SIGNDOCDIRECTAUX']._serialized_end = 733
    _globals['_TXBODY']._serialized_start = 736
    _globals['_TXBODY']._serialized_end = 935
    _globals['_AUTHINFO']._serialized_start = 938
    _globals['_AUTHINFO']._serialized_end = 1079
    _globals['_SIGNERINFO']._serialized_start = 1081
    _globals['_SIGNERINFO']._serialized_end = 1201
    _globals['_MODEINFO']._serialized_start = 1204
    _globals['_MODEINFO']._serialized_end = 1513
    _globals['_MODEINFO_SINGLE']._serialized_start = 1322
    _globals['_MODEINFO_SINGLE']._serialized_end = 1381
    _globals['_MODEINFO_MULTI']._serialized_start = 1383
    _globals['_MODEINFO_MULTI']._serialized_end = 1506
    _globals['_FEE']._serialized_start = 1516
    _globals['_FEE']._serialized_end = 1739
    _globals['_TIP']._serialized_start = 1742
    _globals['_TIP']._serialized_end = 1908
    _globals['_AUXSIGNERDATA']._serialized_start = 1911
    _globals['_AUXSIGNERDATA']._serialized_end = 2088
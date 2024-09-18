"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.vesting.v1beta1 import vesting_pb2 as cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/vesting/v1beta1/tx.proto\x12\x16cosmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$cosmos/vesting/v1beta1/vesting.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xcb\x02\n\x17MsgCreateVestingAccount\x12.\n\x0cfrom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12q\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12\x10\n\x08end_time\x18\x04 \x01(\x03\x12\x0f\n\x07delayed\x18\x05 \x01(\x08:<\xe8\xa0\x1f\x01\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*"cosmos-sdk/MsgCreateVestingAccount"!\n\x1fMsgCreateVestingAccountResponse"\xaf\x02\n\x1fMsgCreatePermanentLockedAccount\x12-\n\x0cfrom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"from_address"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"to_address"\x12q\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01:?\xe8\xa0\x1f\x01\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*%cosmos-sdk/MsgCreatePermLockedAccount")\n\'MsgCreatePermanentLockedAccountResponse"\xe4\x01\n\x1fMsgCreatePeriodicVestingAccount\x12\x14\n\x0cfrom_address\x18\x01 \x01(\t\x12\x12\n\nto_address\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12B\n\x0fvesting_periods\x18\x04 \x03(\x0b2\x1e.cosmos.vesting.v1beta1.PeriodB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:?\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*%cosmos-sdk/MsgCreatePeriodVestAccount")\n\'MsgCreatePeriodicVestingAccountResponse2\xc5\x03\n\x03Msg\x12\x80\x01\n\x14CreateVestingAccount\x12/.cosmos.vesting.v1beta1.MsgCreateVestingAccount\x1a7.cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse\x12\x98\x01\n\x1cCreatePermanentLockedAccount\x127.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccountResponse\x12\x98\x01\n\x1cCreatePeriodicVestingAccount\x127.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponse\x1a\x05\x80\xe7\xb0*\x01B3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['from_address']._options = None
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['from_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['to_address']._options = None
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['to_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['amount']._options = None
    _globals['_MSGCREATEVESTINGACCOUNT'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_MSGCREATEVESTINGACCOUNT']._options = None
    _globals['_MSGCREATEVESTINGACCOUNT']._serialized_options = b'\xe8\xa0\x1f\x01\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*"cosmos-sdk/MsgCreateVestingAccount'
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['from_address']._options = None
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['from_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"from_address"'
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['to_address']._options = None
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['to_address']._serialized_options = b'\xf2\xde\x1f\x11yaml:"to_address"'
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['amount']._options = None
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT']._options = None
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT']._serialized_options = b'\xe8\xa0\x1f\x01\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*%cosmos-sdk/MsgCreatePermLockedAccount'
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._options = None
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT']._options = None
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT']._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*%cosmos-sdk/MsgCreatePeriodVestAccount'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGCREATEVESTINGACCOUNT']._serialized_start = 223
    _globals['_MSGCREATEVESTINGACCOUNT']._serialized_end = 554
    _globals['_MSGCREATEVESTINGACCOUNTRESPONSE']._serialized_start = 556
    _globals['_MSGCREATEVESTINGACCOUNTRESPONSE']._serialized_end = 589
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT']._serialized_start = 592
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNT']._serialized_end = 895
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE']._serialized_start = 897
    _globals['_MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE']._serialized_end = 938
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT']._serialized_start = 941
    _globals['_MSGCREATEPERIODICVESTINGACCOUNT']._serialized_end = 1169
    _globals['_MSGCREATEPERIODICVESTINGACCOUNTRESPONSE']._serialized_start = 1171
    _globals['_MSGCREATEPERIODICVESTINGACCOUNTRESPONSE']._serialized_end = 1212
    _globals['_MSG']._serialized_start = 1215
    _globals['_MSG']._serialized_end = 1668
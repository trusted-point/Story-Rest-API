"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16cosmos.vesting.v1beta1\x1a\x11amino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto"\x82\x04\n\x12BaseVestingAccount\x12<\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12{\n\x10original_vesting\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12y\n\x0edelegated_free\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12|\n\x11delegated_vesting\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12\x10\n\x08end_time\x18\x05 \x01(\x03:&\x88\xa0\x1f\x00\x8a\xe7\xb0*\x1dcosmos-sdk/BaseVestingAccount"\xac\x01\n\x18ContinuousVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03:,\x88\xa0\x1f\x00\x8a\xe7\xb0*#cosmos-sdk/ContinuousVestingAccount"\x92\x01\n\x15DelayedVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:)\x88\xa0\x1f\x00\x8a\xe7\xb0* cosmos-sdk/DelayedVestingAccount"\x8b\x01\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12q\n\x06amount\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01"\xec\x01\n\x16PeriodicVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12B\n\x0fvesting_periods\x18\x03 \x03(\x0b2\x1e.cosmos.vesting.v1beta1.PeriodB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:*\x88\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PeriodicVestingAccount"\x94\x01\n\x16PermanentLockedAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:*\x88\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PermanentLockedAccountB3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.vesting_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['base_account']._options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['original_vesting']._options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['original_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_free']._options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_free']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_vesting']._options = None
    _globals['_BASEVESTINGACCOUNT'].fields_by_name['delegated_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_BASEVESTINGACCOUNT']._options = None
    _globals['_BASEVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0*\x1dcosmos-sdk/BaseVestingAccount'
    _globals['_CONTINUOUSVESTINGACCOUNT'].fields_by_name['base_vesting_account']._options = None
    _globals['_CONTINUOUSVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_CONTINUOUSVESTINGACCOUNT']._options = None
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0*#cosmos-sdk/ContinuousVestingAccount'
    _globals['_DELAYEDVESTINGACCOUNT'].fields_by_name['base_vesting_account']._options = None
    _globals['_DELAYEDVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_DELAYEDVESTINGACCOUNT']._options = None
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0* cosmos-sdk/DelayedVestingAccount'
    _globals['_PERIOD'].fields_by_name['amount']._options = None
    _globals['_PERIOD'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01'
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['base_vesting_account']._options = None
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._options = None
    _globals['_PERIODICVESTINGACCOUNT'].fields_by_name['vesting_periods']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_PERIODICVESTINGACCOUNT']._options = None
    _globals['_PERIODICVESTINGACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PeriodicVestingAccount'
    _globals['_PERMANENTLOCKEDACCOUNT'].fields_by_name['base_vesting_account']._options = None
    _globals['_PERMANENTLOCKEDACCOUNT'].fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_PERMANENTLOCKEDACCOUNT']._options = None
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_options = b'\x88\xa0\x1f\x00\x8a\xe7\xb0*!cosmos-sdk/PermanentLockedAccount'
    _globals['_BASEVESTINGACCOUNT']._serialized_start = 170
    _globals['_BASEVESTINGACCOUNT']._serialized_end = 684
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_start = 687
    _globals['_CONTINUOUSVESTINGACCOUNT']._serialized_end = 859
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_start = 862
    _globals['_DELAYEDVESTINGACCOUNT']._serialized_end = 1008
    _globals['_PERIOD']._serialized_start = 1011
    _globals['_PERIOD']._serialized_end = 1150
    _globals['_PERIODICVESTINGACCOUNT']._serialized_start = 1153
    _globals['_PERIODICVESTINGACCOUNT']._serialized_end = 1389
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_start = 1392
    _globals['_PERMANENTLOCKEDACCOUNT']._serialized_end = 1540
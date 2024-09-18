"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/autocli/v1/options.proto\x12\x11cosmos.autocli.v1"\x84\x01\n\rModuleOptions\x127\n\x02tx\x18\x01 \x01(\x0b2+.cosmos.autocli.v1.ServiceCommandDescriptor\x12:\n\x05query\x18\x02 \x01(\x0b2+.cosmos.autocli.v1.ServiceCommandDescriptor"\xa3\x02\n\x18ServiceCommandDescriptor\x12\x0f\n\x07service\x18\x01 \x01(\t\x12A\n\x13rpc_command_options\x18\x02 \x03(\x0b2$.cosmos.autocli.v1.RpcCommandOptions\x12R\n\x0csub_commands\x18\x03 \x03(\x0b2<.cosmos.autocli.v1.ServiceCommandDescriptor.SubCommandsEntry\x1a_\n\x10SubCommandsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.cosmos.autocli.v1.ServiceCommandDescriptor:\x028\x01"\x9f\x03\n\x11RpcCommandOptions\x12\x12\n\nrpc_method\x18\x01 \x01(\t\x12\x0b\n\x03use\x18\x02 \x01(\t\x12\x0c\n\x04long\x18\x03 \x01(\t\x12\r\n\x05short\x18\x04 \x01(\t\x12\x0f\n\x07example\x18\x05 \x01(\t\x12\r\n\x05alias\x18\x06 \x03(\t\x12\x13\n\x0bsuggest_for\x18\x07 \x03(\t\x12\x12\n\ndeprecated\x18\x08 \x01(\t\x12\x0f\n\x07version\x18\t \x01(\t\x12K\n\x0cflag_options\x18\n \x03(\x0b25.cosmos.autocli.v1.RpcCommandOptions.FlagOptionsEntry\x12C\n\x0fpositional_args\x18\x0b \x03(\x0b2*.cosmos.autocli.v1.PositionalArgDescriptor\x12\x0c\n\x04skip\x18\x0c \x01(\x08\x1aR\n\x10FlagOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b2\x1e.cosmos.autocli.v1.FlagOptions:\x028\x01"\x96\x01\n\x0bFlagOptions\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tshorthand\x18\x02 \x01(\t\x12\r\n\x05usage\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x04 \x01(\t\x12\x12\n\ndeprecated\x18\x06 \x01(\t\x12\x1c\n\x14shorthand_deprecated\x18\x07 \x01(\t\x12\x0e\n\x06hidden\x18\x08 \x01(\x08"?\n\x17PositionalArgDescriptor\x12\x13\n\x0bproto_field\x18\x01 \x01(\t\x12\x0f\n\x07varargs\x18\x02 \x01(\x08B+Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.autocli.v1.options_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1'
    _globals['_SERVICECOMMANDDESCRIPTOR_SUBCOMMANDSENTRY']._options = None
    _globals['_SERVICECOMMANDDESCRIPTOR_SUBCOMMANDSENTRY']._serialized_options = b'8\x01'
    _globals['_RPCCOMMANDOPTIONS_FLAGOPTIONSENTRY']._options = None
    _globals['_RPCCOMMANDOPTIONS_FLAGOPTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_MODULEOPTIONS']._serialized_start = 55
    _globals['_MODULEOPTIONS']._serialized_end = 187
    _globals['_SERVICECOMMANDDESCRIPTOR']._serialized_start = 190
    _globals['_SERVICECOMMANDDESCRIPTOR']._serialized_end = 481
    _globals['_SERVICECOMMANDDESCRIPTOR_SUBCOMMANDSENTRY']._serialized_start = 386
    _globals['_SERVICECOMMANDDESCRIPTOR_SUBCOMMANDSENTRY']._serialized_end = 481
    _globals['_RPCCOMMANDOPTIONS']._serialized_start = 484
    _globals['_RPCCOMMANDOPTIONS']._serialized_end = 899
    _globals['_RPCCOMMANDOPTIONS_FLAGOPTIONSENTRY']._serialized_start = 817
    _globals['_RPCCOMMANDOPTIONS_FLAGOPTIONSENTRY']._serialized_end = 899
    _globals['_FLAGOPTIONS']._serialized_start = 902
    _globals['_FLAGOPTIONS']._serialized_end = 1052
    _globals['_POSITIONALARGDESCRIPTOR']._serialized_start = 1054
    _globals['_POSITIONALARGDESCRIPTOR']._serialized_end = 1117
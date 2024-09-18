"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19tendermint/p2p/conn.proto\x12\x0etendermint.p2p\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/crypto/keys.proto"\x0c\n\nPacketPing"\x0c\n\nPacketPong"R\n\tPacketMsg\x12!\n\nchannel_id\x18\x01 \x01(\x05B\r\xe2\xde\x1f\tChannelID\x12\x14\n\x03eof\x18\x02 \x01(\x08B\x07\xe2\xde\x1f\x03EOF\x12\x0c\n\x04data\x18\x03 \x01(\x0c"\xa6\x01\n\x06Packet\x121\n\x0bpacket_ping\x18\x01 \x01(\x0b2\x1a.tendermint.p2p.PacketPingH\x00\x121\n\x0bpacket_pong\x18\x02 \x01(\x0b2\x1a.tendermint.p2p.PacketPongH\x00\x12/\n\npacket_msg\x18\x03 \x01(\x0b2\x19.tendermint.p2p.PacketMsgH\x00B\x05\n\x03sum"R\n\x0eAuthSigMessage\x123\n\x07pub_key\x18\x01 \x01(\x0b2\x1c.tendermint.crypto.PublicKeyB\x04\xc8\xde\x1f\x00\x12\x0b\n\x03sig\x18\x02 \x01(\x0cB3Z1github.com/cometbft/cometbft/proto/tendermint/p2pb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.p2p.conn_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cometbft/cometbft/proto/tendermint/p2p'
    _globals['_PACKETMSG'].fields_by_name['channel_id']._options = None
    _globals['_PACKETMSG'].fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _globals['_PACKETMSG'].fields_by_name['eof']._options = None
    _globals['_PACKETMSG'].fields_by_name['eof']._serialized_options = b'\xe2\xde\x1f\x03EOF'
    _globals['_AUTHSIGMESSAGE'].fields_by_name['pub_key']._options = None
    _globals['_AUTHSIGMESSAGE'].fields_by_name['pub_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PACKETPING']._serialized_start = 97
    _globals['_PACKETPING']._serialized_end = 109
    _globals['_PACKETPONG']._serialized_start = 111
    _globals['_PACKETPONG']._serialized_end = 123
    _globals['_PACKETMSG']._serialized_start = 125
    _globals['_PACKETMSG']._serialized_end = 207
    _globals['_PACKET']._serialized_start = 210
    _globals['_PACKET']._serialized_end = 376
    _globals['_AUTHSIGMESSAGE']._serialized_start = 378
    _globals['_AUTHSIGMESSAGE']._serialized_end = 460
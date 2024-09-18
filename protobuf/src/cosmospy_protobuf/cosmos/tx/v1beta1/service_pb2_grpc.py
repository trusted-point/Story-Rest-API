"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.tx.v1beta1 import service_pb2 as cosmos_dot_tx_dot_v1beta1_dot_service__pb2

class ServiceStub(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Simulate = channel.unary_unary('/cosmos.tx.v1beta1.Service/Simulate', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.FromString)
        self.GetTx = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetTx', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.FromString)
        self.BroadcastTx = channel.unary_unary('/cosmos.tx.v1beta1.Service/BroadcastTx', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.FromString)
        self.GetTxsEvent = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetTxsEvent', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.FromString)
        self.GetBlockWithTxs = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetBlockWithTxs', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.FromString)
        self.TxDecode = channel.unary_unary('/cosmos.tx.v1beta1.Service/TxDecode', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeResponse.FromString)
        self.TxEncode = channel.unary_unary('/cosmos.tx.v1beta1.Service/TxEncode', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeResponse.FromString)
        self.TxEncodeAmino = channel.unary_unary('/cosmos.tx.v1beta1.Service/TxEncodeAmino', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoResponse.FromString)
        self.TxDecodeAmino = channel.unary_unary('/cosmos.tx.v1beta1.Service/TxDecodeAmino', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoResponse.FromString)

class ServiceServicer(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    def Simulate(self, request, context):
        """Simulate simulates executing a transaction for estimating gas usage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTx(self, request, context):
        """GetTx fetches a tx by hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastTx(self, request, context):
        """BroadcastTx broadcast transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTxsEvent(self, request, context):
        """GetTxsEvent fetches txs by event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockWithTxs(self, request, context):
        """GetBlockWithTxs fetches a block with decoded txs.

        Since: cosmos-sdk 0.45.2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TxDecode(self, request, context):
        """TxDecode decodes the transaction.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TxEncode(self, request, context):
        """TxEncode encodes the transaction.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TxEncodeAmino(self, request, context):
        """TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TxDecodeAmino(self, request, context):
        """TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Simulate': grpc.unary_unary_rpc_method_handler(servicer.Simulate, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.SerializeToString), 'GetTx': grpc.unary_unary_rpc_method_handler(servicer.GetTx, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.SerializeToString), 'BroadcastTx': grpc.unary_unary_rpc_method_handler(servicer.BroadcastTx, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.SerializeToString), 'GetTxsEvent': grpc.unary_unary_rpc_method_handler(servicer.GetTxsEvent, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.SerializeToString), 'GetBlockWithTxs': grpc.unary_unary_rpc_method_handler(servicer.GetBlockWithTxs, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.SerializeToString), 'TxDecode': grpc.unary_unary_rpc_method_handler(servicer.TxDecode, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeResponse.SerializeToString), 'TxEncode': grpc.unary_unary_rpc_method_handler(servicer.TxEncode, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeResponse.SerializeToString), 'TxEncodeAmino': grpc.unary_unary_rpc_method_handler(servicer.TxEncodeAmino, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoResponse.SerializeToString), 'TxDecodeAmino': grpc.unary_unary_rpc_method_handler(servicer.TxDecodeAmino, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.tx.v1beta1.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    @staticmethod
    def Simulate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/Simulate', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetTx', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BroadcastTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/BroadcastTx', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTxsEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetTxsEvent', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockWithTxs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetBlockWithTxs', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TxDecode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/TxDecode', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TxEncode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/TxEncode', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TxEncodeAmino(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/TxEncodeAmino', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxEncodeAminoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TxDecodeAmino(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/TxDecodeAmino', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.TxDecodeAminoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
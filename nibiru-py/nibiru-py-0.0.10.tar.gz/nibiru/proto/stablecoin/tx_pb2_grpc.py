# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from stablecoin import tx_pb2 as stablecoin_dot_tx__pb2


class MsgStub(object):
    """Msg defines the x/stablecoin Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MintStable = channel.unary_unary(
                '/nibiru.stablecoin.v1.Msg/MintStable',
                request_serializer=stablecoin_dot_tx__pb2.MsgMintStable.SerializeToString,
                response_deserializer=stablecoin_dot_tx__pb2.MsgMintStableResponse.FromString,
                )
        self.BurnStable = channel.unary_unary(
                '/nibiru.stablecoin.v1.Msg/BurnStable',
                request_serializer=stablecoin_dot_tx__pb2.MsgBurnStable.SerializeToString,
                response_deserializer=stablecoin_dot_tx__pb2.MsgBurnStableResponse.FromString,
                )
        self.Recollateralize = channel.unary_unary(
                '/nibiru.stablecoin.v1.Msg/Recollateralize',
                request_serializer=stablecoin_dot_tx__pb2.MsgRecollateralize.SerializeToString,
                response_deserializer=stablecoin_dot_tx__pb2.MsgRecollateralizeResponse.FromString,
                )
        self.Buyback = channel.unary_unary(
                '/nibiru.stablecoin.v1.Msg/Buyback',
                request_serializer=stablecoin_dot_tx__pb2.MsgBuyback.SerializeToString,
                response_deserializer=stablecoin_dot_tx__pb2.MsgBuybackResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the x/stablecoin Msg service.
    """

    def MintStable(self, request, context):
        """MintStable defines a method for trading a mixture of GOV and COLL to mint an 
        equivalent value of stablecoins. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BurnStable(self, request, context):
        """BurnStable defines a method for redeeming/burning stablecoins to receive an 
        equivalent value as a mixture of governance and collateral tokens. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recollateralize(self, request, context):
        """Recollateralize defines a method for manually adding collateral to the 
        protocol in exchange for an equivalent stablecoin value in governance tokens 
        plus a small bonus. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Buyback(self, request, context):
        """Buyback defines a method for manually adding NIBI to the protocol 
        in exchange for an equivalent stablecoin value in collateral, effectively 
        executing a share buyback for Nibiru Chain. The NIBI purchased by the protocol 
        is then burned, distributing value to all NIBI hodlers. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MintStable': grpc.unary_unary_rpc_method_handler(
                    servicer.MintStable,
                    request_deserializer=stablecoin_dot_tx__pb2.MsgMintStable.FromString,
                    response_serializer=stablecoin_dot_tx__pb2.MsgMintStableResponse.SerializeToString,
            ),
            'BurnStable': grpc.unary_unary_rpc_method_handler(
                    servicer.BurnStable,
                    request_deserializer=stablecoin_dot_tx__pb2.MsgBurnStable.FromString,
                    response_serializer=stablecoin_dot_tx__pb2.MsgBurnStableResponse.SerializeToString,
            ),
            'Recollateralize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recollateralize,
                    request_deserializer=stablecoin_dot_tx__pb2.MsgRecollateralize.FromString,
                    response_serializer=stablecoin_dot_tx__pb2.MsgRecollateralizeResponse.SerializeToString,
            ),
            'Buyback': grpc.unary_unary_rpc_method_handler(
                    servicer.Buyback,
                    request_deserializer=stablecoin_dot_tx__pb2.MsgBuyback.FromString,
                    response_serializer=stablecoin_dot_tx__pb2.MsgBuybackResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.stablecoin.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the x/stablecoin Msg service.
    """

    @staticmethod
    def MintStable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.stablecoin.v1.Msg/MintStable',
            stablecoin_dot_tx__pb2.MsgMintStable.SerializeToString,
            stablecoin_dot_tx__pb2.MsgMintStableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BurnStable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.stablecoin.v1.Msg/BurnStable',
            stablecoin_dot_tx__pb2.MsgBurnStable.SerializeToString,
            stablecoin_dot_tx__pb2.MsgBurnStableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recollateralize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.stablecoin.v1.Msg/Recollateralize',
            stablecoin_dot_tx__pb2.MsgRecollateralize.SerializeToString,
            stablecoin_dot_tx__pb2.MsgRecollateralizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Buyback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.stablecoin.v1.Msg/Buyback',
            stablecoin_dot_tx__pb2.MsgBuyback.SerializeToString,
            stablecoin_dot_tx__pb2.MsgBuybackResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

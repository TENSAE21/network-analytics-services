# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import network_analytics_util_pb2 as network__analytics__util__pb2


class NetowrkAnalyticsStub(object):
  """/// End Bipartite graph

  /// Network Analytics Services

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MinNodeGraph = channel.unary_unary(
        '/NetowrkAnalytics/MinNodeGraph',
        request_serializer=network__analytics__util__pb2.MinNodeGraphRequest.SerializeToString,
        response_deserializer=network__analytics__util__pb2.MinNodeGraphResponse.FromString,
        )
    self.MostImportantGraph = channel.unary_unary(
        '/NetowrkAnalytics/MostImportantGraph',
        request_serializer=network__analytics__util__pb2.MostImportantGraphRequest.SerializeToString,
        response_deserializer=network__analytics__util__pb2.MostImportantGraphResponse.FromString,
        )


class NetowrkAnalyticsServicer(object):
  """/// End Bipartite graph

  /// Network Analytics Services

  """

  def MinNodeGraph(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MostImportantGraph(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetowrkAnalyticsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MinNodeGraph': grpc.unary_unary_rpc_method_handler(
          servicer.MinNodeGraph,
          request_deserializer=network__analytics__util__pb2.MinNodeGraphRequest.FromString,
          response_serializer=network__analytics__util__pb2.MinNodeGraphResponse.SerializeToString,
      ),
      'MostImportantGraph': grpc.unary_unary_rpc_method_handler(
          servicer.MostImportantGraph,
          request_deserializer=network__analytics__util__pb2.MostImportantGraphRequest.FromString,
          response_serializer=network__analytics__util__pb2.MostImportantGraphResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NetowrkAnalytics', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

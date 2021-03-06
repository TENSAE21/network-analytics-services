# Tested on python3.6

import logging
import time

import grpc

import network_analytics_util_pb2
import network_analytics_util_pb2_grpc
from google.protobuf.json_format import MessageToJson, Parse

import subprocess
import yaml


def test_1():#Check MinNodesToRemove
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_util_pb2_grpc.NetowrkAnalyticsStub(channel)

    graph = {
        "nodes": ['1','2','3','4','5','6'],
        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['4','6']]
        }
    source_node = '1'
    target_node = '6'
     
    edges_req = []
    for e in graph["edges"]:
        edges_req.append(network_analytics_util_pb2.Edge(edge=e))

    graph_in = network_analytics_util_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

    graph_1 = network_analytics_util_pb2.MinNodeGraphRequest(graph=graph_in,source_node=source_node,target_node=target_node)

    response = stub.MinNodeGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.nodes_output)
    print(response.edges_output)

def test_2():#Check MostImportantNodes
    channel = grpc.insecure_channel('localhost:5000')
    stub = network_analytics_util_pb2_grpc.NetowrkAnalyticsStub(channel)

    graph = {
        "nodes": ['1','2','3','4','5','6','7','8'],
        "edges": [['1','2'],['1','4'],['2','3'],['2','5'],['3','4'],['3','6'],['2','7'],['3','8']],
        "weights": [3,4,5,6,7,8,9,10]
    }
    source_nodes = ['5','7']
    target_nodes = ['6']

     
    edges_req = []
    for e in graph["edges"]:
        edges_req.append(network_analytics_util_pb2.Edge(edge=e))

    if('weights' in graph):
        graph_in = network_analytics_util_pb2.Graph(nodes=graph["nodes"],edges=edges_req, weights=graph['weights'])
    else:    
        graph_in = network_analytics_util_pb2.Graph(nodes=graph["nodes"],edges=edges_req)


    graph_1 = network_analytics_util_pb2.MostImportantGraphRequest(graph=graph_in,source_nodes=source_nodes,target_nodes=target_nodes,Type=1)

    response = stub.MostImportantGraph(graph_1)
    print(response.status)
    print(response.message)
    print(response.node_betweenness_centrality)
    print(response.edge_betweenness_centrality)




if __name__ == '__main__':

    # generate_call_credentials()
     test_1()
     test_2()
 

from __future__ import print_function
import logging

import grpc

# import helloworld_pb2
# import helloworld_pb2_grpc
import memory_pb2
import memory_pb2_grpc

import profiler_pb2
import profiler_pb2_grpc


import numpy as np
from matplotlib import pyplot as plt


import socketserver
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:42195') as channel:
        profiler_stub = profiler_pb2_grpc.ProfilerServiceStub(channel)
        beg = profiler_pb2.BeginSessionRequest(device_id=123,pid=28828)
        profile_session = profiler_stub.BeginSession(beg)
        #
        stub = memory_pb2_grpc.MemoryServiceStub(channel)
        response1 = stub.StartMonitoringApp(memory_pb2.MemoryStartRequest(session=profile_session.session))
        memData = stub.GetData(memory_pb2.MemoryRequest(session=profile_session.session,start_time=0,end_time=9223372036854775807))

    memResult = memData.mem_samples
    java_mem_list = []

    native_mem_list = []
    stack_mem_list = []
    code_mem_list = []
    others_mem_list = []
    total_mem_list = []
    index_list = []
    for index,value in enumerate(memResult):

        print("Greeter client received: " + str())
        java_mem_list.append(value.memory_usage.java_mem)
        native_mem_list.append(value.memory_usage.native_mem)
        stack_mem_list.append(value.memory_usage.stack_mem)
        code_mem_list.append(value.memory_usage.code_mem)
        others_mem_list.append(value.memory_usage.others_mem)
        total_mem_list.append(value.memory_usage.total_mem)
        index_list.append(index)
    print(java_mem_list)
    plt.plot(index_list, java_mem_list)
    # plt.plot(index_list, native_mem_list)
    # plt.plot(index_list, stack_mem_list)
    # plt.plot(index_list, code_mem_list)
    # plt.plot(index_list, others_mem_list)
    # plt.plot(index_list, total_mem_list)
    print(memDatae
    print(len(memResult))
    plt.show()

if __name__ == '__main__':
    logging.basicConfig()
    run()

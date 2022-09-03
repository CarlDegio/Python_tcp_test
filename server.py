
import socket
import struct

def tcp_recv_server():
    """服务端接收数据"""
    # 创建tcp套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定信息
    tcp_server.bind(('127.0.0.1', 10001))
    # 将主动转被动(服务器提供连接服务时需要)
    tcp_server.listen(128)
    # 等待连接(接到连接后,会创建一个连接副本,然后返回连接到此端口的主机信息)
    new_tcp, host_info = tcp_server.accept()
    # 接收数据
    package = new_tcp.recv(1024)
    print(str(package,'utf-8'))
    print(host_info)


def tcp_send_server():
    """服务端发送数据"""
    # 创建tcp套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定信息
    tcp_server.bind(('127.0.0.1', 10050))
    # 将主动转被动(服务器提供连接服务时需要)
    tcp_server.listen(128)
    # 等待连接(接到连接后,会创建一个连接副本,然后返回连接到此端口的主机信息)
    new_tcp, host_info = tcp_server.accept()
    # 发送数据
    data = struct.pack('i4d',2022,*[1.2,2.3,3.4,4.5])
    new_tcp.send(data)


if __name__ == '__main__':
    tcp_recv_server()
    #tcp_send_server()
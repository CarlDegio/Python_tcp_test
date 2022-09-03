import socket
import struct

def tcp_send_client():
    """使用tcp发送数据"""
    # 创建tcp套接字
    tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(('127.0.0.1', 10001))
    # 发送数据
    cmd_args="calibrateGripper()"
    tcp_socket.sendall(bytes(cmd_args,"utf-8"))
    # 断开连接
    tcp_socket.close()

def tcp_recv_client():
    """使用tcp接收数据"""
    # 创建TCP套接字
    tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(('127.0.0.1', 10001))
    # 接收数据
    package = tcp_socket.recv(40)
    magic_num, x, y, z, angle = struct.unpack('i4d', package)
    # 打印数据
    print(magic_num, x, y, z, angle)
    # 断开连接
    tcp_socket.close()

if __name__ == '__main__':
    tcp_send_client()
    #tcp_recv_client()
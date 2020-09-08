# coding=utf-8
#author：kingving time:2020/5/13

import socket

#1、创建socket对象
sk=socket.socket()
#客户端不需要设置IP地址和端口号，IP地址就是设备的IP地址，端口号由系统分配一个空闲的端口号
#2、发起连接(连接服务端的后台）
sk.connect(('127.0.0.1',13000))

#23、、发送数据到服务端
sk.sendall(input('>>>').encode('utf8'))

#4、接收服务端发过来的数据
server_Data=sk.recv(1024)#内部需要有字节大写，超过1024字节，需要用循环接收
print(server_Data.decode('utf8'))








# coding=utf-8
#author：kingving time:2020/5/15

'''
网络通信三大要素
IP地址、端口号、传输协议
http协议都是建立在TCP协议之上的
'''

'''
服务器的端口和IP地址都是不能改变的，要在本地设置好（永恒不变）
客户端的端口和IP地址都是可以改变的（可以改变）
'''

'''
要先启动服务器
请求是客户端先发送请求给服务器，上报客户端的IP地址和端口
服务器接收上报信息后回应客户端
'''


'''

字符串是不能直接在网络上传播的，需要转成bytes类型，才能被pycharm理解

'''

'''
流程：

服务器：
1、服务器创建socket对象socket.socket()
2、绑定ip地址和端口 sk.bind()
3、监听客户端的请求数据sk.listen()
4、等待客户端连接（连接之前服务器处于阻塞状态）conn，adrr，sk.accpet()
5、服务器接收客户端的数据 -----客户端数据=conn.recv(1024)，打印时要解码
6、处理数据，发送数据给客户端---conn.sendall,要编码

客户端：
1、客户端创建socket对象socket.socket()
2、创建连接服务器的端口和ip地址 sk.connect()
3、发送数据给服务端sk.sendall 打印时需要编码
4、接收服务器传过来的数据---服务器数据conn.recv(1024),处理时要解码

'''

# 服务器：
import socket

sk=socket.socket
sk.bind(('0.0.0.0',13000))
sk.listen()
print('服务器启动')
conn,adrr=sk.accept()
print('客户端的地址',addr)
clent_data=sk.recv(1024)
print(clent_data.decode('utf8'))
send_Data=input('>>>')
conn.sendall(input('>>>').encode('utf8'))

#客户端：
sk=socket.socket
sk.connect(('127.0.0.1',13000))
sk.sendall(input('>>>').encode('utf8'))
severdata=sk.recv(1024).decode('utf8')
print(severdata)














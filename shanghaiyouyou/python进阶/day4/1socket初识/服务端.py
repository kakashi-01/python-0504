# coding=utf-8
#author：kingving time:2020/5/13

import socket

#1、创建socket对象
sk=socket.socket()

#2、绑定IP地址和端口号（13000） 通过bind函数来绑定，用元组来传参
sk.bind(('0.0.0.0',13000))

#3、监听，有没有请求发送过来
sk.listen()
print('服务端启动了')

#4、等待传入连接，连接成功之前，是阻塞状态的（当没人找你办业务时，是阻塞状态的）
#5、连接成功之后，解除阻塞，返回一个新的socket对象和客户端的IP地址
conn,addr=sk.accept() #conn是新的socket对象,addr是客户端主动上报的IP地址和端口号
print('客户端的地址',addr)

#6、服务端接收数据（来自客户端发过来的数据）
#   在接收到数据之前，会处于阻塞状态
client_Data=conn.recv(1024)
print(client_Data.decode('utf8'))#需要将字符串转成bytes形式

#7、处理数据--忽略
send_Data=input('>>>')

#8、发送数据（发送一个键盘输入，发给客户端）
conn.sendall((send_Data.encode('utf8')))














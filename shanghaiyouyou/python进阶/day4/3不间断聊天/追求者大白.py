# coding=utf-8
#author：kingving time:2020/5/20

import socket

sk=socket.socket()

sk.connect(('127.0.0.1',13001))
print('大白上线了')

while True:

    #向女神发送数据
    data='大白:'+ input('>>>')
    sk.sendall(data.encode('utf8'))

    #接收数据
    data=sk.recv(1024)
    print(data.decode('utf8'))


sk = socket.socket()
sk.connect(("127.0.0.1", 13000))
print("大白上线了...")

while True:
    # 向女神发送数据
    data = "大白：" + input(">>>")
    sk.sendall(data.encode("utf8"))

    # 接受数据
    data = sk.recv(1024)
    print(data.decode("utf8"))
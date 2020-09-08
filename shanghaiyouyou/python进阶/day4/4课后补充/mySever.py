# coding=utf-8
#author：kingving time:2020/5/20

import socket

sk=socket.socket()
sk.bind(('127.0.0.1',13008))
sk.listen()

while True:
    #等待传入连接

    conn,addr=sk.accept()

    #接收数据
    data=conn.recv(1024)

    print(data.decode('utf8'))

    #发送数据
    html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>妮妮baby</p>
</body>
</html>    
    
"""
    #返回
    # b"HTTP/1/1 200 OK\r\n%s" %html.encode('utf8')
    conn.sendall(("HTTP/1/1 200 OK\r\n%s" %html).encode('utf8'))
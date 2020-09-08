# coding=utf-8
#author：kingving time:2020/5/18

import socket
import os

def post_file(sk_obj, file_path):
    '''
    发送文件
    :param sk_obj:socket对象
    :param file_path:文件路径
    :return: None
    '''

    # 发送文件大小
    file_size = os.stat(file_path).st_size  # 获取文件大小,得到的是int，需要转成str
    file_size = str(file_size)  # 将int转成str
    file_size = file_size.encode('utf8')  # 将str转成bytes
    sk_obj.sendall(file_size)
    sk_obj.recv(1024)

    # 发送文件名称
    sk_obj.sendall(os.path.split(file_path)[1].encode("utf8"))
    sk_obj.recv(1024)

    # 发送文件内容
    file_size = os.stat(file_path).st_size #重新获取，得到int
    with open(file_path, 'rb')as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size = file_size - 1024

#创建socket对象
sk=socket.socket()

#发起连接
sk.connect(('127.0.0.1',13000))

post_file(sk, '/python进阶/day4/2文件上传/客户端/qq.png')

#释放资源
sk.close()
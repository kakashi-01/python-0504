# coding=utf-8
# author：kingving time:2020/5/18

import os
import socket

# D:\QQ\untitled\untitled\python进阶\day4\2文件上传\客户端\qq.png#使用os.path.split 切割成文件夹和文件名

def get_file(sk_obj):
    '''
    接受文件
    :param sk_obj:socket对象
    :return: None
    '''

    # 接受文件大小
    file_size = int(sk_obj.recv(1024).decode('utf8'))  # 将bytes转成str
    sk_obj.sendall(b'ok')

    # 接受文件名称
    file_name = sk_obj.recv(1024).decode('utf8')
    sk_obj.sendall(b'ok')

    # 接受文件内容
    with open('qq.png', 'wb') as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size = file_size - 1024


#创建socket对象
sk=socket.socket()
#绑定IP地址和端口号
sk.bind(('127.0.0.1',13000))
#监听
sk.listen()
#等待传入连接
conn,addr=sk.accept()

get_file(conn)

#释放资源
conn.close()
sk.close()


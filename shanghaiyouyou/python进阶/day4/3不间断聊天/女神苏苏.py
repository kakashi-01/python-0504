# coding=utf-8
#author：kingving time:2020/5/20


import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('有人和女神聊天了')

        while True:
            #接收数据
            client_data=self.request.recv(1024) #相当于之前的conn.recv()，来接收数据的

            print(client_data.decode('utf8'))

            #发送数据

            self.request.sendall(input('>>>').encode('utf8'))

server= socketserver.ThreadingTCPServer(('127.0.0.1',13005),MyServer)

print('女神上线了，并且发了一张自拍，说自己很无聊.......')

server.serve_forever()
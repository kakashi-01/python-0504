# coding=utf-8
#author：kingving time:2020/5/14

import threading
import time

def foo():
    time.sleep(3)
    print('阳光明媚')

t1=threading.Thread(target=foo)
t1.start()

t1.join()  #在线程t1结束之前阻塞住主线程，不让继续往下运行

print('主线程最后一行代码')

print('最后的最后')
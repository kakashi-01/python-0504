# coding=utf-8
#author：kingving time:2020/5/14

import threading
import time

lockA=threading.Lock() #面试官的锁
lockB=threading.Lock() #小明的锁

#面试官的函数

def foo1():
    lockA.acquire() #面试官上锁
    print('请解释什么是死锁')
    time.sleep(1)

    lockB.acquire() #小明上锁
    print('请求面试官发offer')
    time.sleep(1)

    lockA.release() #释放锁
    lockB.release() #释放锁

#小明的函数
def foo2():
    lockB.acquire() #小明上锁
    print('请给我offer')
    time.sleep(1)

    lockA.acquire() #面试官上锁
    print('解释什么是死锁')
    time.sleep(1)

    lockA.release()  # 释放锁
    lockB.release()  # 释放锁

t1=threading.Thread(target=foo1)
t2=threading.Thread(target=foo2)

t1.start()
t2.start()


#----死锁会阻塞，运行不下去----
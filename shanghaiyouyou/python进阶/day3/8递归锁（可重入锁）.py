# coding=utf-8
#author：kingving time:2020/5/14

import threading
import time

# lockA=threading.Lock() #面试官的锁
# lockB=threading.Lock() #小明的锁
lockR=threading.RLock() #递归锁

'''
递归锁内部维护着一把锁和一个计数器
每次上锁，计数器加一
每次解锁，计数器减一
计数器可以大于零，也可以等于零，也不可以小于零

'''



#面试官的函数

def foo1():
    lockR.acquire() #面试官上锁
    print('请解释什么是死锁')
    time.sleep(1)

    lockR.acquire() #小明上锁
    print('请求面试官发offer')
    time.sleep(1)

    lockR.release() #释放锁
    lockR.release() #释放锁

#小明的函数
def foo2():
    lockR.acquire() #小明上锁
    print('请给我offer')
    time.sleep(1)

    lockR.acquire() #面试官上锁
    print('解释什么是死锁')
    time.sleep(1)

    lockR.release()  # 释放锁
    lockR.release()  # 释放锁

t1=threading.Thread(target=foo1)
t2=threading.Thread(target=foo2)

t1.start()
t2.start()


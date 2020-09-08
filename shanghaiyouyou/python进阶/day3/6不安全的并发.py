# coding=utf-8
#author：kingving time:2020/5/14

import threading
import time

balance=500 #账户余额
r=threading.Lock() #声明一把锁

'''

这是一把同步锁
同步锁必须上锁与解锁相对
如果上锁之后不解锁，再次上锁，代码会阻塞，反之如果解锁之后不上锁，再次解锁，那么代码会报错

'''



#操作账户余额
def foo(num):
    #1、申明全局变量    如果需要修改全局变量就要申明一下全局变量global，如果不需要就不需要这一步
    global balance

    r.acquire()#上锁

    #2、将接口取到的值存进自己的系统变量中
    user_balance=balance

    time.sleep(1) #防止代码太少，cpu执行速度太快造成串行

    #3、计算出结果
    user_balance=user_balance+num

    #4、将结果通过接口传递出来
    balance=user_balance

    r.release()#解锁

#消费300元

t1=threading.Thread(target=foo,args=[-300])
#收入10000元

t2=threading.Thread(target=foo,args=[10000])

#启动线程
t1.start()
t2.start()

#阻塞主线程
t1.join()
t2.join()

print('最终余额：',balance)
# coding=utf-8
#author：kingving time:2020/5/13

import threading
import time

def foo():
    num=0
    for i in range(1000000):
        num+=1

begin_Time=time.time()


'''
#并发  总消耗时长 0.15561318397521973  因为额外付出了切换的时间，所以时间比串行更长

t1=threading.Thread(target=foo)
t2=threading.Thread(target=foo)

t1.start()
t2.start()

t1.join()
t2.join()
'''


'''
#串行 总消耗时长 0.07181525230407715

foo()
foo()
'''

end_Time=time.time()
print('总消耗时长',end_Time-begin_Time)
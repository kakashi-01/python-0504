# coding=utf-8
#author：kingving time:2020/5/11

import threading
import time

''' 1 串行的时间
def foo(something):
    print(something)
    time.sleep(1)

begin_Time=time.time()
foo('磁盘写入100M数据')
foo('CPU去做其他事情')


end_Time=time.time()

print('总消耗市场',end_Time-begin_Time)  #串行的时间2.000243663787842秒

'''

'''
 2并行的时间 0.0009975433349609375秒
def foo(something):
    print(something)
    time.sleep(1)

begin_Time = time.time()

#创建线程实例
t1=threading.Thread(target=foo,args=('磁盘写入100M数据',))
t2=threading.Thread(target=foo,args=('CPU去做其他事情',))

#启动线程
t1.start()
t2.start()

end_Time=time.time()
print('总消耗时长',end_Time-begin_Time)  #并行的时间
'''

'''
3 并发 总消耗时长： 1.0012900829315186秒  加入join后，设置阻塞，必须完成所有的join后，再来完成主线程
def foo(something):
    print(something)
    time.sleep(1)

begin_Time = time.time()

#创建线程实例
t1=threading.Thread(target=foo,args=('磁盘写入100M数据',))
t2=threading.Thread(target=foo,args=('CPU去做其他事情',))

#启动线程
t1.start()
t2.start()

#join的作用：在子线程完成运行之前，这个主线程将一直被阻塞
t1.join()
t2.join()

end_Time=time.time()
print('总消耗时长',end_Time-begin_Time,'秒')  #

'''
#coding=utf-8
#author:Kingving time:2020/6/23 0:07

a=0 #false
b=1 #true
if a and b: #两个都为真，才成立
    print('hello')
else:
    print('hehe')

if a or b: #1个为真，就成立
    print('hello')
else:
    print('hehe')

if not a: # a是false，not a 就是真
    print('hello')
else:
    print('hehe')
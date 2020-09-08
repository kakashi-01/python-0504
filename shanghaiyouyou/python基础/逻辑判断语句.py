#coding=utf-8
#author:Kingving time:2020/6/20 21:28

'''if循环

age= 30
if age>20:
    print('hello world')

elif age<5:
    print('hehe')

else:
    print('end!')
'''
'''for循环

a='hello world'
for i in a:
    print(i)
'''

"""input和if的嵌套，特别注意input打印出来的是str，需要转为int
i=int(input('请输入数字：'))
print(i)
if i>19:
    print("ues")
"""

'''for循环
n='hello world'
for i in n:
    print(i)


l=['he','12',12,'hello','22']
for i in l:
    print(i)
'''

'''range用法
s=0
for i in list(range(10)):#range(1,100,2)起点，终点，步长，左含右不含
    s+=i
print(s)

x=list(range(100))
print(x)
'''


'''while语句循环'''
a=0
while 1: #恒真，死循环
    a+=1
    if a>10:
        break
print(a)

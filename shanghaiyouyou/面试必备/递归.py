#coding=utf-8
#author:Kingving time:2020/6/18 2:03

"""斐波那契数列"""
#0,1,1,2,3,5,8,13，前两者之和等于第三个数

a=0
b=1
c=a+b
d=b+c
s=[]

while b<100:
    # print(b)
    s.append(b)
    a,b=b,a+b


print(s)
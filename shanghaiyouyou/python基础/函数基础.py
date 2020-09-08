#coding=utf-8
#author:Kingving time:2020/6/29 1:20


# 求和
a=[1,3,5,7]

s=0

for i in a:
    s+=i
print(s)
#直接使用sum()也可以
c=sum(a) #内建函数
print(c)

#定义函数
def qiuhe(a=[]):
    s=0
    for i in a:
        s=s+i
    print(s)
    return s
b=qiuhe(a)
print(b)
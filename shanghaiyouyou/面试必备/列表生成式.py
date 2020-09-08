#coding=utf-8
#author:Kingving time:2020/6/18 1:59

"""要获取1，-2,3，-4,5，-6....-100并且求和"""

a=range(1,101)#可迭代对象
print(list(a))#转化成列表

b=[x for x in range(1,101)]
print(b)

c=[x*((-1)**(x+1)) for x in range(1,101)]#根据位数来获取列表
print(c)

print(sum(c))#求和
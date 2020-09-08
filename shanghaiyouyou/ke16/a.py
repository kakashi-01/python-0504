#coding=utf-8
#author:Kingving time:2020/7/21 23:05


#快速生成列表  [1,4,9.....,81]  1的平方到9的平方的列表
a=[i*i for i in range(1,10)]
print(a)



#生成器
b=(i*i for i in range(1,10))
print(b)  #generator object  可以节省内存
print(next(b))  #用到几个取几个
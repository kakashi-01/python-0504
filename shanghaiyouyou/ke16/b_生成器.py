#coding=utf-8
#author:Kingving time:2020/7/21 23:09

def func(a=10):
    while True:
        a=a+2
        print('a的值：%s'%a)
        yield a+10   #相当于return   在这里已经结束了

        print('下次取值：***********')  #这里不会取值了




b=func(a=10)  #generator object  生成器:一次一次取值
# print(b)
# print(next(b))
# print(next(b))
# print(next(b))

for i in range (10):
    print(next(b))
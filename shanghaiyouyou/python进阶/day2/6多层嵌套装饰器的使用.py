# coding=utf-8
#author：kingving time:2020/5/12
#--------------多个装饰器同时出现扩展知识----------------

def bar1(func):
    def inner1():
        func()
        print(1)
    return inner1

def bar2(func):
    def inner2():
        func()
        print(2)
    return inner2

def bar3(func):
    def inner3():
        func()
        print(3)
    return inner3

@bar3  # 调用的inner3，装饰inner2
@bar2  # 调用的inner2，装饰inner1
@bar1  # 调用的inner1，装饰foo函数
def foo():
    print('我是foo')
foo()
# coding=utf-8
#author：kingving time:2020/5/12

def bar(func):
    def inner(something,a,b,c,d):
        func(something,a,b,c,d)
        #此处是装饰器为函数新增的功能
        print('学会了一些神奇的知识')
    return inner
@bar
def foo(something,a,b,c,d):
    print('正在某事:',something)

foo('看电视',1,2,3,4)


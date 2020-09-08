# coding=utf-8
#author：kingving time:2020/5/12


def foo():
    print('我是一个函数')

'''
a=1
b=a
所以b=1了
1、函数名可用赋值给其它变量
b=foo
print(foo)
print(b)
b()
'''

'''
def test(a):
    a()
#2、函数名作为参数传递，所以test（foo）就是foo(),输出的就是'我是一个函数'
test(foo)
'''


def bar():
    print('我是bar函数')

    def inner():
        print('我是inner函数')
    #3、函数名作为返回值
    return inner
a=bar()#我是bar函数,输出的是bar()的返回值，同时返回值赋值给inner,此时a=inner，所以下面a()实际上时调用的inner()
a()#我是inner函数


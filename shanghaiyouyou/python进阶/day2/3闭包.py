# coding=utf-8
#author：kingving time:2020/5/12


#在一个内部函数里边，对在外部作用域(不能是全局作用域也不能是内置作用域)的变量进行调用
#那么这个内部函数就被称之为闭包
def outer():
    x=10

    def inner():
        print(x)

    return inner

outer()()#outer()相当于inner,再加一个(),等于inner()---方法1

#方法2，由方法1拆分
a=outer()#a=inner
a()#inner()
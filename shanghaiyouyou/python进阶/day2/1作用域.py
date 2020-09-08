# coding=utf-8
#author：kingving time:2020/5/11

'''
作用域是程序运行时，变量可被访问的范围
定义在函数内的变量是局部变量
定义在模块最外层的变量是全局变量
一般都是从里向外寻找去找作用域
'''
#B（builtins)pycharm内置作用域
g='全局作用域'#G(global）全局作用域,仅该py文件中可用，其它py文件不能用

def foo():
    print(g)

    def foo1():
        print(g)

        def foo2():
            print(g)

#L(Local):局部作用域
def ha():
    c=1
    def foo():
        a ='hello world'#E(enclosing)嵌套作用域

        def bar():
            b='hello python'#L(Local):局部作用域
        print(a)
print(set   )
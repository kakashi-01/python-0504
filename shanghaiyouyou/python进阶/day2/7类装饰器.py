# coding=utf-8
#author：kingving time:2020/5/12

'''
类当中有3个成员：字段(__init__(self)、方法(@staticmethod和@classmethod)、属性(@property)
成员1：字段
1、普通字段，保存在对象里边，执行的时候只能通过对象调用
2、静态字段，保存在类里边，执行的时候既可以通过对象调用，也可以通过类直接调用
'''
# class Foo:
#     name:'这是静态字段'
#
#     def __init__(self):
#         self.age='普通字段'
#
# obj1=Foo()
# obj2=Foo()
# print(obj1.age)
'''
成员2：方法
1）普通方法，保存在类里边，由对象调用
2）静态方法，保存在类里边，可以通过类调用，也可以通过对象调用
3）类  方法，保存在类里边，可以通过类调用，也可以通过对象调用
'''
class Foo:
    def foo(self):
        print('普通方法')

    @staticmethod
    def foo2():
        print('静态方法')

    @classmethod
    def foo3(cls):
        print('类方法')

# 类方法，保存在类里边，由类直接调用，无需实例化类
Foo.foo3()
#静态方法，保存在类里边，由类直接调用，无需实例化类
Foo.foo2()
#普通方法，保存在类里边，只能由对象调用
obj=Foo()
obj.foo()

'''
成员3:属性 就是不加括号也能执行的方法
定义时，在普通方法上加一个装饰器
定义时，属性只能有一个self参数
调用的时候，不用加括号
    方法的调用形式：obj.func()
    属性的调用形式：obj.func
'''
class Foo:
    @property #属性
    def foo2(self):
        print('这是属性')

    @foo2.setter
    def foo2(self,values):
        print('伪装赋值:',values)

    @foo2.deleter
    def foo2(self):
        print('伪装删除')

obj=Foo()
#自动执行@property 装饰的foo2方法并获取返回值
print(obj.foo2)
#自动执行@foo2.setter 装饰的方法，并将'123'赋值给values
obj.foo2='123'
#自动执行 @foo2.deleter 修饰的方法

# class Foo:
#
#     @classmethod #把函数变成类方法，保存在类当中的，由类直接调用
#     def foo(cls):
#         print(123)
#
# FOO.foo()
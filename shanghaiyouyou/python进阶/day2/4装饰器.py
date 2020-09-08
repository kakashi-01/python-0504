# coding=utf-8
#author：kingving time:2020/5/12

# 1、直接修改foo函数---会影响源代码功能实现，方案不通过
# 2、重新写一个函数，实现foo函数功能的同时增加新功能
# 开放封闭原则：允许扩展现有的功能代码，但是禁止修改已有功能代码

def bar(func):
    def inner():
        func()
        #此处省略一系列神仙操作
        print('成功利用摄像头捕捉到用户视网膜映射的手机壳颜色')
        print('成功调整UI界面主题')
    return inner

# bar(foo) #高阶函数，函数名作为参数，foo函数作为参数直接给bar函数调用

@bar   #等同于 foo=bar(foo)
def foo():
    #此处省略三个字
    print('事情干完了')

#这中间可能还有几百行代码，
# if foo()==bar(foo)
# foo=bar(foo)
foo()#等于是inner










#coding=utf-8
#author:Kingving time:2020/6/29 1:58

#不带参数的函数
'''
def add():
    """
    描述这个函数实现的是什么功能
    :return: 返回什么内容
    """
    print('没有返回值')
    # return 'hello'

r=add() #返回print里的内容，并不是函数返回的内容
print(r) #None
'''
#带参数的函数

def abc(a,b):
    """

    :param a:
    :param b:
    :return:
    """
    return a+b
r=abc(a='hello',b='world')
print(r)



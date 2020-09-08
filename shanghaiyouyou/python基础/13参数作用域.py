#coding=utf-8
#author:Kingving time:2020/7/12 23:19


class People(object):

    n=2
#初始化，实例化
    def __init__(self):
        self.c=3
        d=4 #局部参数
        print(d)

    def hands(self,a,b):
        e='hello'
        self.g='world'
        print('有两只手，可以吃饭')
        print('n的值  ：%s'%self.n) #只能通过self实例化调用
        return a+b


    def foots(self):
        print('c的值：%s'%self.c)
        print('两只脚，可以走路')

    def get_g(self):
        print('g的值：%s'%self.g)

aa=People()
print(aa.n)
print(aa.hands('1','a'))
aa.get_g()
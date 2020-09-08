#coding=utf-8
#author:Kingving time:2020/7/12 20:32

class People(object):

    def __init__(self,age='18',name='xiaohua'):

        #构造函数,初始化，一般将公共的方法放在这里

        self.age=age #属性
        self.name=name
        print('实例化的时候，自动执行__init__内容')


    def hands(self):
        self.a='hello' #参数
        print('有两只手，可以吃饭')


    def foots(self):
        print('我的名字是：%s'%self.name)
        print('两只脚，可以走路')

#实例化
xiaohua=People()
a=xiaohua.age
print(a)
xiaohua.age=20
print(xiaohua.age)

xiaohua.name='zhangsan' #改变属性
xiaohua.foots()

#加其他属性
xiaohua.token='qweeeeeee'
print(xiaohua.token)


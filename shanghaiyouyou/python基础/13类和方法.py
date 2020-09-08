#coding=utf-8
#author:Kingving time:2020/7/12 20:20

class People(object):

    def hands(self):
        print('有两只手，可以吃饭')


    def foots(self):
        print('两只脚，可以走路')

    def chifan(self):
        self.hands()# self类本身的一个实例参数
        print('吃饭咯')

#实例化
xiaohua=People()
# print(xiaohua.hands())
# print(xiaohua.foots())
xiaohua.chifan()

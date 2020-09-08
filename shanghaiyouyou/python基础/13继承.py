#coding=utf-8
#author:Kingving time:2020/7/12 20:26

class Father():

    def __init__(self):
        self.name='father'
        self.age=50
        self.waihao='lao wang'

    def fangzi(self):
        print('父亲的房子')

    def chezi(self):
        print('父亲的车子')

class Mother():

    def gongsi(self):
        print('母亲开的公司')


#子类继承父类，相当于把父类的方法直接继承过来
class Son(Father,Mother):

    def __init__(self):
        super().__init__()# 要用到父类里的属性
        self.age=20
        self.name='son'
        self.gexing='新增的个性'

    def cunkuan(self):
        print('儿子自己的存款')

    def fangzi(self):  #当子类的方法和父类方法同样，就直接覆盖了父类
        print('自己推翻了，重新盖')


s=Son()
print(s.age)
print(s.name)
print(s.waihao)
print(s.gexing)
s.fangzi()
s.chezi()
s.gongsi()
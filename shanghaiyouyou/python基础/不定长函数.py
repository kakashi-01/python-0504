#coding=utf-8
#author:Kingving time:2020/6/29 2:13

#两个*可以传不定长的参数，一个*就可以传1个或2个参数的

def func(**kwargs):
    print('不定长参数:%s'%kwargs)

h={
    'a1':"abc",
    'b1':'sada',
    'c1':'eeqqweq'
}

func(**h) #以字典的方式传入

def printinfo(*args,**kwargs):
    print('传入的参数:%s' %str(args))

printinfo(3,4)
#coding=utf-8
#author:Kingving time:2020/6/26 1:38

'''
python数据类型：None,bool,int,float,str,list,tuple,dict

'''
a=None
print(a) #None
print(type(a))#type函数，查看数据类型

b=1
print(type(b))#int

c=1.02
print(type(c)) #float

d='helo world!'
print(type(d))#str

e='123' #str
print(type(e))

f=[1,2,3,4,5,None,'hejwe'] #list
print(type(f))
print(f.append('wkeow'))
print(f)


g=(32,[132,43242,43],'123',None) #tuple
print(g[0])
print(type(g))

h={'key1':'value1','key2':'value2'} #dict
print(type(h))
#查询值
print(h['key1'])
#改变key对应的值
h['key1']='1value'
print(h)
#新增键值对
h['new']='new1'
print(h)
#删除
del h['key1']
print(h)
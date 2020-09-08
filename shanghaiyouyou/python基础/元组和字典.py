#coding=utf-8
#author:Kingving time:2020/6/23 0:31

#元祖（），只能读，不能增删改查

#可以相加
a=(1,2)
b=(3,4)
print(a+b)


#字典{}，是无序的,由键值对组成，查询key得到值,value可以是字符串，int，list，tuple,key不能重复
c={"a":'123',"b":'456','c':[1,2,3],'d':(1,2)}
print(c['c'])
print(c.keys()) #查询所有的keys
print(c.values())#查询所有的values
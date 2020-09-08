# coding=utf-8
#author：kingving time:2020/5/10

a='abc'
b=b'abc'

print(a,type(a))#str类型
print(b,type(b))#字节类型，不能加汉字


# str和bytes互转
a='自君之出矣，不复理残机'
b=a.encode('gbk')#把str转成bytes
print(b)

b.decode('gbk')#把Bytes类型转成str
c=b.decode('gbk')
print(c)
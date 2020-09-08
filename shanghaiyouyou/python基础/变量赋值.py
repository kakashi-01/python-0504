#coding=utf-8
#author:Kingving time:2020/6/22 21:44


#赋值
a=1
print(type(a))
a=1.1
print(type(a))
a='hfuifhi'
print(type(a))
b=[1,3,5,7]
print(type(b))
print(b)

#列表求和
c=[1,2,3,4,5,6,7,8,9,10]
s=0
for i in c:
    s=s+i
    # print('第%s次循环'%i)
print(s)

#多个变量赋值
a=b=c=1
print(a,b,c)

d,e,f=4,5,6
print(d,e,f)


#浮点数+int
a=10.22222222
b=5
print(a+b)
print(int(a+b))

#字符串 可以相加 也可以相乘
a='hello'
b='wolrd'
print(a+b)
print(a*3)


#字符串的切片
a='helloworld'
#取前五个
print(a[0:5]) #左含右不含，第五位取不到
print(a[:5]) #从0开始取 前面可以不加0
print(a[5:])#从第五位开始取，一直到最后
print(a[::-1])#反着取
print(a[5:3:-1])#反着数
print(a[5])# 只取一个
print(len(a))# 计算字符串长度，空格也属于一个长度
print(a[2:5:2])#加入步长的概念
print(a.count('o'))#统计某个字符串出现的次数



#布尔类型：非0为真，0为假，None，空字符串也为假
a=0
b=''
c=None
print(bool(a))
print(bool(b))
print(bool(c))

d=1
print(bool(a<d)) #比较a和d的关系是否成立，成立为真，不成立为假
print(bool(a==d))#等于关系是否成立
print(bool(a!=d))#不等于关系

f=a>d #false
print(f)

g=a==d #false
print(g)
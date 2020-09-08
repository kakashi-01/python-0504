#coding=utf-8
#author:Kingving time:2020/6/23 0:13


#新增一个数据
a=[1,3,4,5,6]
a.append(10) #加在尾部
print(a)

#删除一个数据（通过下标删除）
del a[4] #删除的是下标
print(a)

#删除一个数据（指定数据删除）
a.remove(4)
print(a)

#删除一个数据（弹出最后一个删除,默认最后一个，根据下标来弹出）
b=a.pop()
print(a)

#弹出倒数第二个
c=a.pop(-2)
print(a)


#修改，先通过下标修改对应数据，再打印列表
a[0]=0
print(a)


#列表排序
n=[1,11,3,45,25]
n.sort() #正排序，从小到大
print(n)

print(n[::-1]) #反向排序，从大到小
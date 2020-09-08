# -*- coding: utf-8 -*-
# @Author   : 'Kakashi'
# @Date     : 2020-05-15

# 冒泡排序：
a=[1,3,10,9,21,35,4,6]
s=range(1,len(a))[::-1]
print(list(s))
for i in a:
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    print("第%s轮交换后数据:%s" %(len(s)-j+1,a))
print(a)

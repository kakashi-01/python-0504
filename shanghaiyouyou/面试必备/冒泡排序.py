#coding=utf-8
#author:Kingving time:2020/6/15 1:02

li=[1,2,10,9,21,35,46]
s=range(len(li))[::-1] #次数 分为多轮交换
print (s)
for i in s:
    for j in range(i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
print(li)

#或者用li.sort()
#coding=utf-8
#author:Kingving time:2020/7/8 23:43


# 问题1：对列表a中的数字从小到大排序
# 问题2 排序后去除重复的数字
list1=[1,6,8,11,9,1,8,6,8,7,8]
# s=range(len(list1))[::-1] #次数 分为多轮交换
# # print (s)
# for i in s:
#     for j in range(i):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)
#
# del list1[1]
#
# print(list1)


#set集合去重
print(list(set(list1)))   #去重 然后排序


#排序(不改变原始的序列）
b=sorted(list1)
print(list1)
print(b)


#改变原始的序列
list1.sort()
print(list1)
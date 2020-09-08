#coding=utf-8
#author:Kingving time:2020/6/22 0:40

'''
送命题：

如果一个list是一组打乱的数字

List1 = [3, 2, 1, 9, 10, 78,6]

那么问题来了：如何用python去冒泡排序呢？
'''

list1=[3, 2, 1, 9, 10, 78,6]
# s=range(len(list1))[::-1] #次数 分为多轮交换
# print (s)
# for i in s:
#     for j in range(i):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)

for i in range(6,-1,-1):
    for j in range(i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)



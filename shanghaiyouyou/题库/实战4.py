#coding=utf-8
#author:Kingving time:2020/7/27 0:23

'''给定一个数组奇数为是升序，偶数位是降序，（如：1，8，3，6，5，4，7，2）如何让其升序变成（1，2，3，4，5，6，7，8）;'''

a=[1,8,3,6,5,4,7,2]
s=range(len(a) - 1)
print(s)
for i in range(len(a) - 1):
    for j in range(len(a) - 1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)


def Sort_Func(a):
    # 拆分成奇数位序列和偶数位序列，偶数位序列倒置
    result = [a[i] for i in range(len(a)) if i % 2 == 0]
    temp_lst = [a[i] for i in range(len(a)) if i % 2 == 1][::-1]
    # 设置游标j
    j = 0
    # 将偶数位的序列插入结果表;
    for i in range(len(temp_lst)):
        while result[j] < temp_lst[i] and j < len(result) - 1:
            if result[j + 1] > temp_lst[i]:
                break
            j += 1
        # 找到坐标插入后，j向右移动
        result.insert(j + 1, temp_lst[i])
        j += 1
    return result


a1 = [1, 8, 3, 6, 5, 4, 7, 2]
a2 = [1, 80, 3, 60, 5, 40, 7, 20]

print(Sort_Func(a1))
print(Sort_Func(a2))

import random
# 定义冒泡排序函数
def bubble_sort(data):
    for i in range(len(data) - 1):# 外循环每一次使得有序的数增加一个
        indicator = False # 用于优化（没有交换时表示已经有序，结束循环）
        for j in range(len(data) - 1 - i):#内循环每次讲无序部分中的最大值放到最上面
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                indicator = True
        if not indicator:#如果没有交换说明列表已经有序，结束循环
            break
# 验证算法正确性
data = list(range(10))#产生一个有序列表
random.shuffle(data) # 调用shuffle函数打乱顺序
print(data)# 排序前
bubble_sort(data)# 调用冒泡排序算法
print(data)#排序后

a=[1,8,3,6,5,4,7,2]
s=range(len(a))[::-1]
for i in s:
    for j in range(i):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
b=a[::-1]
print(b)
#coding=utf-8
#author:Kingving time:2020/7/26 17:40

'''
1. 给定一个数组和数字k，使用k去滑动比较数组的k个数字中最大值，打印输出如：
[1,2,3,4,45,3,2,3,4,75,2]
滑动窗口k=3
滑动窗口取值分别为[1,2,3],[2,3,4],[3,4,45],[4,45,3].....
打印输出 3,4,45,45....'''

def max_k_size(nums,k):
    #result记录结果
    result=[]
    #index记录按数值大小排序的nums元素下标
    index=[]
    #对列表中的前k个元素进行排序，确保index[0]对应的的nums[index[0]]是前k个元素中最大的
    for i in range(k):
        #index不为空的场景，新元素比nums[index[-1]]大，将index中的坐标值弹出
        while len(index)>0 and nums[i]>nums[index[-1]]:
            index.pop()
        index.append(i)
        print("index:",index)
    #前k个元素的取一次最大值
    result.append(nums[index[0]])
    #滑块开始滑动，每次滑动1
    for i in range(k,len(nums)):
        #如果index[0]记录的坐标值已经超出了滑块所在的范围，就弹出
        if index[0]<i-k+1:
            index.pop(0)
        #如果新元素值大于nums[index[-1]]，弹出index的最后一个元素；否则的话压入新的nums坐标值i
        while len(index)>0 and nums[i]>nums[index[-1]]:
            index.pop()
        index.append(i)
        #每次滑块向右移动的同时，取一次滑块内部的最大值，即nums[index[0]]
        result.append(nums[index[0]])
    return result

nums=[1,2,3,4,45,3,2,3,4,75,2]
print(max_k_size(nums,3))
#coding=utf-8
#author:Kingving time:2020/7/20 22:30

# python作业9：
# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到： [3, 5, 1, 7]
#使用insert()函数，将指定对象插入列表的指定位置
l = [1, 3, 5, 7]
l.insert(3,1)  #(index,obj)
print(l[1:])



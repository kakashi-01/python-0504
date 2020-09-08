#coding=utf-8
#author:Kingving time:2020/6/18 1:19

"""切片操作"""

a='axbyczdj' #取‘abcd’

#使用切片
print(a[0::2]) #从0位开始取，步长为2

#取‘ab'
print(a[0:4:2]) #从0位开始取，取到第四位结束，步长为2，（大于0，小于4），左含右不含[0:4)

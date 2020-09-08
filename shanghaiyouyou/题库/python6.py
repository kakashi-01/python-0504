#coding=utf-8
#author:Kingving time:2020/7/19 17:42
'''
python作业6-如何判断一个数组是对称数组：要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a",  0, "2", 0, "a", 1]'''

x=[1,'a',0,2,0,'a',1]

if x[::-1]==x:
    print('true')

else:
    print('false')
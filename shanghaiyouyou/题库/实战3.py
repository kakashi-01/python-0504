#coding=utf-8
#author:Kingving time:2020/7/27 0:13

'''给定字符串“2-2*2-7/7+2”输出结果，如果字符串中包含空格和其他字符怎么办？'''



def func(a):
    a = list(filter(lambda x : x in "0123456789+-*/",a))
    a = "".join(a)
    return eval(a)
a="2-2*2-7/7+2"
print(func(a))
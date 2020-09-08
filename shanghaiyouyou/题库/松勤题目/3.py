#coding=utf-8
#author:Kingving time:2020/7/5 23:44

"""3、下面的列表里面包含了一些字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]

请用while 循环 写一段代码打印其中所有包含ok的字符串元素"""

#利用下标和列表长度去取值
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
i=0
length=len(info)
while i<length:
    if 'ok' in info[i]:
        print(info[i])
    i=i+1
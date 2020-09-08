#coding=utf-8
#author:Kingving time:2020/7/19 17:47

'''python作业8：
有一个数据list of dict如下
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]
写入到本地一个txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
yoyo3,123456'''


a=[{"yoyo1":"123456"},
{"yoyo2":"123456"},
{"yoyo3":"123456"},
]

# fileDir = 'e:\\ttt.txt'
# fo = open(fileDir,'w')
# for one in range(1,101):
#     info = f'yoyo{one},123456'
#     fo.write(info+'\n')
#
#
# fo.close()

fileDir = 'e:\\11111.txt'
# f = open(fileDir,'rb')

for i in a:
    for j,k in i.items():
        with open(fileDir,'a')as f:
            f.write(f'{j},{k}\n')
            f.flush()
            f.close()


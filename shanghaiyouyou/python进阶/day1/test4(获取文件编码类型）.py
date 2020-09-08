# coding=utf-8
#author：kingving time:2020/5/10


import chardet

#获取文件编码类型
def get_encoding(file):
    #二进制的方式，读取文件数据
    with open(file,'rb')as f:
        data=f.read()
        return chardet.detect(data)

enData=get_encoding('qq.png')
enData1=get_encoding('a.txt')
print(enData1)
# coding=utf-8
#author：kingving time:2020/5/10

'''
下载附件cfiles.zip（见附件cfiles.zip）

解压该压缩包，里面
包含了两个文件。 一个叫
'gbk编码.txt',
该文件是gbk编码的。
另一个文件叫
'utf8编码.txt', 该文件是utf8编码的。
两个文件里面的内容都包含中文。

要求大家编写一个python程序，该程序做到以下2点

1.
将两个文件内容读出， 合并内容到一个字符串中，
并能用print语句将合并后的内容正确显示

2.
然后，程序用中文提示用户“请输入
新文件的名称”，
用户输入文件名可以包含中文
将上面合并后的内容存储到一个新文件中，以utf8格式编码。
新文件的文件名就是上面用户输入的名字。
'''

#答案
# 根据不同的编码格式，指定参数
with open(r'C:\Users\dell\Desktop\python进阶测试-作业1-字符编码集-task07\cfiles\gbk编码.txt',encoding='gbk') as f1,\
     open(r'C:\Users\dell\Desktop\python进阶测试-作业1-字符编码集-task07\cfiles\utf8编码.txt',encoding='utf8') as f2:

    # read后，自动转化成unicode
    content1 = f1.read()
    content2 = f2.read()

    newContent = content1 + content2
    print(newContent)

newFile = input('请输入新文件的名称:')

with open(newFile,'w',encoding='utf8') as f:
    f.write(newContent)

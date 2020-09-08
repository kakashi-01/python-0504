# coding=utf-8
#author：kingving time:2020/5/10

# with open('./a.txt',"w",encoding='gb2312')as f:   不仅仅用gb2312，可以用其它的但是得保证编码和解码保持一致才可以
#     f.write('五花马，千金裘，呼儿将出换美酒')
#
# with open('./a.txt','r',encoding='gb2312')as f:
#     data=f.read()
#     print(data)

with open('qq.png', 'rb')as f:#rb以2进制读，wb以2进制写,当不需要理解文件的内容时，使用rb和wb，
# 如果需要理解文件内容，使用r，w，此时需要编码成str
    data=f.read()

with open('妮妮发的.png', 'wb')as f:#通过这种方法可以做图片剪切，拷贝，重命名的操作
    f.write(data)


with open('b.txt', 'wb')as f:
    f.write(b'abc')
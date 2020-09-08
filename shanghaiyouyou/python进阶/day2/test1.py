# coding=utf-8
#author：kingving time:2020/5/10
'''

总结：
如果想要知道程序是否运行成功，使用os.system，判断他的退出码ret==0（成功）or==1（不成功）
如果想要拿到程序的运行结果，存到python变量当中，需要使用subprocess.cheek_output！

'''
import os

#相当于打开操作系统的shell，敲入一串命令
#阻塞式调用：调用的外部程序没有退出时，python程序会一直停在这里
#直到调用的外部程序退出，代码才接着往下执行
os.system('ipconfig')
os.system('mspaint')
ret=os.system('for %i in (1,2,10) do @echo %i')
# print('after')
print('ret=',ret)

#ret=0,证明调用的程序运行成功，ret=1，证明调用的程序运行不成功

'''
os.system('cp f1 f2')
if ret==0:
   大功告成
else：
    bug,预案措施
'''
#-----------------------------------------------------------------------------------------------

import subprocess

#执行一个指定的命令，并将结果以字节字符串的形式返回

# out=subprocess.check_output('ipconfig')#需要赋值给一个变量
# # print(out)
# print(out.decode('gbk'))#转成中文
# print('结果')

'''
说明subprocess也是属于阻塞式调用,执行结果不会直接打印出来需要赋值，打印的内容时字节字符串，需要用gbk转码
out=subprocess.check_output('mspaint')
print('执行结果',out.decode('gbk'))

'''
# -----------------------------------------------------------------------------------------------
import subprocess
from subprocess import Popen,PIPE
import time

#Popen属于class,属于非阻塞式调用
#输出重定向
child = subprocess.Popen(
    'ipconfig',
    stdout=subprocess.PIPE,
)

output,err=child.communicate()
print(output)
time.sleep(1)


#输入重定向
child=subprocess.Popen(
    'python ioTest.py',
    stdin=PIPE,
    encoding='gbk'
)
output,err=child.communicate('胡\n何')
print(output)
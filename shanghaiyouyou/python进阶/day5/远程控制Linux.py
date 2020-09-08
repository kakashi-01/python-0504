# coding=utf-8
#author：kingving time:2020/5/19

import paramiko

#创建ssh对象
ssh=paramiko.SSHClient()

#连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#远程真机IP地址，端口号(默认22），在远程主机已经存在的用户名和密码
ssh.connect('192.168.2.149',22,'songqin','songqin')

'''
#执行命令，并获取命令执行结果
stdin,stdout,stdeer=ssh.exec_command('cd Desktop;ls')
print(stdout.read().decode('utf8'))
stdin,stdout,stdeer=ssh.exec_command('pwd')
print(stdout.read().deconde('utf8'))
'''

sftp=ssh.open_sftp() #进行文件传输

#将本地文件传送到远程机器,传入两个参数，第一个参数是本地文件路径，第二个参数是远程文件路径
sftp.put(r'D:\QQ\untitled\untitled\python进阶\day4\2文件上传\客户端\qq.png','/home/songqin/Desktop/loginPage.py')

#将远程机器文件下载到本地，第一个参数是远程文件路径，第二个参数是本地文件路径
sftp.get('','')

ssh.close()
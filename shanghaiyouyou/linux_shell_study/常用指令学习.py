#coding=utf-8
#author:Kingving time:2020/6/19 0:49

#1 连接服务器
host='服务器地址'
post=22
username:'root'
password:'wodemima'

#2 XFTP FTP文件上传  直接拖动即可

#3 linux常用指令

''' 简单指令
1.  ls 查看目录中的文件，只看名称，ll可看文件详情

2.cd/home 进入/home目录，cd.. 返回上级目录

3.mkdir dir1 创建一个叫dir1的目录

4.rmdir dir1 删除一个叫dir1的目录

5.rm -f file1 删除一个叫file1的文件，-f参数是用来忽略不存在的文件

6.rm -rf/mulu 目录下面文件以及子目录文件删除

7.cp/test1/file1/test2/file2 将/test1目录下的file1文件复制到/test2目录下并且将文件名改为file2

8.mv/test1/file1/test2/file2 将/test1目录下的file1文件移动到/test2目录下并且将文件名改为file2

9.mv * ../  将linux当前目录所有文件移动到上一级目录

10.ps -ef | grep xxx 显示进程pid

11.kill 终结进程，先使用ps命令找到进程id，使用kill -9 命令，终止进程

12.tar -xvf file.tar 解压tar包

13.unzip file.zip 解压zip包

14.unrar e file.rar 解压rar包

15.free -m 查看服务器内存使用情况

-----------------------------------------------------------------------------------------------------------
高级指令
1.查找文件
1）find 查找文件
find/-name "文件名"

2）find/* "py" 查找所有py开头的文件

3）find/-name *.exe 查找所有以exe结尾的文件

4）查找一个文件大小超过100M的文件
find.-type f -size +100m

2.查看日志
先cd到logs目录中（里面有xx.out文件）

tail -f xx.out

最后用ctrl+C 停止

3.查看最近1000行日志
tail -1000 xx.out

4.查看端口
netstat -anp |grep 端口号（如3306）

5.查看所有端口号情况
netstat -nultap


'''
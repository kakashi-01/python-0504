#coding=utf-8
#author:Kingving time:2020/7/27 0:05

'''写程序实现递归删除一个目录下的文件和文件夹;'''

# 利用os.walk()

import os

def RecDelDirAndFile(root_path):
    #遍历先删除文件
    for root,dirs,files in os.walk(root_path):
        for file in files:
            #拼接文件路径
            file_path = os.path.join(root,file)
            print(file_path)
            os.remove(file_path)

    #遍历删除非空目录，注意参数: topdown=False    
    for root,dirs,files in os.walk(root_path,topdown=False):
        for dir in dirs:
            #拼接目录路径
            dir_path = os.path.join(root,dir)
            print("dir:" ,dir_path)
            #删除非空目录
            os.rmdir(dir_path)

if __name__ == "__main__":
    RecDelDirAndFile("e:\\777res")
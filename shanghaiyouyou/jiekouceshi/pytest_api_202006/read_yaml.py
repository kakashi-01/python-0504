#coding=utf-8
#author:Kingving time:2020/6/30 23:02

import yaml
import os

def get_yaml_data(yamlpath):
    '''获取yaml文件数据'''

    #使用open函数读取
    f=open(yamlpath,'r',encoding='utf-8')
    yamldata=f.read()
    print(yamldata) #str

    #把yaml文件数据str转字典
    d=yaml.load(yamldata)
    f.close()#关闭
    # print(d)
    return d

if __name__ == '__main__':
    #获取上一层路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    print(curpath)

    # 拼接yaml文件路径
    yamlpath = os.path.join(curpath, 'update_info.yml')
    print(yamlpath)

#以上是获取yaml文件路径，可以复制到其他里面直接用

    a=get_yaml_data(yamlpath)
    print(a)
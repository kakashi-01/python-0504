#coding=utf-8
#author:Kingving time:2020/7/20 1:48
'''
应用场景：接口压测 - -jmeter - --
100
个用户的登录接口，需要不同账号与密码进行csv - -参数化操作
问题：100
个账号密码怎么获取？
方案：
1 - 数据库导出来
2 - 没有权限到，其他同事没时间，但是告诉你账号密码的规律，
python来实现 - --写文件

示例：sq016, 123456
'''
fileDir = 'e:\\name.txt'
fo = open(fileDir,'w')
for one in range(1,101):
    info = f'sq{one:0>3},123456'
    fo.write(info+'\n')


fo.close()

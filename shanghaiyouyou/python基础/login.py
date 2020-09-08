#coding=utf-8
#author:Kingving time:2020/6/29 22:28

def login_func(username,psw):
    '''
    登陆功能
    :param username:
    :param psw:
    :return:
    '''
    print(username)
    print(psw)
    return 'token xxxxxxx'


#测试函数功能
if __name__ == '__main__': #当在自己模块时可以执行，别人调用不执行
    login_func(username='11',psw='22')#自测的内容
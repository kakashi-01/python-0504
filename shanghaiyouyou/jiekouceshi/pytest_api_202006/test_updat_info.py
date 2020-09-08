#coding=utf-8
#author:Kingving time:2020/6/29 23:27


from jiekouceshi.pytest_api_202006.common_function import login, update_info, get_info
import requests

s = requests.sessions()

def setup_module(): #模块级别
    '''前置操作，整个模块开始用例前只执行一次'''
    login(s)  # 登陆
    print('前置操作，整个模块开始用例前只执行一次')

def teardown_module():#模块级别
    print('后置操作，整个模块开始用例前只执行一次')

def setup_function():#函数级别
    print('每个测试用例之前，都会执行一次')

def teardown_function():#函数级别
    print('每个测试用例结束，都会执行一次')


def test_get_info():#测试用例1
    '''修改成功'''
    infos = update_info(s, name='test', mail='xxx@qq.com')
    print(infos)  # 修改

    assert infos['data']['mail'] == 'xxx@qq.com'

def test_get_info1():#测试用例2
    '''修改不成功'''
    infos=update_info(s,name='test1',mail='xxx@qq.com')
    print(infos)

    assert infos['message']=='无权限操作'
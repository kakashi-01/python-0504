#coding=utf-8
#author:Kingving time:2020/6/30 0:16
from jiekouceshi.pytest_api_202006.common_function import login,update_info,get_info
import requests


def test_info_1(login_fixture):#引用login_fixture
    print('用例1')
    s=login_fixture
    print(s.headers)
    infos=update_info(s,name='test',mail='xxx@qq.com')
    assert infos['data']['mail'] == 'xxx@qq.com'


def test_info_2(login_fixture):
    print('用例2')
    s=login_fixture
    print(s.headers)


def test_info_3(unlogin_fixture): #不登录
    print('用例3')
    s=unlogin_fixture
    print(s.headers)


def test_info_4(unlogin_fixture):#不登录
    print('用例4')
    s=unlogin_fixture
    print(s.headers)
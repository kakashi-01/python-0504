#coding=utf-8
#author:Kingving time:2020/6/30 0:13

#conftest 固定名称
from jiekouceshi.pytest_api_202006.common_function import login,update_info,get_info
import requests
import pytest

@pytest.fixture(scope='session')#前置
def login_fixture():
    print('先登录,输入账号密码，登录')
    s=requests.session()
    login(s)
    yield s #相当于return出来
    print('后置操作')#后置
    s.close()#关闭session

@pytest.fixture(scope='session')  # 前置
def unlogin_fixture():
    print('不登录')
    s=requests.session()
    yield s  #相当于return出来
    print('后置操作')#后置
    s.close()#关闭session
#coding=utf-8
#author:Kingving time:2020/7/21 23:18

import pytest
import requests
from k15.login_xadmin_page import login_xadmin
import os

host=os.environ['host']

#添加命令行参数 parser内置fixture
def pytest_addoption(parser):
    pytest_addoption(
        '--cmdhost',action='store',
        default='http://49.235.92.12:8020',
        help='my option:host1 or host2'
    )

@pytest.fixture(scope='session',autouse=True) #会话开始时自动生效
def host(request):
    """设置环境变量，自动生效"""
    os.environ['host']=request.config.getoption("--cmdhost")



def host():
    h='http://49.235.92.12:8020'
    return h


#request 是pytest内置的fixture
@pytest.fixture(scope='session')
def login_fixture(request):
    """登录前置操作"""
    s=requests.session()
    #先登录
    login_xadmin(s)

    def close_s():
        s.close()

    def close_x():
        print('关闭其他的线程')
    request.addfinalizer(close_s) #终结函数
    request.addfinalizer(close_x)  # 终结函数
    return s

    # yield s
    # print('数据清理，后置操作')
    # s.close()



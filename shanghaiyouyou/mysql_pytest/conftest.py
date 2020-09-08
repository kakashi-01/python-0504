#coding=utf-8
#author:Kingving time:2020/7/3 0:25

import requests
import pytest

@pytest.fixture(scope='session')
def unlogin_fixture():
    """不登录"""
    s=requests.session()
    return  s

#coding=utf-8
#author:Kingving time:2020/7/22 23:37

import pytest


@pytest.fixture(scope='session')
def login_fixture():
    print('前置操作：登录')
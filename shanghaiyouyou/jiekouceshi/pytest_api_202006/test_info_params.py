#coding=utf-8
#author:Kingving time:2020/6/30 22:23

from jiekouceshi.pytest_api_202006.common_function import login,update_info,get_info
import requests
import pytest


def test_info_1(login_fixture):#引用login_fixture
    print('用例1')
    s=login_fixture
    print(s.headers)
    infos=update_info(s,name='test',mail='xxx@qq.com')
    assert infos['data']['mail'] == 'xxx@qq.com'

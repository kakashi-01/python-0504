#coding=utf-8
#author:Kingving time:2020/7/3 1:10

import pytest
from mysql_pytest.common_functions import register
from mysql_pytest.connect_mysql import execute_sql


#模拟删除注册信息的函数

@pytest.fixture(scope='function')#function级别：每个测试用例都去调用一次
def delete_register():
    '''执行sql,删除注册'''
    sql="'DELETE from auth_user WHERE username='test333';"
    execute_sql(sql)
    yield
    print('后置清理数据操作')


#在不登录的状态下执行用例
# 接口特征：执行一次，就不能重复执行了
# 接口自动化期望：用例可以重复执行
# 解决办法：用例开始前先清理数据：delete_register

def test_register_1(unlogin_fixture,delete_register):
    """测试用例：注册"""
    s=  unlogin_fixture
    r=register(s)
    print(r.json())
    assert r.json()['msg']=='注册成功'
    assert r.json()['code']==0

def test_register_2(unlogin_fixture,delete_register):
    """测试用例：重复注册"""
    s=  unlogin_fixture
    r=register(s) #注册第一次
    r2=register(s) #注册第二次

    print(r.json())
    assert r.json()['msg']=='注册成功'
    assert r.json()['code']==0
    assert '用户已被注册' in r2.json()['msg']
    assert r2.json()['code']==2000
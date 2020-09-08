#coding=utf-8
#author:Kingving time:2020/7/22 23:38

import pytest
from ke17.common_function import add_x,modify_aaa,get_xxx
import allure

@allure.feature('模块1：xxxxx')
def test_01():
    '''用例1的描述：xxxx'''
    print('测试用例1')

@allure.feature('模块1：xxxxx')
@allure.issue('http://49.235.92.12:8080/zentao/bug-view-1.html')
def test_02():
    '''用例2的描述：222222'''
    print('测试用例2')


@allure.feature('模块2:2222222')
@allure.story('story用例的标题：修改个人信息-sex参数为空')
@allure.testcase('http://49.235.92.12:8080/zentao/testcase-view-366-1.html')
def test_03(login_fixture):
    '''用例3的描述：333'''
    print('测试步骤1：')
    add_x()
    print('测试步骤2：')
    modify_aaa()
    print('测试步骤3：查询')
    get_xxx()

#coding=utf-8
#author:Kingving time:2020/7/23 0:00


import allure


@allure.severity('critical')
@allure.feature('模块3：xxxxx')
def test_01():
    '''用例1的描述：xxxx'''
    print('测试用例1')
    assert 1==2


@allure.severity('blocker')
@allure.feature('模块3：xxxxx')
@allure.issue('http://49.235.92.12:8080/zentao/bug-view-1.html')
def test_02():
    '''用例2的描述：222222'''
    print('测试用例2')
    assert 1==2

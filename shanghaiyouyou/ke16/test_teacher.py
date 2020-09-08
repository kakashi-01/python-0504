#coding=utf-8
#author:Kingving time:2020/7/21 23:43

from k15.login_xadmin_page import login_xadmin
from requests_toolbelt import MultipartEncoder
import requests
import re
from lxml import etree
from k15.from_data_xadmin import add_teacher_name
from mysql_pytest.connect_mysql import select_sql,execute_sql
import pytest
import allure

#前置操作：先清空数据
@pytest.fixture(scope='function')
def delete_teacher():
    sql='DELETE FROM djangoweb.hello_teacher WHERE '
    execute_sql(sql)
    yield
    print('数据清理的操作')



@allure.story('编辑文章分类，输入中文，编辑成功')
@allure.testcase('http://49.235.92.12:8080/zentao/testcase-view-6-2.html')

def test_add_teacher(login_fixture,delete_teacher):

    #新增数据
    s=login_fixture
    text=add_teacher_name(s)
    #查询数据库结果
    sql='SELECT count(*) as sum from djangoweb.hello_teacher'
    result1=select_sql(sql)[0]['sum']
    #校验结果
    assert result1==1
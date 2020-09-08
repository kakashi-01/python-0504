#coding=utf-8
#author:Kingving time:2020/7/22 23:39

import allure


@allure.step('登录')
def login():
    '''登录操作'''
    print('先登录')

@allure.step('添加xx内容')
def add_x():
    '''添加xx内容'''
    print('添加xx内容')

@allure.step('修改aaa内容')
def add_aaa():
    '''修改aaa内容'''
    print('修改aaa内容')



def modify_aaa():
    '''修改aaa内容'''
    print('修改aaa内容')

def get_xxx():
    '''查询xxx内容'''
    print('查询xxx内容')
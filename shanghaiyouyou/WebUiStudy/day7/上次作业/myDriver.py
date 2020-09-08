#coding=utf-8
#author:Kingving time:2020/6/8 0:10

from selenium import webdriver
from day7.上次作业.mySetting import DOMAIN,driverPath


class Driver:
    #浏览器驱动对象初始化为空，一个下划线：实例变量外部可访问
    #类成员，保存在类当中，实现唯一性
    _driver=None

    @classmethod
    def get_driver(cls,browser_name='Chrome'):
        """
        获取浏览器对象
        :param browser_name: 浏览器类型比如Chrome、IE
        :return: 浏览器驱动对象
        """
        #如果不为空就不需要创建，为空就要创建
        if cls._driver is None:
            if browser_name=="Chrome":
                cls._driver=webdriver.Chrome(driverPath["Chrome"])
            elif browser_name=='Firefox':
                cls._driver=webdriver.Firefox(driverPath['Firefox'])

            #.......省略其它的浏览器声明

            #最大化窗口
            cls._driver.maximize_window()
            #访问默认的网址
            #执行登录
            cls.__login()

        return cls._driver

    @classmethod
    def __login(cls):
        #登录逻辑，在driver初始化的时候被调用一次，去操作登录页面
        cls._driver.find_element_by_name('username').sendkeys('libai')
        cls._driver.find_element_by_name('password').sendkeys('opmsopms123')
        cls._driver.find_element_by_tagname('button').click()

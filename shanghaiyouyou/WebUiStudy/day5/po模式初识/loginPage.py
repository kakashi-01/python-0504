#coding=utf-8
#author:Kingving time:2020/6/6 0:46
from selenium import webdriver
class LoginPage:
    """登录页面"""

    def __init__(self):
        #创建driver对象
        self.driver=webdriver.Chrome('D:\selenium\chromedriver.exe')
        #访问网址
        self.driver.get('http://127.0.0.1:8088/login')

    def userInpBox(self):
        """实时获取用户名输入框"""
        return self.driver.find_element_by_name('username')

    def pwdInpBox(self):
        """实时获取密码输入框"""
        return self.driver.find_element_by_name('password')

    def loginButtonBox(self):
        """实时获取登录按钮"""
        return self.driver.find_element_by_css_selector('button')

#抽离出页面动作类，继承页面类,把常用的公共方法封装起来
class LoginPageAction(LoginPage):

    def login(self):
        #输入用户名
        self.userInpBox().send_keys('libai')

        #输入密码
        self.pwdInpBox().send_keys('opmsopms123')

        #点击登录按钮
        self.loginButtonBox().click()


if __name__ == '__main__':#实例化操作

    loginPageObj=LoginPageAction()
    loginPageObj.login()
#coding=utf-8
#author:Kingving time:2020/6/6 0:46
from selenium.webdriver.common.by import By
from day6.抽离出basePage的版本.basePage import BasePage

class LoginPage(BasePage):
    """登录页面"""

    def __init__(self):

        #执行父类的构造方法
        super().__init__()

        #用户名输入框
        self.userinpLo=(By.NAME,'username')
        #密码输入框
        self.pwdInpLo=(By.NAME,'password')
        #登录按钮
        self.loginButtonLo=(By.CSS_SELECTOR,'button')

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
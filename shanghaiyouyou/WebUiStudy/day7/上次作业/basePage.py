#coding=utf-8
#author:Kingving time:2020/6/9 0:41

from day6.抽离出basePage的版本.myDriver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day6.抽离出basePage的版本.mySetting import TIMEOUT,POLL_FREQUENCY

class BasePage:
    def __init__(self):
        #获取浏览器驱动对象
        self.driver=Driver.get_driver()

    def get_element(self, locator):
        """
        根据表达式匹配单个元素
        :param locator:元祖形式的元素定位表达式，比如（By.ID,"abc")
        :return:
        """
        # 只判断元素是否存在
        WebDriverWait(
            # 传入浏览器驱动对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY, ).until(
            # 检测元素是否可见
            EC.visibility_of_element_located(locator)
        )
        # 返回元素对象
        return self.driver.find_element(*locator)

    def get_element(self, locator):

        """
        根据表达式匹配元素列表
        :param locator:元祖形式的元素定位表达式，比如（By.ID,"abc")
        :return:
        """
        #只判断元素是否存在
        WebDriverWait(
            #传入浏览器驱动对象
            driver=self.driver,
            #传入超时时间
            timeout=TIMEOUT,
            #设置轮询时间
            poll_frequency=POLL_FREQUENCY,).until(
            # 检测元素是否可见
            EC.visibility_of_element_located(locator)
        )
        #返回元素对象
        return self.driver.find_elements(*locator)


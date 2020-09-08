#coding=utf-8
#author:Kingving time:2020/6/13 0:35

#项目管理页面

from day7.po模式实战.pages.basePage import BasePage

class ProjectManagementPage(BasePage):

    def __init__(self,path="/project/manage"):
        """
        项目管理页面类
        :param path:
        """
        super().__init__()
        self.path=self.url+path

    def to_page(self):
        self.driver.get(self.path)
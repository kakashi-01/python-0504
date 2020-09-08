#coding=utf-8
#author:Kingving time:2020/6/30 0:00


from jiekouceshi.pytest_api_202006.common_function import login, update_info, get_info
import requests

s = requests.session()



class TestInfo():
    def setup_class(self):  # 类级别
        '''前置操作，整个class开始用例前只执行一次'''
        login(s)  # 登陆
        print('前置操作class，整个class开始用例前只执行一次')

    def teardown_class(self):  # 类级别
        print('后置操作class，整个class开始用例前只执行一次')



    def setup_method(self):  # 方法级别
        '''前置操作，整个method开始用例前只执行一次'''
        login(s)  # 登陆
        print('前置操作method，整个method开始用例前只执行一次')



    def teardown_method(self):  # 方法级别
        print('后置操作method，整个method开始用例前只执行一次')




    def test_get_info_1(self):  # 测试用例1
        '''修改成功'''
        infos = update_info(s, name='test', mail='xxx@qq.com')
        print(infos)  # 修改

        assert infos['data']['mail'] == 'xxx@qq.com'

    def test_get_info_2(self):  # 测试用例2
        '''修改不成功'''
        infos = update_info(s, name='test1', mail='xxx@qq.com')
        print(infos)

        assert infos['message'] == '无权限操作'
        
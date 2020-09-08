#coding=utf-8
#author:Kingving time:2020/6/29 23:21


from jiekouceshi.pytest_api_202006.common_function import login,update_info,get_info
import requests

def test_get_info():
    s=requests.session()
    login(s) #登陆

    infos = update_info(s, name='test', mail='xxx@qq.com')
    print(infos) #修改

    # 查询
    m = get_info(s)
    print(m)
    assert infos['data']['mail']=='xxx@qq.com'
    assert m['data'][0]['mail']=='xxx@qq.com'
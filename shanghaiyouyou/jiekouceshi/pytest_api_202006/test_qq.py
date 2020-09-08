#coding=utf-8
#author:Kingving time:2020/6/26 1:15

import requests
def qq1(key,qq):
    url = 'http://japi.juhe.cn/qqevaluate/qq'
    querystring = {
        'key': key,
        'qq': qq
    }
    r = requests.get(url, params=querystring)
    print(r.text) #json字符串
    # print(r.json())#把json转换成python中的字典
    return r
def test_qq_1():
    """用例描述：qq号码-1.必填项key，输入正确的keyid，请求成功"""
    r=qq1(key='8dbee1fcd8627fb6699bce7b986adc45',qq=12345678)

    # error_code = r.json()["error_code"]
    # reason = r.json()["reason"]

    assert r.json()["error_code"] == 0
    assert r.json()["reason"] == 'success'

def test_qq_2():
    """用例描述：qq号码-2.必填项key为空，请求失败，提示 KEY ERROR"""

    r=qq1(key='',qq=12345678)

    assert r.json()["error_code"] ==10001
    assert r.json()["reason"] == 'KEY ERROR!'

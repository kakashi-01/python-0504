#coding=utf-8
#author:Kingving time:2020/6/30 22:02


import pytest


#参数化，中间的过程都是一样，只关注测试输入和测试结果
#一个测试输入对应一个测试结果

@pytest.mark.parametrize('test_input,expected',
                         [
                             ('1+3',4),
                             ('11+3',14)


                         ])
def test_eval(test_input,expected):
    a=test_input
    print('\n'+a)
    assert eval(a)==expected

# def test_eval1():
#     a='11+3'
#     assert eval(a)==14

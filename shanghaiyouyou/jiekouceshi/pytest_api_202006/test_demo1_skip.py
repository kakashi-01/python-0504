#coding=utf-8
#author:Kingving time:2020/6/30 22:10

import pytest

#期望结果都是固定的一个
#username '',123,'aaaa'
#psw '',234,'bbb'





#跳过skip
@pytest.mark.skip('跳过原因：有bug')
def test_2():
    '''已知这个接口有bug'''
    print('已经知道这个接口有BUG了')


#参数化，中间的过程都是一样，只关注测试输入和测试结果
#一个测试输入对应一个测试结果
@pytest.mark.parametrize('username',['',123,'aaaa'])
@pytest.mark.parametrize('psw',['',234,'bbb'])


def test_eval(username,psw):
    print('\n 账号和密码组合：%s,%s'%(username,psw))
    # assert
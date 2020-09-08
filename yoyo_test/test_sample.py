# -*- coding: utf-8 -*-
# @Author   : 'Kakashi'
# @Date     : 2020-08-13
import pytest

class Test_Class:
        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = "hello"
            assert hasattr(x, 'check')

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b

if __name__ == "__main__":
    pytest.main(['-q ','test_class.py'])
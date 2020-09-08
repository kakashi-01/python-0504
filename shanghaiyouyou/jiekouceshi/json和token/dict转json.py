#coding=utf-8
#author:Kingving time:2020/6/26 1:54


# Dict转json （注意：字典是无序的）
import json

d={
    'a':None,
    'b':213213,
    "c":'qweqfadsa',
    'd':True,
    'e':[1,2,3,True,None,'jeiwjr',False],
    'f':{
        'usename':'123',
        'password':'1515'
    }
}
print(d)
#标准输出
#{'a': None, 'b': 213213, 'c': 'qweqfadsa', 'd': True, 'e': [1, 2, 3, True, None, 'jeiwjr', False], 'f': {'usename': '123', 'password': '1515'}}

#转换成json
d_json=json.dumps(d)
print(d_json)
#标准输出json格式
# {"a": null, "b": 213213, "c": "qweqfadsa", "d": true, "e": [1, 2, 3, true, null, "jeiwjr", false], "f": {"usename": "123", "password": "1515"}}


'''
     |  | Python            | JSON          |
     |  +===================+===============+
     |  | dict              | object(str)   |
     |  +-------------- -----+-------------+|
     |  | list, tuple       | array         |
     |  +-------------------+---------------+  
     |  | str, unicode      | string        |
     |  +-------------------+---------------+
     |  | int, long, float  | number        |
     |  +-------------------+---------------+
     |  | True              | true          |
     |  +-------------------+---------------+ 
     |  | False             | false         |
     |  +-------------------+---------------+ 
     |  | None              | null          |
     |  +-------------------+--------------+|

'''












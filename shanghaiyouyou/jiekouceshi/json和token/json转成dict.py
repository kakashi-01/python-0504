#coding=utf-8
#author:Kingving time:2020/6/26 2:08

# eval（）将字符串转成字典
# indent加空格，ensure_ascii=false转变成中文
#json只能用双引号
#requests库里面的内置json解析器
#注意要导入import json
'''
r.json()#json字符串转换成dict，方便取值
r.text()#json字符串
json.dumps()#转json
json_dict=json.loads()#转字典
'''
'''
|  +---------------+-------------------+
     |  | JSON               | Python            |
     |  +===============+===================+
     |  | object             | dict              |
     |  +---------------+-------------------+
     |  | array               | list              |
     |  +---------------+-------------------+
     |  | string              | unicode           |
     |  +---------------+-------------------+
     |  | number (int)    | int, long         |
     |  +---------------+-------------------+
     |  | number (real)   | float             |
     |  +---------------+-------------------+
     |  | true                | True              |
     |  +---------------+-------------------+
     |  | false               | False             |
     |  +---------------+-------------------+
     |  | null                 | None              |
     |  +---------------+-------------------+
'''
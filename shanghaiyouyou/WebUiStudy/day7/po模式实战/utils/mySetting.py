#coding=utf-8
#author:Kingving time:2020/6/11 20:29


#配置文件

#域名，将网址配置成配置文件
DOMAIN='http://127.0.0.1:8088'


#超时时间
TIMEOUT=10

#轮询时间
POLL_FREQUENCY=0.5

#driver路径
driverPath={
    "Chrome":'D:\selenium\chromedriver.exe'
    # 'Firefox''D:\selenium\geodriver.exe'
}

#cookie过期后需要更新的
cookieSli=[{'domain': '127.0.0.1',
          'httpOnly': False,
          'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
          'path': '/',
          'secure': False,
          'value': '1591879157'},
         {'domain': '127.0.0.1',
          # 'expiry': 1623415157,
          'httpOnly': False,
          'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
          'path': '/',
          'secure': False,
          'value': '1591879157'},
         {'domain': '127.0.0.1',
          # 'expiry': 1623415157,
          'httpOnly': True,
          'name': 'beegosessionID',
          'path': '/',
          'secure': False,
          'value': 'c3860256b9277f07e8fdabe73727dab4'}]

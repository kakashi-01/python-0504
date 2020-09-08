#coding=utf-8
#author:Kingving time:2020/6/2 0:49

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('http://www.vmall.com')

# 3、获取所有的一级菜单
liSli=driver.find_elements_by_css_selector('ol>li')
for liEle in liSli:
    #一级菜单名称打印
    print('一级菜单:',liEle.find_element_by_css_selector('a>span').text)

    #鼠标悬停到一级菜单
    ActionChains(driver).move_to_element(liEle).perform()

    #匹配每一个二级菜单
    liEle2=liEle.find_elements_by_css_selector('p>span')
    for i in liEle2:
        print('\t',i.text)

# ----------------------------------------------------------------

#通过执行js向下滑动
driver.execute_script('window.scrollBy(0,1000)')

#找到每个单品
lisLi=driver.find_elements_by_css_selector('div[class=\"span-968 fl\"] > ul[class=\"grid-list clearfix\"] > li')
for i in lisLi:
    if not i.find_elements_by_css_selector('span'): #如果没找到继续找
        continue

    #如果找到了，获取商品名称
    goodName=i.find_element_by_css_selector('div').text

    #获得商品价格
    goodPrice=i.find_element_by_css_selector('p[class=\"grid-price\"]').text

    print('商品名称  {},商品价格  {}'.format(goodName,goodPrice))

driver.quit()
#coding=utf-8
#author:Kingving time:2020/5/26 22:41


from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('https://m.weibo.cn/')

#隐式等待
driver.implicitly_wait(5)

#3、先通过input标签并点击
driver.find_element_by_class_name("m-search").click()
# driver.find_element_by_xpath('//i[@class="m-font m-font-search"]').click()

#4、点击微博热搜榜按钮
#先定位到热搜榜所在的外层大标签
hotEle=driver.find_element_by_xpath('//div[@class=\"card m-panel card16 m-col-2\"]')

#在大标签列表中，点击微博热搜榜按钮
hotEle.find_elements_by_class_name('m-text-cut')[-1].click()

#5、找到每分钟更新一次的最外层大标签
hotSli=driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
# hotEleSli=hotSli.find_elements_by_class_name('card m-panel card4')
hotEleSli = hotSli.find_elements_by_class_name("card4") #当用class name定位元素，此时class name中元素定位不能有空格（复合类）
for ele in hotEleSli:
    iconSli=ele.find_elements_by_class_name('m-link-icon') #匹配每个小标签的元素列表
    if iconSli:
        img=iconSli[0].find_element_by_tag_name('img')#取0是因为只有一个标签，从小标签中找到img元素
        srcLinkText=img.get_attribute('src') #通过src关键字 判断标签类型

        #判断类型
        if 'fei' in srcLinkText:
            hotType='沸'
            print('热搜类型是：',hotType)
            print('热搜文本是：',ele.find_element_by_class_name('m-text-cut').text)
        elif 'hot' in srcLinkText:
            hotType = '热'
            print('热搜类型是：', hotType)
            print('热搜文本是：',ele.find_element_by_class_name('m-text-cut').text)
driver.quit()

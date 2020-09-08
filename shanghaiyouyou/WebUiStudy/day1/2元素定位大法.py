#coding=utf-8
#author:Kingving time:2020/5/24 23:52


#找到元素赋值给变量，或者直接操作元素


from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('file:///D:/QQ/untitled/untitled/untitled/Web自动化测试/day1/test.html')


'''元素定位
#3、通过id属性定位--第一招
# textElement=driver.find_element_by_id('abc')

#4、获取元素文本值
# print(textElement.text)

#5、通过name属性定位--第二招
inp_element=driver.find_element_by_name('a1')
inp_element.send_keys('孔雀东南飞')

#6、通过xpath定位--第三招
option_element=driver.find_element_by_xpath('/html/body/div/select/option[2]')
print(option_element.text)

#7、通过链接文本定位--第四招（精确定位）
driver.find_element_by_link_text('访问百度').click()

#8、通过部分链接文本定位（模糊定位）--第五招
driver.find_element_by_partial_link_text('问').click()

#9、通过标签名称进行匹配查找（tag name），只返回匹配到的第一个元素,如果找不到就报错--第六招
ele=driver.find_element_by_tag_name('span')
print(ele.text)

#10、通过class名称进行查找--第七招
ele=driver.find_element_by_class_name('a2')
print(ele.text)

#11、通过css选择器查找--第八招
sele_element=driver.find_element_by_css_selector('body > div:nth-child(7) > table > tbody > tr:nth-child(2) > td').text
print(sele_element)
'''

driver.quit()
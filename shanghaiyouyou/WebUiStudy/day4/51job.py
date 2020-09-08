#coding=utf-8
#author:Kingving time:2020/6/4 23:49


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

driver.get('http://www.51job.com')

#1点击高级搜索
driver.find_element_by_css_selector('a[class=\"more\"]').click()

#2输入关键词python
driver.find_element_by_id('kwdselectid').send_keys('python')

#3点击其它区域取消蒙层
driver.find_element_by_css_selector('div[class=\"rtit r1\"]').click()

#4地区选择杭州
driver.find_element_by_css_selector('div>p [class=\"dicon\"]').click()

#5匹配默认被选中的元素，匹配元素列表
citySli=driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span')
for city in citySli:
    city.click()
    time.sleep(0.5)

#6选择杭州并且点击确定
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()

driver.find_element_by_id('work_position_click_bottom_save').click()

#7定位到职能类别
driver.find_element_by_id('funtype_click').click()

#8点击后端开发
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

#9点击高级软件工程师
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()

#10点击确定
confirmEle=driver.find_element_by_id('funtype_click_bottom_save').click()

#11公司性质选 外资 欧美
driver.find_elements_by_css_selector('div span[class=\"ic i_arrow\"]')[0].click()

driver.find_element_by_css_selector('span[title=\"民营公司\"]').click()

#12工作年限选 1-3 年
driver.find_elements_by_css_selector('div span[class=\"ic i_arrow\"]')[1].click()
driver.find_element_by_css_selector('span[title=\"1-3年\"]').click()

#13点击搜索按钮开始搜索职位
driver.find_element_by_css_selector('div[class=\"btnbox p_sou\"]> span[class=\"p_but\"] ').click()

# --------------------------------------------------------------------------------------------------


#抓取职位信息

# 1匹配每一行职位：
jobEleLis=driver.find_elements_by_css_selector('#resultList>div[class=\"el\"]')
for job in jobEleLis:
    #职位名称
    jobName=job.find_element_by_css_selector('p').text

    #公司名：
    jobComName=job.find_element_by_css_selector("[class=\"t2\"]").text

    #工作地点：
    jobAddr=job.find_element_by_css_selector("[class=\"t3\"]").text

    #薪资：
    jobPrice=job.find_element_by_css_selector("[class=\"t4\"]").text

    #发布时间
    jobDate=job.find_element_by_css_selector("[class=\"t5\"]").text

    # print('|'.join([jobName,jobComName,jobPrice,jobDate]))
    print('职位名称：{},公司名：{},工作地点：{}'.format(jobName,jobComName,jobAddr))




driver.quit()
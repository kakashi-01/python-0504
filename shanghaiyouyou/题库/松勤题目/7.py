#coding=utf-8
#author:Kingving time:2020/7/6 0:02
'''
7、浏览器进入网页云音乐  https://music.163.com/
在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量'''
from selenium import webdriver
import time

#1、创建一个浏览器驱动对象
driver=webdriver.Chrome('D:\selenium\chromedriver.exe')

#2、访问网址
driver.get('https://music.163.com/')

#3、 进入排行榜
driver.find_element_by_css_selector('#g_nav2 > div > ul > li:nth-child(2) > a').click()

#4、进入云音乐新歌版
driver.find_element_by_id('3779629').click()


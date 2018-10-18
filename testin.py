#coding=utf-8
"""
@Time : 2018/10/18 9:44
@Author : pawpawdu
"""
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
#浏览器最大化

print("浏览器最大化")
driver.maximize_window()

#设置浏览器宽、高

print("设置浏览器宽480，高800显示")
driver.set_window_size(1280,720)

#控制浏览器前进、后退

first_url = "http://www.baidu.com"
print("now access %s"%(first_url))
driver.get(first_url)

#访问新闻页面

second_url = "http://test.baidu.com"
print("now access %s"%(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to %s"%(first_url))
driver.back()

#前进到百度众测
print("forward to %s"%(second_url))
driver.forward()


#定位方法find
"""
id 
name
class name
link text
partial link text 
xpath
css selector
方法：find_elements_by_partial_link_text()
"""
#通过tag标签名对元素进行定位，不太靠谱，重名太多div input、script（脚本）
driver.find_elements_by_tag_name("div")

#通过元素中带的class属性对元素进行定位
#class="main-head"
driver.find_element_by_class_name("main-head")

#link text 链接元素
# <a href="/crowdtest/community/index">首页</a>
driver.find_element_by_link_text("成就").click()
driver.find_element_by_link_text("任务").click()
driver.find_element_by_link_text("公会").click()
driver.find_element_by_link_text("首页").click()
#partial link text 一部分内容，特定不重复的

driver.find_elements_by_partial_link_text("公测社区3.0")

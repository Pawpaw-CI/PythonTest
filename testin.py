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
driver.set_window_size(480,800)

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
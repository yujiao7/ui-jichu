#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/19'
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")
# 调整窗口大小
driver.maximize_window()

# 点击重置按钮 弹出提示框后显示只有一个确认按钮点击确认后自动关闭
def alert_demo():
    driver.get("C://Users//Administrator//Documents//WeChat%20Files//y470778//FileStorage//File//2019-09//demo.html")
    sleep(2)
    # l=driver.find_element_by_xpath('//input[@type="reset"]')  # 和后面.click()方法一样
    # l.click()
    driver.find_element_by_xpath('//input[@type="reset"]').click()
    alert = driver.switch_to.alert  # 弹框不能定位时，直接用这种方式定位到弹框
    sleep(2)
    alert.accept()   # 表示点击确定按钮
    # alert.dismiss()    # 表示点击取消按钮

#  普通按钮 ，弹出提示框输入答案，填制后按确定按钮
def propt_demo():
    driver.get("C://Users//Administrator//Documents//WeChat%20Files//y470778//FileStorage//File//2019-09//demo.html")
    sleep(2)
    driver.find_element_by_xpath('''//input[@type="button"]''').click()
    sleep(2)
    propt1 = driver.switch_to.alert
    sleep(2)
    propt1.send_keys("nihaoa")
    sleep(2)
    propt1.accept()


# 提交按钮 点击后弹出提示款，点击取消后自动关闭
def submit_demo():
    driver.get("C://Users//Administrator//Documents//WeChat%20Files//y470778//FileStorage//File//2019-09//demo.html")
    sleep(2)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    sleep(2)
    su=driver.switch_to.alert
    sleep(2)
    su.dismiss()

if __name__ == '__main__':
    # alert_demo()
    # propt_demo()
    submit_demo()
    sleep(2)      # 休息
    driver.quit() # 关闭浏览器
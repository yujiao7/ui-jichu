#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/19'

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")
driver.maximize_window()


# 滚动窗口
def scroll_window():
    driver.get("https://www.baidu.com/")
    sleep(2)
    a = driver.find_element_by_id("kw")
    a.clear()
    a.send_keys("华为手机")
    sleep(2)
    driver.find_element_by_id('su').click()
    sleep(3)
    # 没有滚动模块包
    # 滚动到页面底部
    js = "var q=document.documentElement.scrollTop=100"

    driver.execute_script(js)
    sleep(2)

    # 滚动到指定元素出现
    # target = driver.find_element_by_xpath('''(//h3/a/em)[8]''')
    #
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    # sleep(2)


if __name__ == '__main__':
    scroll_window()
    sleep(2)
    driver.quit()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/17'
from time import sleep

import driver as driver
from selenium import webdriver

# 打开浏览器
driver=webdriver.Chrome("../chromedriver-v77/chromedriver.exe")


# 调整浏览器窗口大小
driver.maximize_window() # 窗口最大化一般用这个
# driver.set_window_size(1600,900) # 括号里面跟分辨率

# 打开网址
driver.get("http://api.yansl.com:8080/swagger-ui.html#!")
sleep(2)
driver.get("https://www.baidu.com/")
sleep(2)
driver.get("https://www.taobao.com/")


# 后退
driver.back()
sleep(2)

# 前进
driver.forward()
sleep(2)

# 刷新
driver.refresh()
sleep(2)

# 关闭浏览器
sleep(3)
# driver.close()# 只关浏览器不退出进程
driver.quit()# 推荐用这个机关掉又结束进程
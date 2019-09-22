#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/19'
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, support
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")
# 调整窗口大小
driver.maximize_window()

#  根据http://www.guoyasoft.com:8080/guoya-client
def iframe_demo():
    # 打开网址
    driver.get("http://www.guoyasoft.com:8080/guoya-client/jsp/user/login.jsp")
    sleep(2)
  # 定位用户名输入框
    username = driver.find_element_by_id("userName")
    username.clear()
    username.send_keys("xuepl")
    # 定位密码输入框，并输入密码
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("123456")
    #定位登录按钮点击
    driver.find_element_by_id('loginBtn').click()
    sleep(2)
   # 定位面试查询，并点击
    driver.find_element_by_xpath("//a[text()='面试查询']").click()
    sleep(10)
    # 切换至iframe 要先定位到一个空白框里面
    iframe=driver.find_element_by_id('iframepage')
    driver.switch_to.frame(iframe)
    # 定位到查询按钮并点击查询
    driver.find_element_by_xpath("//button[text()='查询']").click()
    sleep(2)
    # 想点击iframe 外面的必须先退出当前iframe
    # 退出当前iframe
    driver.switch_to.parent_frame()
    # 返回最外层页面
    # driver.switch_to.default_content()
    driver.find_element_by_xpath("//a[text()='作业检查1811A']").click()
    sleep(2)
# driver.implicitly_wait(10)
# selenium显示等待和隐示等待
from selenium.webdriver.support import expected_conditions as EC

def iframe_demo():
    # 打开网址
    driver.get("http://www.guoyasoft.com:8080/guoya-client/jsp/user/login.jsp")
    # sleep(2)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userName'))# 这里只能放一个元素进去，元组或者列表。
  # 定位用户名输入框
    username = driver.find_element_by_id("userName")
    username.clear()
    username.send_keys("xuepl")
    # 定位密码输入框，并输入密码
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("123456")
    #定位登录按钮点击
    driver.find_element_by_id('loginBtn').click()
    sleep(2)
   # 定位面试查询，并点击
    driver.find_element_by_xpath("//a[text()='面试查询']").click()
    sleep(10)
    # 切换至iframe 要先定位到一个空白框里面
    iframe=driver.find_element_by_id('iframepage')
    driver.switch_to.frame(iframe)
    # 定位到查询按钮并点击查询
    driver.find_element_by_xpath("//button[text()='查询']").click()
    sleep(2)
    # 想点击iframe 外面的必须先退出当前iframe
    # 退出当前iframe
    driver.switch_to.parent_frame()
    # 返回最外层页面
    # driver.switch_to.default_content()
    driver.find_element_by_xpath("//a[text()='作业检查1811A']").click()
    sleep(2)



# 切换窗口，先按住ctrl 左击打开几个窗口(超链接)
def qiehuan_chuangkou_demo():
    driver.get("C://Users/Administrator//Documents//WeChat%20Files//y470778//FileStorage//File//2019-09//demo.html")
    sleep(2)
    # jdong=driver.find_element_by_partial_link_text("京东")
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).click(jdong).key_up(Keys.CONTROL).perform()  # 按下ctrl 按住点击jdong，然后抬起ctrl，执行
    # # actions.reset_actions()    # 重置清除 这里可以不用
    sleep(2)
    # "问问度娘"窗口
    # baidu = driver.find_element_by_partial_link_text("问问度娘")
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).click(baidu).key_up(Keys.CONTROL).perform()
    # actions.reset_actions()
    # sleep(2)
    # # "当当"窗口
    # dd = driver.find_element_by_partial_link_text("当当")
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).click(dd).key_up(Keys.CONTROL).perform()
    # actions.reset_actions()
    # sleep(2)\
    # 两种方法
    jdong = driver.find_element_by_partial_link_text("京东")
    baidu = driver.find_element_by_partial_link_text("问问度娘")
    dd = driver.find_element_by_partial_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dd).click(baidu).click(jdong).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 窗口句柄：一个句柄代表一个窗口
    # 切换上面所有窗口
    handles = driver.window_handles
    for h in handles:
        driver.switch_to.window(h)
        sleep(2)
      # print(h)  # 打印句柄

      # 指定切换的窗口
      # handles = driver.window_handles
      # for h in handles:
      #     driver.switch_to.window(h)
      #     sleep(2)
      #     if (driver.title.__contains__("京东")):  # 指定切换的窗口
      #         break


if __name__ == '__main__':
    # iframe_demo()
    qiehuan_chuangkou_demo()
    sleep(2)
    driver.quit()



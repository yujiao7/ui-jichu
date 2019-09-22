#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yj'
#__mtime__ = '2019/9/18'
import os
from time import sleep

import autoit
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")
driver.maximize_window()
# 查找输入框
def input_demo():
    # 查找元素的方法有：id(选择使用）,name,class,tag_name,xpath(推荐)，css_selector
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    text = driver.find_element_by_name("t1")
    # 清空
    text.clear()
    # 填值
    text.send_keys("你好")

    # 组合键 先ctrl+a 全选然后抬起键盘然后删除最后执行
    actions = ActionChains(driver)
    actions.click(text).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
   #  继续操作要重置才能执行
   # actions.reset_actins()

def input_demo2():
    # 查找元素的方法有：id(选择使用）,name,class,tag_name,xpath(推荐)，css_selector
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    text = driver.find_element_by_name("t2")
    # 清空
    text.clear()
    # 填值
    text.send_keys("你好")





 # 查找单选框
def radio_demo():
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    sex = driver.find_element_by_xpath("//input[@value='0']")
    sex.click()

def radio_demo2():
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    sex = driver.find_element_by_xpath("//input[@value='1']")
    sex.click()

def radio_demo33():
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    sex = driver.find_element_by_xpath("(//span[@class='el-radio__inner'])[2]")
    sex.click()

# 查询多选框

def check_box_demo():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("//input[@value='1']")
    check_box.click()
    if (not check_box.is_selected()):
        check_box.click()


def check_box_demo2():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("//span[@class='el-checkbox__inner']")
    check_box.click()
    if (not check_box.is_selected()):# 判断条件
        check_box.click()
    #check_box.is_enabled()#当前元素可用unabled()不可用
    # attribute = check_box.get_attribute("class") #获取属性
    # print(attribute)
# def check_box_demo3():
#     driver.get("http://ui.yansl.com/#/checkbox")
#     sleep(2)
#     check_box = driver.find_element_by_xpath("//span[text()='html]")
#     check_box.click()
#     check_box.is_enabled()

def check_box_demo4():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("//span[text()='上海']/../span/span")
    check_box.click()
    if (not check_box.is_selected()) : # 判断条件
        check_box.click()

def check_box_demo5():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("(//span[text()='上海'])[2]")
    check_box.click()
    if (not check_box.is_selected()) : # 判断条件
        check_box.click()
# 下拉框
def select_demo():
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select = driver.find_element_by_xpath("//input[@name='item2']")
    select.click()
    sleep(1)
    lll = driver.find_element_by_xpath("//span[text() = '黄金糕2']")
    lll.click()

def select_demo2():
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select = driver.find_element_by_xpath("//input[@name='item3']")
    select.click()
    sleep(1)
    select2 = driver.find_element_by_xpath("(//span[text()='双皮奶'])[5]")
    select2.click()
    sleep(1)
    select2 = driver.find_element_by_xpath("//form")   # 要点击空白的地方定位
    select2.click()
def select_demo3():
    driver.get("http://ui.yansl.com/#/select")
    select = driver.find_element_by_xpath("//input[@name='item4']")
    sleep(2)
    selecti = driver.find_element_by_xpath("(//li[@name='option4'])[2]")
    selecti.click()
    sleep(1)
    # select2 = driver.find_element_by_xpath("//form")
    # select2.click()

# 级联选择器
def cascader_demo():
    driver.get("http://ui.yansl.com/#/cascader")
    sleep(2)
    driver.find_element_by_xpath("//label[text()='hover触发']/../div//input").click()
    sleep(2)
    zu_jian=driver.find_element_by_xpath("(//span[text()='组件'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(zu_jian).perform()

# 任意时间框

def time_demo():
    driver.get("http://ui.yansl.com/#/dateTime")
    time_demo= driver.find_element_by_xpath('//input[@placeholder="任意时间"]')
    time_demo.clear() # 清除
    time_demo.send_keys("18:50:01") # 写入值


# 文件上传框
def upload_demo():
    driver.get("http://ui.yansl.com/#/upload")
    sleep(1)
    # upload1 = driver.find_element_by_xpath("//label[text()='原始上传']/../div/input")
    # upload1.send_keys("C:\\Users\\Administrator\\Desktop\\replay_pid728.log") # 每个斜杠都要加\转义

# send_key 上传方法只支持input标签，type属性为file的
    file=driver.find_element_by_xpath("(//span[text()='点击上传'])[1]")
    file.click()
    autoit.win_wait("打开", 10)
    sleep(2)
# autoit.control_send("打开", "Edit1", os.path.abspath(file_path))

    autoit.control_set_text("打开", "Edit1","C:\\Users\\Administrator\\Desktop\\replay_pid728.log" )
    sleep(2)
    autoit.control_click("打开", "Button1")

if __name__ == '__main__':
    # input_demo()
    # input_demo2()
    # time_demo()
    # radio_demo()
    # radio_demo2()
    # upload_demo()
    # cascader_demo()
    # check_box_demo()
    # check_box_demo2()
    # check_box_demo3()
    # check_box_demo4()

    # select_demo()
    select_demo2()
    # select_demo3()  有问题

    # check_box_demo5()
    sleep(2)
    driver.quit()

#-*- coding: UTF-8 -*-
'''
Created on 2017-7-24
@author: chow_meng
Project:语音配置页面的测试用例
'''
from selenium import webdriver
import unittest, time
from BasePage.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SetandSaveTest(unittest.TestCase):#设置和保存
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://120.92.2.162/hcis_test/#/"
    # Step1: 输入ip
        self.driver.get(self.base_url)
    # Step2: Open Login page
        login_page = LoginPage(self.driver)
    # Step3: 输入用户名
        login_page.set_username()
    # Step4:输入密码
        login_page.set_password()
    # 点击登录
        login_page.click_login()
    time.sleep(2)
    
    def test_line_cfg_Set_and_Save(self):

       
        time.sleep(3)
        title=driver.title
        
    def tearDown(self):

        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
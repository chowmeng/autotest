#-*- coding: UTF-8 -*-
'''
Created on 2017-7-24
@author: chow_meng
Project:登录测试用例
'''
from selenium import webdriver
import unittest, time
from BasePage.LoginPage import LoginPage
from BasePage.CreatafilePage import CreatafilePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import sys

my_browser =webdriver.Chrome()

def setUpModule():
	defaultencoding = 'utf-8'
	if sys.getdefaultencoding() != defaultencoding:
		reload(sys)
		sys.setdefaultencoding(defaultencoding)
	my_browser.implicitly_wait(30)
def tearDownModule():
    my_browser.quit()

    
class LoginTest(unittest.TestCase):
	#@classmethod
	#def setUpClass(self):
		
	#@classmethod	
	#def tearDownClass(self):
	def setUp(self):
		my_browser.delete_all_cookies()
		self.base_url = "http://120.92.2.162/hcis_test"
		my_browser.get(self.base_url)
		time.sleep(1)
    
	#def tearDown(self):
		

	def test_login_right(self):
		u"""test_1.1登录-正常登录"""
		login_page = LoginPage(my_browser)
		login_page.set_username()
		login_page.set_password()
		login_page.click_login()
		get_rec=login_page.ifloginok()
		self.assertEqual(get_rec,True,msg='Failed to enter the main interface after landing')
		
	def test_login_noinput(self):
		u"""test_1.2登录-未输入用户名密码"""  		
		login_page = LoginPage(my_browser)
		login_page.click_login()
		time.sleep(2)
		get_rec=login_page.ifloginonimput()
		self.assertEqual(get_rec.strip(), u'登录失败',msg='No alert or error alert')
		
	def test_login_wrong_password(self):
		u"""test_1.3登录-错误的密码""" 		
		login_page = LoginPage(my_browser)
		login_page.set_username()
		login_page.set_wrong_password()
		login_page.click_login()
		time.sleep(2)
		get_rec=login_page.ifloginonimput()
		#t = Test()
		self.assertEqual(get_rec, u'访问数据接口失败',msg='No alert or error alert')
		
	def test_login_wrong_username(self):
		u"""test_1.4登录-错误的用户名""" 		
		login_page = LoginPage(my_browser)
		login_page.set_wrong_username()
		login_page.set_password()
		login_page.click_login()
		time.sleep(2)
		get_rec=login_page.ifloginonimput()
		self.assertEqual(get_rec, u'访问数据接口失败',msg='No alert or error alert')

class CreateafileTest(unittest.TestCase):

	def test_login_right(self):
		u"""test_1.1登录-正常登录"""
		creatafile_page = CreatafilePage(my_browser)
		creatafile_page.click_Patient_management()
		time.sleep(1)
		creatafile_page.click_Creat_a_file()
		time.sleep(1)
		creatafile_page.set_Social_security_number()
		creatafile_page.set_patient_name()
		creatafile_page.set_cellphone_number()
		time.sleep(1)
		creatafile_page.click_attending_doctor_selecter()
		creatafile_page.click_attending_doctor()
		time.sleep(1)
		creatafile_page.click_Creat()
		time.sleep(1)
		get_rec=creatafile_page.ifloginok()
		time.sleep(1)
		self.assertEqual(get_rec,u'用户添加成功',msg='Failed to creat a patient')

	

if __name__ == "__main__":
    unittest.main()
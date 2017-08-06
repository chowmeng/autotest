#-*- coding: UTF-8 -*-
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest,HTMLTestRunner
from TestCase import Test_Login
import sys



#构造测试集
suite = unittest.TestSuite()
suite.addTest(Test_Login.LoginTest('test_login_right'))
suite.addTest(Test_Login.CreateafileTest('test_login_right'))




if __name__=='__main__':
    #执行测试
    fr = open('res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title=u'糖尿病照护系统测试报告',description=u'测试报告详情')
    report.run(suite)

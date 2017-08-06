#-*- coding: UTF-8 -*-
import yaml,os,time
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import GetElement


class LoginPage(BasePage):
    """description of class"""
    filename = os.path.join(os.path.dirname(__file__),'Element_Login.yaml').replace("\\","/")
    f = open(filename)
    login_ele=yaml.load(f)

    def set_username(self):
        GetElement.Inputit(self.driver,LoginPage.login_ele['input_name'])
    def set_wrong_username(self):
        GetElement.Inputwrongit(self.driver,LoginPage.login_ele['input_name'])
    def set_password(self):
        GetElement.Inputit(self.driver,LoginPage.login_ele['input_pwd'])
    def set_wrong_password(self):
        GetElement.Inputwrongit(self.driver,LoginPage.login_ele['input_pwd'])
    def click_login(self):
        GetElement.Clickit(self.driver,LoginPage.login_ele['button_login'])
    def ifloginok(self):
        return GetElement.isElementExist(self.driver,LoginPage.login_ele['main_interface']['leftspan'])
    def ifloginonimput(self):
        return GetElement.getStr(self.driver,LoginPage.login_ele['noimputerror'])

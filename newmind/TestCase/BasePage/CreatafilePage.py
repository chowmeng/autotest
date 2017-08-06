#-*- coding: UTF-8 -*-
import yaml,os,time
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import GetElement


class CreatafilePage(BasePage):
    """description of class"""
    filename = os.path.join(os.path.dirname(__file__),'Element_Creatafile.yaml').replace("\\","/")
    f = open(filename)
    creatafile_ele=yaml.load(f)

    def click_Patient_management(self):
        GetElement.Clickit(self.driver,CreatafilePage.creatafile_ele['Patient_management'])
    def click_Creat_a_file(self):
        GetElement.Clickit(self.driver,CreatafilePage.creatafile_ele['Creat_a_file'])
    def set_Social_security_number(self):
        GetElement.Inputit(self.driver,CreatafilePage.creatafile_ele['Social_security_number'])
    def set_patient_name(self):
        GetElement.Inputit(self.driver,CreatafilePage.creatafile_ele['patient_name'])
    def set_cellphone_number(self):
        GetElement.Inputit(self.driver,CreatafilePage.creatafile_ele['cellphone_number'])
    def click_attending_doctor_selecter(self):
        GetElement.Clickit(self.driver,CreatafilePage.creatafile_ele['attending_doctor_selecter'])
    def click_attending_doctor(self):
        GetElement.Clickit(self.driver,CreatafilePage.creatafile_ele['attending_doctor'])
    def click_Creat(self):
        GetElement.Clickit(self.driver,CreatafilePage.creatafile_ele['creat_file'])
    def ifloginok(self):
        return GetElement.getStr(self.driver,CreatafilePage.creatafile_ele['ifcreat_ok'])
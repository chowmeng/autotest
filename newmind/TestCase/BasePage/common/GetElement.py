#-*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

def Clickit(mydriver,butt):
	#print butt['type']
	if butt['type']=='name':
		mydriver.find_element_by_name(butt['value']).click()
	elif butt['type']=='id':
		mydriver.find_element_by_id(butt['value']).click()
	elif butt['type']=='class':
		mydriver.find_element_by_class_name(butt['value']).click()
	elif butt['type']=='XPath':
		mydriver.find_element_by_xpath(butt['value']).click()
	elif butt['type']=='link_text':
		mydriver.find_element_by_link_text(butt['value']).click()
def Inputit(mydriver,butt):
	#print butt['type']
	if butt['type']=='name':
		mydriver.find_element_by_name(butt['value']).send_keys(butt['inputvalue'])
	elif butt['type']=='id':
		mydriver.find_element_by_id(butt['value']).send_keys(butt['inputvalue'])
	elif butt['type']=='class':
		mydriver.find_element_by_class_name(butt['value']).send_keys(butt['inputvalue'])
	elif butt['type']=='XPath':
		mydriver.find_element_by_xpath(butt['value']).send_keys(butt['inputvalue'])
def Inputwrongit(mydriver,butt):
	#print butt['type']
	if butt['type']=='name':
		mydriver.find_element_by_name(butt['value']).send_keys(butt['wrongvalue'])
	elif butt['type']=='id':
		mydriver.find_element_by_id(butt['value']).send_keys(butt['wrongvalue'])
	elif butt['type']=='class':
		mydriver.find_element_by_class_name(butt['value']).send_keys(butt['wrongvalue'])
	elif butt['type']=='XPath':
		mydriver.find_element_by_xpath(butt['value']).send_keys(butt['wrongvalue'])
def Getit(mydriver,butt):
	#print butt['type']
	if butt['type']=='name':
		return mydriver.find_element_by_name(butt['value'])
	elif butt['type']=='id':
		return mydriver.find_element_by_id(butt['value'])
	elif butt['type']=='class':
		return mydriver.find_element_by_class_name(butt['value'])
	elif butt['type']=='XPath':
		return mydriver.find_element_by_xpath(butt['value'])
def isElementExist(mydriver,butt):
		flag=True	
		try:
			if butt['type']=='name':
				mydriver.find_element_by_name(butt['value'])
			elif butt['type']=='id':
				mydriver.find_element_by_id(butt['value'])
			elif butt['type']=='class':
				mydriver.find_element_by_class_name(butt['value'])
			elif butt['type']=='XPath':
				mydriver.find_element_by_xpath(butt['value'])
			return flag
		except:
			flag=False
			return flag
def getStr(mydriver,butt):
		flag=True	
		try:
			if butt['type']=='name':
				strget=mydriver.find_element_by_name(butt['value']).text
			elif butt['type']=='id':
				strget=mydriver.find_element_by_id(butt['value']).text 
			elif butt['type']=='class':
				strget=mydriver.find_element_by_class_name(butt['value']).text  
			elif butt['type']=='XPath':
				strget=mydriver.find_element_by_xpath(butt['value']).text
			print strget
			return strget
		except:
			flag=False
			return flag
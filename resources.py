from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
class Resources:
    def __init__(self,TargetUrl):
        self.BASEURL= TargetUrl
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.openUrl()
        self.driver.delete_all_cookies()
            
    def get_curr_url(self):
        return self.driver.current_url

    def check_url(self,text, Partial= False):
        if Partial == True:
            return True if text in self.get_curr_url() else False 
        return True if text == self.get_curr_url() else False 

    def is_element_exist(self,text,typeofelement):
        return True if len(self.get_elements_data(text,typeofelement)) > 0 else False

    def get_elements_data(self,text,typeofelement):
        if str(typeofelement).lower() == "partial_link_text":
            elements = self.driver.find_elements_by_partial_link_text(text)
        elif str(typeofelement).lower() == 'class':
            elements = self.driver.find_elements_by_class_name(text) 
        elif str(typeofelement).lower() == 'id':
            elements = self.driver.find_elements_by_id(text) 
        elif str(typeofelement).lower() == 'xpath':
            elements = self.driver.find_elements_by_xpath(text) 
        else:
            raise Exception('INVALID ARRUGMENT')
        return elements
    def remove_text_from_element(self,text, typeofelement):
        self.get_element_data(text,typeofelement).send_keys(Keys.CONTROL + 'a'+  Keys.BACKSPACE)

    def get_element_data(self,text,typeofelement):
        if str(typeofelement).lower() == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(text)
        elif str(typeofelement).lower() == 'class':
            element = self.driver.find_element_by_class_name(text) 
        elif str(typeofelement).lower() == 'id':
            element = self.driver.find_element_by_id(text) 
        elif str(typeofelement).lower() == 'xpath':
            element = self.driver.find_element_by_xpath(text) 
        else:
            raise Exception('INVALID ARRUGMENT')
        return element

    def press_button(self,role,data_testid):
        text= "//div[@role='{}' and @data-testid='{}']".format(role,data_testid)
        if self.is_element_exist(text,'xpath'): 
            self.get_element_data(text,'xpath').click()
        else:
            self.press_button(role,data_testid)
    
    def clearField(self,text):
        self.get_element_data(text,'xpath').send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
    
    def openUrl(self,url=''):
        self.driver.get(self.BASEURL+url)
    
    def driver_execute_script(self,scriptText):
        data = self.driver.execute_script(scriptText)
        if data is not None:
            return data
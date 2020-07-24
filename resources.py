from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
class Resources:
    WAITTIME = 2
    LONGWAITTIME = 5
    SHORTWAITTIME = 1
    VERYSHORTWAITTIME = 0.5
    def __init__(self,TargetUrl):
        """
    Controls a browser by sending commands to a remote server. A common Class which can se used by any Selenium work
    
    :Attributes:
     - TargetUrl : base url of the webdriver         
    """
        self.BASEURL= TargetUrl
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.openUrl()
        self.driver.delete_all_cookies()
            
    def get_curr_url(self):
        """
        Gets the URL of the current page.

        :Usage:
            driver.current_url
        """
        return self.driver.current_url

    def check_url(self,text, Partial= False):
        """
        Check Element exists or not

        :Args:
         - text - url which you want to compare.
         - Partial (Defailt value 'false')- check certian part of url if trur .

        :Returns:
         - true if element found, else false

        :Usage:
            element = driverObject.check_url('https://www.linkedin.com/')
            element = driverObject.check_url('https://www.linkedin.com/', True)
        """
        if Partial == True:
            return True if text in self.get_curr_url() else False 
        return True if text == self.get_curr_url() else False 

    def is_element_exist(self,text,typeofelement):
        """
        Check Element exists or not

        :Args:
         - text - The path of the element.
         - typeofelement - Type of element to search target .

        :Returns:
         - true if element found, else false

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driverObject.is_element_exist('foo', 'class')
            element = driverObject.is_element_exist('alert', 'class')
        """
        return True if len(self.get_elements_data(text,typeofelement)) > 0 else False

    def get_elements_data(self,text,typeofelement):       
        """
        Finds and return an elements

        :Args:
         - text - The path of the element.
         - typeofelement - Type of element to search target .

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driverObject.get_elements_data('foo', 'class')
            element = driverObject.get_elements_data('alert', 'class')
        """
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


    def get_element_data(self,text,typeofelement):
        """Finds and return an elements.

        :Args:
         - text - The path of the element.
         - typeofelement - Type of element to search target .

        :Returns:
         - WebElement - elements if found.

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driverObject.get_element_data('foo', 'class')
            element = driverObject.get_element_data('alert', 'class')
        """
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
#
    def press_button(self,role,data_testid):
        """Finds and Press the buttonz.

        :Args:
         - Role - Role value of Button.
         - data_testid - data_testid value of Button.

        :Returns:
         - No Return Type

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            driverObject.press_button('button', 'login')
        """

        text= "//div[@role='{}' and @data-testid='{}']".format(role,data_testid)
        if self.is_element_exist(text,'xpath'): 
            self.get_element_data(text,'xpath').click()
        else:
            self.press_button(role,data_testid)
    
    def clearField(self,text,typeofelement):
        """
        clear the field in the web element

        Example:
            webdriverObject.clearField(text, 'xpath')
            webdriverObject.clearField('//input[@id="username"]', 'xpath')
            webdriverObject.clearField('username', 'class')
            webdriverObject.clearField('username', 'id')
        
        Parameters:
            - > Accept Web element path as string type
            - > Type of element to search target  
        
        Return:
            No return type
        """
        self.get_element_data(text,typeofelement).send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
    
    def openUrl(self,url=''):
        """
        Open the url in Selenium Driver Browser

        Example:
            -> webdriverObject.openUrl()
            -> webdriverObject.openUrl('https://www.linkedin.com/')
        
        Parameters:
            Accept url as string type 
        
        Return:
            No return type
        """
        self.driver.get(self.BASEURL+url)
    
    def driver_execute_script(self,scriptText):
        """
        Excute the Java script in the browser

        Example:
            webdriverObject.time_sleep(5)
        
        Parameters:
            Accept javascipt command as string type  
        
        Return:
            only if function receive any value from javascript execution
        """
        data = self.driver.execute_script(scriptText)
        if data is not None:
            return data
    
    def driver_quit(self):
        """
        Close the Selenium Driver Browser  

        Example:
            webdriverObject.driver_quit()
        
        Parameters:
            Accept No Parameters 
        
        Return:
            No return type
        """
        self.driver.quit()
    
    def time_sleep(self,time):
        """
        Pause the driver for certian seconds

        Example:
            webdriverObject.time_sleep(5)
        
        Parameters:
            accept time as integer avlue to stop driver as Parameters 
        
        Return:
            No return type
        """
        sleep(time)
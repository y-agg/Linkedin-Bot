from selenium.common.exceptions import NoSuchElementException
import time
import sys
from resources import Resources
WAITTIME = 2
LONGWAITTIME = 5
SHORTWAITTIME = 1
VERYSHORTWAITTIME = 0.5

class LinkedinBot(Resources):
    def __init__(self,BASEURL):
        super().__init__(BASEURL)
        self.openUrl('login')
        self.username= input("Enter Username/Email:")
        self.password= input("Enter Password:")        
        self.no_of_connect= input("Enter no_of_connect:")        
        self.keyword = input("Enter Keyword/Text:")
        self.click_left = self.no_of_connect
        self.currrent_page = 1

    def press_button(self,typeText,aria_label):
        text= "//button[@type='{}' and @aria-label='{}']".format(typeText,aria_label)
        if self.is_element_exist(text,'xpath'): 
            self.clearField(text)
            self.get_element_data(text,'xpath').click()
        else:
            time.sleep(WAITTIME)
            self.press_button(typeText,aria_label)

    
    def login(self,id,data):
        text= '//input[@id="{}"]'.format(id)
        if self.is_element_exist(text,'xpath'): 
            self.get_element_data(text,'xpath').send_keys(data)
        else:
            time.sleep(WAITTIME)
            self.login(id,data)

    
    def start(self):
        if self.check_url(self.BASEURL+'login') == False:
            print('Not on Login Page // Redirecting to Login Page')
            self.openUrl("login")
        self.login('username', self.username)
        self.login('password', self.password)
        self.press_button('submit', 'Sign in')
        if self.check_url(self.BASEURL+'login', True) or self.check_url(self.BASEURL+'checkpoint/lg/login-submit', True):
            print("IVALID USERNAME AND PASSWORD")
            self.username= input('Enter Correct Username:')
            self.password= input('Enter Correct Password:')
            self.start()

    def search(self,page):
        self.openUrl('search/results/people/?keywords='+self.keyword+'&page='+str(page))
        
    def connect_click(self, connect_path):
        scrollHeight = 100
        while True:
            if self.click_left == 0:
                print(f'Invitation Sent To {self.no_of_connect} People // Program Terminated')
                sys.exit()
            connectList= self.get_elements_data(connect_path,'xpath')
            for i in connectList:
                if i.text == 'Connect':
                    i.click()
                    self.get_element_data('//button[@aria-label="Send now"]','xpath').click()
                    self.click_left = self.click_left - 1 
                    time.sleep(WAITTIME)

            self.driver_execute_script(f"window.scrollTo({scrollHeight},{scrollHeight+150})")
            scrollHeight+=150 
            if scrollHeight >= self.driver_execute_script("return document.body.scrollHeight"):
                self.currrent_page += 1
                break
    def page_search_and_click(self):
        connectButton = '//button[@data-control-name="srp_profile_actions" and @type="button"]' 
        while True:
            self.search(self.currrent_page)    
            time.sleep(WAITTIME)
            self.connect_click(connectButton)

if __name__ == "__main__":
    try:
        obj= LinkedinBot('https://www.linkedin.com/')
        time.sleep(WAITTIME)    
        obj.start()
        obj.page_search_and_click()
    except NoSuchElementException as e:
        print(f'ERROR FOUND-> {e}')
    except Exception as e:
        print(f'ERROR FOUND-> {e}')
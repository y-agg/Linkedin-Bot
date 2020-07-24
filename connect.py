from common import CommonElements

class LinkedinBot(CommonElements):
    def __init__(self,BASEURL):
        super().__init__(BASEURL)        
        self.no_of_connect= input("Enter no_of_connect:")        
        self.keyword = input("Enter Keyword/Text:")
        self.click_left = self.no_of_connect
        self.currrent_page = 1

    def press_button(self,typeText,aria_label):
        text= "//button[@type='{}' and @aria-label='{}']".format(typeText,aria_label)
        if self.is_element_exist(text,'xpath'): 
            self.clearField(text,'xpath')
            self.get_element_data(text,'xpath').click()
        else:
            self.time_sleep(self.WAITTIME)
            self.press_button(typeText,aria_label)
    
    def search(self,page):
        self.openUrl('search/results/people/?keywords='+self.keyword+'&page='+str(page))
        
    def connect_click(self, connect_path):
        scrollHeight = 100
        while True:
            if self.click_left == 0:
                print(f'Invitation Sent To {self.no_of_connect} People // Program Terminated')
                self.driver_quit()
            connectList= self.get_elements_data(connect_path,'xpath')
            for i in connectList:
                if i.text == 'Connect':
                    i.click()
                    self.get_element_data('//button[@aria-label="Send now"]','xpath').click()
                    self.click_left = self.click_left - 1 
                    self.time_sleep(self.WAITTIME)

            self.driver_execute_script(f"window.scrollTo({scrollHeight},{scrollHeight+150})")
            scrollHeight+=150 
            if scrollHeight >= self.driver_execute_script("return document.body.scrollHeight"):
                self.currrent_page += 1
                break

    def page_search_and_click(self):
        connectButton = '//button[@data-control-name="srp_profile_actions" and @type="button"]' 
        while True:
            self.search(self.currrent_page)    
            self.time_sleep(self.WAITTIME)
            self.connect_click(connectButton)
    
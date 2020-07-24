from resources import Resources

class CommonElements(Resources):
    def login(self,id,data):
        text= '//input[@id="{}"]'.format(id)
        if self.is_element_exist(text,'xpath'): 
            self.get_element_data(text,'xpath').send_keys(data)
        else:
            self.time_sleep(self.WAITTIME)
            self.login(id,data)
    
    def start(self,username,password):
        if self.check_url(self.BASEURL+'login') == False:
            print('Not on Login Page // Redirecting to Login Page')
            self.openUrl("login")
        self.login('username', username)
        self.login('password', password)
        self.press_button('submit', 'Sign in')
        if self.check_url(self.BASEURL+'login', True):
            print("IVALID USERNAME AND PASSWORD")
            username= input('Enter Correct Username:')
            password= input('Enter Correct Password:')
            self.start(username,password)

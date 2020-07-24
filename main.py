from selenium.common.exceptions import NoSuchElementException
from connect import LinkedinBot

if __name__ == "__main__":
    try:
        username= input("Enter Username/Email:")
        password= input("Enter Password:")        
        obj= LinkedinBot('https://www.linkedin.com/')
        obj.time_sleep(2)    
        obj.start(username,password)
        obj.page_search_and_click()
    except NoSuchElementException as e:
        print(f'NoSuchElementException -> {e}')
    except Exception as e:
        print(f'ERROR FOUND-> {e}')

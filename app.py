from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint, random
from selenium.webdriver.common.by import By

class CloudTest:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        #test account login: with provided credentials
        #
        bot = self.bot
        #bot.get('appurl')
        bot.get('appurl')
        time.sleep(randint(5,15))

        
        user_email = bot.find_element(By.NAME, "username")
        user_password = bot.find_element(By.NAME, "password")
        user_email.clear()
        user_password.clear()
        user_email.send_keys(self.email)
        user_password.send_keys(self.password)
        user_password.send_keys(Keys.RETURN)
        time.sleep(3)
        
        
account_email = ""
account_password = ""
ceh = CloudTest(account_email, account_password)
try:
    ceh.login()
except Exception as e:
    print(e)

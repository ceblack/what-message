#!/usr/bin/env python3
import sys
import os
import time
import env
from utils import behavior
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Facebook():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        self.action = ActionChains(self.driver);

    def login(self):
        self.driver.get('https://www.messenger.com/')
        behavior.sleep_random(3)

        username_box = self.driver.find_element_by_id('email')
        username_box.send_keys(self.username)
        print('sent user')
        behavior.sleep_random(2)

        password_box = self.driver.find_element_by_id('pass')
        password_box.send_keys(self.password)
        print('sent pass')
        behavior.sleep_random(2)

        login_box = self.driver.find_element_by_id('loginbutton')
        login_box.click()
        print('clicked login')
        behavior.sleep_random(300)

        self.driver.quit()



if __name__ == '__main__':
    f = Facebook('devs@oscillas.com', 'horsebatterystaple')
    f.login()

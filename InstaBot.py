from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        print("Connecting to Instagram login page...")
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        print("Connected.")
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        print("Entered the username.")
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        print("Entered the password.")
        password_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        print("Navigated to Instagram profile.")
        # notnow_elem = driver.find_element_by_css_selector("button[class='aOOlW   HoLwm ']")
        # notnow_elem.click()
        # time.sleep(2)
        # print("Clicked 'Not now' button.")


# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.rcvacademy.com")
        #to get the text from the web element use .text
        text = driver.find_element(By.XPATH, "//a[normalize-space()='AUTOMATION PRACTICE PAGE']").text
        print(text)
        time.sleep(2)



findbyid = DemoGetText()
findbyid.demo_gettext()
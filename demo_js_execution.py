# HOW TO EXECUTE JAVASCRIPT IN SELENIUM

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoJS():
    def demo_JavaScript(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.get("https://training.rcvacademy.com/")
        # driver.maximize_window()
        # time.sleep(4)

        #to execute using js code
        #driver.execute_script("window.open('https://training.rcvacademy.com/');") # => this will launch chrome
        # and open the url in the second tab
        #time.sleep(8)
        # always end the js code using semi-colon

        # to open the url in the same tab
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(8)

        demo_element = driver.execute_script("return document.getElementsByTagName('a')[8];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(2)


demoJS = DemoJS()
demoJS.demo_JavaScript()
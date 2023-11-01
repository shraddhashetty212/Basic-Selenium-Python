# IMPLICIT WAIT IN SELENIUM PYTHON

#LINK : https://www.selenium.dev/documentation/webdriver/waits/

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoImplicitwait():
    def demo_implicit_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=au")
        driver.maximize_window()
        #if the web element is present then it will not wait for 10 seconds or the time mentioned in implicit wait
        driver.find_element(By.ID, "username").send_keys("RCV Academy")
        #lets put a wrong webelement for password field
        driver.find_element(By.ID, "pwwdd").send_keys("RCV")
        # this will wait for 10 seconds to check if the element is present
        #after 10 seconds it will fail and throw error that element is not present


impwait = DemoImplicitwait()
impwait.demo_implicit_wait()

# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoElementState():
    def demo_enable_disbale(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.openspan.com/login")
        #if this particular web element is enables then it will return true
        #if its disabled then it will return false
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state) # here its false because its disabled
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("testing123")
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state1) # here its true bcz its enabled after entering username and password
        time.sleep(2)



attr_obj = DemoElementState()
attr_obj.demo_enable_disbale()
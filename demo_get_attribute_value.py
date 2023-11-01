# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoGetAttributeValue():
    def demo_getvalue(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.rcvacademy.com")
        #to get the value from the web element use .get_attribute(<name of the attribute>)
        #you can get the value of the attribute like class, id, value, href etc using this
        attr_value = driver.find_element(By.XPATH, "//a[normalize-space()='Get Access']").get_attribute("class")
        print(attr_value)
        time.sleep(2)



attr_obj = DemoGetAttributeValue()
attr_obj.demo_getvalue()
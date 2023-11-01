# LINK : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropDown():
    def demo_drop_down(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/de/form/signup/freetrial-sales-pe/?d=70130000000EqoP")
        driver.maximize_window()
        time.sleep(4)

        #reject cookies button
        driver.find_element(By.XPATH, "//button[@id='onetrust-reject-all-handler']").click()

        dropdwn = driver.find_element(By.NAME, "CompanyEmployees")
        dd = Select(dropdwn) # it will check if the element that you passed inside braces is a select tag or not
        #if its not select tag then it will give unexpected tag name exception
        dd.select_by_index(1)
        time.sleep(3)

        dropdwn1 = driver.find_element(By.NAME, "CompanyCountry")
        dd1 = Select(dropdwn1)
        dd1.select_by_value("DZ")
        time.sleep(3)

        dropdwn2 = driver.find_element(By.NAME, "CompanyLanguage")
        dd2 = Select(dropdwn2)
        dd2.select_by_visible_text("Deutsch")
        time.sleep(3)



dropdown_demo = DemoDropDown()
dropdown_demo.demo_drop_down()

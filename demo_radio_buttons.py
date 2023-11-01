# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoRadioButtons():
    def demo_radio_buttons(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://test.rubywatir.com/radios.php")
        driver.maximize_window()
        time.sleep(4)

        #prior to clicking the radio-button, we are checking if its selcted
        print(driver.find_element(By.ID, "radioId").is_selected()) # false
        #clicking on "Two" radio-button
        driver.find_element(By.ID, "radioId").click()
        time.sleep(4)
        print(driver.find_element(By.ID, "radioId").is_selected()) # true

        #prior to clicking 2nd radio-button, checking if its selected
        print(driver.find_element(By.XPATH, "//input[@value='Radio1']").is_selected()) # false
        driver.find_element(By.XPATH, "//input[@value='Radio1']").click()
        time.sleep(4)


radiobuttons = DemoRadioButtons()
radiobuttons.demo_radio_buttons()

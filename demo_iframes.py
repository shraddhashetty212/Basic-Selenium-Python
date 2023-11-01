# HOW TO HANDLE FRAMES IN SELENIUM PYTHON

#LINK : https://selenium-python.readthedocs.io/api.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoIFrame():
    def demo_iframe(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.agoda.com/en-gb/account/signin.html")
        driver.maximize_window()
        time.sleep(4)

        #switch to iframe using the xpath of the block of the frame
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Universal login']"))
        #driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='sc-AxgMl mXdik fade-in-enter-done']"))


        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)


d_iframe = DemoIFrame()
d_iframe.demo_iframe()


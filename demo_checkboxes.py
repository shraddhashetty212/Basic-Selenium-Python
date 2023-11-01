# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoCheckBoxes():
    def demo_check_box(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.sugarcrm.com/au/request-demo/")

        #click on Cookie settings
        driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonCustomize']").click()
        time.sleep(2)
        #click on Accept Selected Cookies
        driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyButtonDecline']").click()
        time.sleep(2)

        #to select the checkbox
        driver.find_element(By.ID, "doi0").click()
        time.sleep(2)

        # to verify if its selected
        # will display True if its selected and False if its not selected
        var1 = driver.find_element(By.ID, "doi0").is_selected()
        print(var1)

checkbox = DemoCheckBoxes()
checkbox.demo_check_box()


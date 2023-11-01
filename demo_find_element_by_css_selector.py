# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByCSSDemo():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://google.com")
        #driver.get("chrome://settings/clearBrowserData")
        reject_all = driver.find_element(By.ID, "W0wltc")
        reject_all.click()
        search_box = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
        search_box.send_keys("python")
        time.sleep(4)


findbyid = FindElementByCSSDemo()
findbyid.locate_by_id_demo()
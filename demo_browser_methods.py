# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #driver.get("https://google.com")
        #driver.get("chrome://settings/clearBrowserData")
        # reject_all = driver.find_element(By.ID, "W0wltc")
        # reject_all.click()
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        driver.minimize_window()
        time.sleep(4)
        driver.quit()
        # search_button = driver.find_element(By.CLASS_NAME, "QCzoEc z1asCe MZy1Rb")
        # search_button.click()



demobrowser = DemoSeleniumLearning()
demobrowser.demo_browser_methods()
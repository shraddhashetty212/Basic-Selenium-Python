# HOW TO HANDLE MOUSE HOVER IN SELENIUM PYTHON

#LINK : https://www.w3schools.com/js/js_popup.asp
#LINK : https://selenium-python.readthedocs.io/api.html  (search action chains i.e. 7.2 section)

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoMouseHover():
    def demo_mouse_hover(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
        driver.maximize_window()
        time.sleep(4)

        hover_img = driver.find_element(By.XPATH, "//button[@id='developers-dd-toggle']")
        achains = ActionChains(driver)
        # .perform() is mandatory when using ActionChains otherwise it will not execute
        # this method is basically telling to execute all the actions one  by one
        achains.move_to_element(hover_img).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@title='Open Source']").click()
        time.sleep(3)


dmouse = DemoMouseHover()
dmouse.demo_mouse_hover()

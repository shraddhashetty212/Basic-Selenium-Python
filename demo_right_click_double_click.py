# HOW TO HANDLE RIGHT CLICK AND DOUBLE CLICK IN SELENIUM PYTHON

#LINK : https://www.w3schools.com/js/js_popup.asp
#LINK : https://selenium-python.readthedocs.io/api.html  (search action chains i.e. 7.2 section)

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoRightClickDoubleClick():
    def demo_right_double_click(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(4)

        #reject all button
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='gdpr-consent-notice']"))
        driver.find_element(By.XPATH, "//button[normalize-space()='Reject All']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Reject']").click()
        driver.switch_to.parent_frame()

        # RIGHT CLICK
        # achains = ActionChains(driver)
        # right_click_btn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # copy_in_right_click_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        # achains.context_click(right_click_btn).perform()
        # time.sleep(3)
        # copy_in_right_click_btn.click()
        # time.sleep(2)

        # DOUBLE CLICK
        achains = ActionChains(driver)
        double_click_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(double_click_btn).perform()
        time.sleep(2)


drightdoubleclick = DemoRightClickDoubleClick()
drightdoubleclick.demo_right_double_click()


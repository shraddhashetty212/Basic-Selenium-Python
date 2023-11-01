# HOW TO HANDLE ALERTS IN SELENIUM PYTHON

#LINK : https://www.w3schools.com/js/js_popup.asp
#LINK : https://selenium-python.readthedocs.io/api.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoHandleAlerts():
    def demo_handle_alerts(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://nxtgenaiacademy.com/alertandpopup/")
        driver.maximize_window()
        time.sleep(4)

        # Accept the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Alert Box']").click()
        time.sleep(2)
        #to click on OK in the alert pop-up
        driver.switch_to.alert.accept()
        time.sleep(2)

        # Cancel the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Alert Box']").click()
        time.sleep(2)
        # to click on cancel in the alert pop-up
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        # Send text in alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Prompt Alert Box']").click()
        time.sleep(2)
        #to get the text displayed in the pop-up
        print(driver.switch_to.alert.text)
        #to enter text in the prompt alert
        driver.switch_to.alert.send_keys("Shraddha")
        time.sleep(4)
        # to press OK in the same prompt after entering text
        driver.switch_to.alert.accept()
        #this above line can also be written as Alert(driver).accept() by importing the Alert class


demo_alert_handle = DemoHandleAlerts()
demo_alert_handle.demo_handle_alerts()

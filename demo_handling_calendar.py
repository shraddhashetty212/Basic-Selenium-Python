# LINK : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoHandlingCalendar():
    def demo_handling_calendar(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.edreams.com/")
        driver.maximize_window()
        time.sleep(4)

        #cookies
        driver.find_element(By.XPATH, "//span[@role='button']").click()

        # 1ST APPROACH
        #departure date selection from the calendar
        driver.find_element(By.XPATH, "//input[@placeholder='Departure']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='odf-calendar-day'][normalize-space()='2']").click()
        time.sleep(2)





demo_calendar = DemoHandlingCalendar()
demo_calendar.demo_handling_calendar()

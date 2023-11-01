# LINK : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoScreenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://demo.t3-framework.org/joomla30/index.php/en/joomla-pages/sample-page-2/login-page")
        driver.maximize_window()
        time.sleep(4)

        sign_in_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
        sign_in_button.screenshot("./test.png") # => dot is current directory that is Learn Selenium
        sign_in_button.click()
        time.sleep(2)
        driver.get_screenshot_as_file("/Users/shraddhashetty/python-selenium/error.png")
        driver.save_screenshot("./testerror.png")


demo_screenshot = DemoScreenshot()
demo_screenshot.demo_screen_capture()


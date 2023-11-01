# HOW TO HANDLE MULTIPLE WINDOWS IN SELENIUM

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoMultipleWindows():
    def demo_multiple_windows(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.makemytrip.com/hotels/")
        driver.maximize_window()
        time.sleep(4)

        #to get the window handle of the current/parent window that is opened
        parent_handle = driver.current_window_handle
        print(parent_handle)

        driver.find_element(By.XPATH, "//li[@class='makeFlex perfectCenter makeRelative']").click()
        all_handles = driver.window_handles
        print(all_handles)
        time.sleep(3)

        for handle in all_handles:
            if handle != parent_handle:
                #switching to second window
                driver.switch_to.window(handle)
                #clicking on link which will open third window
                driver.find_element(By.XPATH, "//p[normalize-space()='#DealsOnWheels: Get Up to Rs. 40 OFF* on Train']").click()
                time.sleep(4)
                #closing the second window
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//li[@class='makeFlex perfectCenter makeRelative']").click()



demo_multi_wind = DemoMultipleWindows()
demo_multi_wind.demo_multiple_windows()


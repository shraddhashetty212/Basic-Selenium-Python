# HOW TO HANDLE SLIDERS IN SELENIUM PYTHON

#LINK : https://selenium-python.readthedocs.io/api.html (action chains)

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoSliders():
    def demo_handle_sliders(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.snapdeal.com/search?keyword=mobile%20phones&sort=plrty")
        driver.maximize_window()
        time.sleep(2)

        low_price_handle = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        high_price_handle = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")


        # MOVING LOW PRICE HANDLE SLIDER TO RIGHT SIDE
        #1ST METHOD
        # sliding through drag and drop using offset by sliding 60 pixels horizontally
        # ActionChains(driver).drag_and_drop_by_offset(low_price_handle, 60, 0).perform()
        # time.sleep(2)

        #2ND METHOD
        # ActionChains(driver).click_and_hold(low_price_handle).pause(1).move_by_offset(50, 0).release().perform()
        # time.sleep(3)

        #3RD METHOD
        # ActionChains(driver).move_to_element(low_price_handle).pause(1).click_and_hold(low_price_handle).move_by_offset(80, 0).release().perform()
        # time.sleep(3)


        # MOVING HIGH PRICE HANDLE SLIDERS TO LEFT SIDE
        #1ST METHOD
        ActionChains(driver).drag_and_drop_by_offset(high_price_handle, -40, 0).perform()
        time.sleep(2)


demo_sliders = DemoSliders()
demo_sliders.demo_handle_sliders()
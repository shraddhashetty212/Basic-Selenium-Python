# LINK : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoAutoSuggest():
    def demo_auto_suggest(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.edreams.com/")
        driver.maximize_window()
        time.sleep(4)

        #cookies
        driver.find_element(By.XPATH, "//span[@role='button']").click()

        #to select directly using full text and clicking on enter
        depart_from = driver.find_element(By.XPATH, "//input[@placeholder='Where from?']")
        depart_from.send_keys("New Delhi")
        time.sleep(4)
        depart_from.send_keys(Keys.ENTER) # => for any keys in the keyboard
        time.sleep(4)

        #selecting from the search result displayed when typing "New"
        arrival_to = driver.find_element(By.XPATH, "//input[@placeholder='Where to?']")
        arrival_to.send_keys("New")
        time.sleep(4)
        search_results = driver.find_element(By.XPATH, "//div[@class='odf-box odf-box-layer odf-popup odf-popup-flex odf-space-outer-top-xs opened css-5ofyg9']//ul//li")
        #print(len(search_results))
        for results in search_results:
            if "John F Kennedy Intl Airport" in results.text:
                results.click()
                time.sleep(4)
                break

demo_auto = DemoAutoSuggest()
demo_auto.demo_auto_suggest()

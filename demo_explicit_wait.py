# EXPLICIT  WAIT IN SELENIUM PYTHON

#LINK : https://www.selenium.dev/documentation/webdriver/waits/
#LINK : https://www.selenium.dev/documentation/webdriver/support_features/expected_conditions/

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoExplicitWait():
    def demo_explicit_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.edreams.com/")
        driver.maximize_window()

        #cookies
        #driver.find_element(By.XPATH, "//span[@role='button']").click()

        #to select directly using full text and clicking on enter
        depart_from = driver.find_element(By.XPATH, "//input[@placeholder='Where from?']")
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER) # => for any keys in the keyboard

        #selecting from the search result displayed when typing "New"
        arrival_to = driver.find_element(By.XPATH, "//input[@placeholder='Where to?']")
        arrival_to.send_keys("New")

        #explicit wait
        #wait = WebDriverWait(driver, 10)

        #fluent wait
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[TypeError])

        search_results = driver.find_element(By.XPATH, "//div[contains(@class,'odf-box odf-box-layer odf-popup odf-popup-flex odf-space-outer-top-xs opened css-5ofyg9')]//ul")
        print(search_results)
        wait.until(EC.visibility_of_element_located(search_results))
        for results in search_results:
            print(results.text)
            if "JFK - John F Kennedy Intl Airport" in results.text:
                results.click()
                break

expwait = DemoExplicitWait()
expwait.demo_explicit_wait()

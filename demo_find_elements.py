# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementsDemo():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://google.com")
        #driver.get("chrome://settings/clearBrowserData")
        reject_all = driver.find_element(By.ID, "W0wltc")
        reject_all.click()
        list_of_elements = driver.find_elements(By.TAG_NAME, "a")
        #list_of_elements1 = driver.find_elements(By.TAG_NAME, "textarea")
        print(len(list_of_elements))
        for i in list_of_elements:
            print(i.text)  # => to print the elements in the list which has anchor tag
        #print(len(list_of_elements1))
        #search_box = driver.find_element(By.TAG_NAME,"textarea")
        #partial_link_check = driver.find_element(By.PARTIAL_LINK_TEXT, "Google in Deutschla").click()
        time.sleep(4)

# find_elements will provide a list so instead of fully printing the list,
# we can just see how many elements of that tag name are there in the page using length function.
# So len(list_of_elements) will give the count of elements in the page with anchor <a> tag
# len(list_of_elements1) will give the count of elements in the page with input <textarea> tag



findbyid = FindElementsDemo()
findbyid.locate_by_id_demo()
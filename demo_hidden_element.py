# LINK : https://selenium-python.readthedocs.io/locating-elements.html

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoHiddenElements():
    def demo_is_displayed_w3schools(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        #to accept cookies in the page
        driver.find_element(By.ID, "accept-choices").click()

        #once the page loads, if this element is present then this will display True
        #to verify if the element is displayed or not, we can use .is_displayed()
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)


        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

        #once the hide button is clicked on the page, we are verifying here if the block in the page
        # is displayed or not
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)


    def demo_is_displayed_agoda(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.agoda.com/en-gb/")

        #click on adding people
        driver.find_element(By.XPATH, "//div[@class='SearchBoxTextDescription SearchBoxTextDescription--occupancy']").click()
        #click on + for children
        driver.find_element(By.XPATH, "//div[3]//div[2]//div[3]//*[name()='svg']").click()
        #verifying if age of child section will be enabled and visible
        elem2 = driver.find_element(By.XPATH, "//span[@class='sc-jrAGrp sc-kEjbxe eDlaBj diTPKs']").is_displayed()
        print(elem2)

        #click on - for childer
        driver.find_element(By.XPATH, "//div[contains(@class,'Box-sc-kv6pi1-0 hRUYUu')]//div[3]//div[2]//div[1]").click()
        #now verifying that the age of child section will be gone completely
        elem3 = driver.find_element(By.XPATH, "//span[@class='sc-jrAGrp sc-kEjbxe eDlaBj diTPKs']").is_displayed()
        print(elem3)



demoDisplayed = DemoHiddenElements()
demoDisplayed.demo_is_displayed_w3schools()
demoDisplayed.demo_is_displayed_agoda()

# for the example with agoda, we will get exception because the "age of child" section or DOM
# will be completed removed from the page so there will be no element to search or find.
# so it will throw exception rather than returning false
# in w3schools example, the block was just hidden when we clicked the button but the DOM
#or the section element would still be there so it will return True or False based on
# whether its getting displayed there or not.

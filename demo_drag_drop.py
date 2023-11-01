# HOW TO PERFORM DRAG AND DROP IN SELENIUM PYTHON

#LINK : https://selenium-python.readthedocs.io/api.html (action chains)

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDragAndDrop():
    def demo_drag_drop(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(4)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        draggable_elem = driver.find_element(By.ID, "draggable")
        droppable_elem = driver.find_element(By.ID, "droppable")
        # just drag and drop from start to target
        #ActionChains(driver).drag_and_drop(draggable_elem, droppable_elem).perform()
        #drag and drop using offset (that is anywhere on the screen using x and y axis)
        # they are not the actual coordinates. they are the distance from the draggable item in the x and y axis
        ActionChains(driver).drag_and_drop_by_offset(draggable_elem, 419, 238).perform()
        time.sleep(4)


dragdropdemo = DemoDragAndDrop()
dragdropdemo.demo_drag_drop()




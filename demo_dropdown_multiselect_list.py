# LINK : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropDownMultiSelectList():
    def demo_drop_down_multiselect(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.mobiscroll.com/select/multiple-select")
        driver.maximize_window()
        time.sleep(4)

        multi_select_box = driver.find_element(By.ID, "multiple-select-select")
        dd_multi = Select(multi_select_box)

        dd_multi.select_by_index(1)
        time.sleep(2)
        dd_multi.select_by_value(3)
        time.sleep(2)
        dd_multi.select_by_visible_text("Clothing & Jewelry")
        time.sleep(2)
        dd_multi.select_by_index(7)
        time.sleep(2)
        dd_multi.select_by_value(6)
        time.sleep(2)
        dd_multi.select_by_visible_text("Books")
        time.sleep(2)

        #deselecting the list
        dd_multi.deselect_by_index(1)
        dd_multi.deselect_by_value(3)
        dd_multi.deselect_by_visible_text("Clothing & Jewelry")
        dd_multi.deselect_all()
        time.sleep(4)


demo_multiselect = DemoDropDownMultiSelectList()
demo_multiselect.demo_drop_down_multiselect()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TopNavSearch:

        def __init__(self, driver):
                self.driver = driver

        def runSearch (self, query):
                self.driver.find_element(By.ID, "input-search").click()
                self.driver.find_element(By.ID, "input-search").send_keys(query)
                self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
                assert "No results found." not in self.driver.page_source
                self.driver.implicitly_wait(10)
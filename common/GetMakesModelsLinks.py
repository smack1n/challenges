from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from array import *

class GetMakesModelsLinks:
    def __init__ (self, driver):
        self.driver = driver

    def getlinks(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        n = len(elements)
        m = 2
        array = [[0 for x in range(m)] for y in range(n)]
        i = 0
        for item in elements:
            j = 0
            array[i][j] = item.text
            j = j+1
            array[i][j] = item.get_attribute("href")
            i = i + 1
        return array

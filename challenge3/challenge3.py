import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        #self.driver.implicitly_wait(10)

        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")

        for item in elements:
            print(item.text + " - " + item.get_attribute("href"))

if __name__ == '__main__':
    unittest.main()
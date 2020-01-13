import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
        print("")
        print("Tear down")

    def test_challenge3(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)

        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")

        print(len(elements))

        #for item in elements:
         #   print(item.text + " - " + item.get_attribute("href"))

        i = 0
        while i < len(elements):
            print(elements[i].text + " - " + elements[i].get_attribute("href"))

            i += 1

if __name__ == '__main__':
    unittest.main()
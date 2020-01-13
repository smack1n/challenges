import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class slingChannels(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
        print("")
        print("Tear down")


    def test_slingChannels(self):
        self.driver.get("https://help.sling.com/")
        self.assertIn("Help Center", self.driver.title)

        self.driver.find_element(By.ID, "support-search-input").click()

        self.driver.find_element(By.ID, "support-search-input").send_keys("roku")

        self.driver.find_element_by_xpath("//div[2]/button").send_keys(Keys.RETURN)

        self.driver.implicitly_wait(10)

        elements = self.driver.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/section")

        number = len(elements)
        print("Number of subjects: ",number)

        for item in elements:

            print(" - ", item.text)

if __name__ == '__main__':
    unittest.main()

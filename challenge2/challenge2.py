import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
        print("Tear down")

    def test_challenge2(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)

        self.driver.find_element(By.ID, "input-search").click()
        self.driver.find_element(By.ID, "input-search").send_keys("exotics")

        self.driver.find_element_by_xpath("//div[2]/button").click()
        self.driver.find_element_by_xpath("//div[2]/button").send_keys(Keys.RETURN)
        assert "No results available" not in self.driver.page_source
        self.driver.implicitly_wait(10)

        car = self.driver.find_element_by_xpath("// *[text() = 'PORSCHE']").text
        assert (car == "Porsche"), print("Porsche available")

if __name__ == '__main__':
    unittest.main()

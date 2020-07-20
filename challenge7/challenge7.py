import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.GetMakesModelsLinks import GetMakesModelsLinks
import time

class challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.implicitly_wait(10)
        s = GetMakesModelsLinks(self.driver)
        ListLinkarray = s.getlinks()
        print(len(ListLinkarray))
        i = 0
        while i < len(ListLinkarray):
            print(ListLinkarray[i][1])
            try:
                self.driver.get(ListLinkarray[i][1])
                WebDriverWait(self.driver, 60).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, '//img[@alt="Copart"]')))
            except TimeoutError:
                print("ERROR: {}'s link ({}) timed out".format(ListLinkarray[i][0], ListLinkarray[i][1]))
            i += 1
            time.sleep(2)
if __name__ == '__main__':
    unittest.main()
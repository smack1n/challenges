import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class slingChannels(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
        print("")
        print("Tear down")

    def test_slingChannels(self):
        self.driver.get("https://www.sling.com/")
        self.assertIn("Live TV Streaming | Sling TV", self.driver.title)
        self.driver.implicitly_wait(10)

        elements = self.driver.find_elements_by_xpath("//*[@id=\"channelList\"]/li/img")

        number = len(elements)

        print("Number of channels in Orange pack: ", number)
        #for item in elements:
         #   print(item.get_attribute("title"))

        i = 0
        while i < len(elements):
            print(elements[i].text + " - " + elements[i].get_attribute("title"))

            i += 1



if __name__ == '__main__':
    unittest.main()

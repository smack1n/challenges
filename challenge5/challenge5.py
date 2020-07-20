import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.TopNavSearch import TopNavSearch
import time

class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')

    def test_checkForModel(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)
        self.driver.implicitly_wait(10)

        query = "Porsche"
        TopNavSearch(self.driver).runSearch(query)

        self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//option[@value='100']").click()
        self.driver.implicitly_wait(10)
        time.sleep(30)

        all_models = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")

        models_damage = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotdamagedescription']")

        print(len(models_damage))

        damagetype = []
        for damage in models_damage:
            damagetype.append(damage.text)

        #print(damagetype)

        print("\n" + "Total Models:" + "\n")

        print(len(all_models))

        models = []
        for model in all_models:

            models.append(model.text) #adds model to models list

        #print(models)

        uniquemodelset = set(models) #removes duplicates using set

        print(len(uniquemodelset)) #check removal of duplicates

        uniquemodeldict = {str(list(uniquemodelset)[0]): 0}

        #print(uniquemodeldict)

        for unique_model in uniquemodelset:
            uniquemodeldict.update({unique_model: 0})

        #print(uniquemodeldict)

        for unique_model in uniquemodelset:
            for model in models:
                if model == unique_model:
                    uniquemodeldict[unique_model] += 1

            print("There are " + str(uniquemodeldict[unique_model]) + " " + unique_model + " on the page.")


    def tearDown(self):
        self.driver.close()
        print("Tear down")

if __name__ == '__main__':
    unittest.main()
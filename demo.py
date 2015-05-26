import unittest
import keywords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class testcases(unittest.TestCase):
    def setUp(abc):
        # driver = webdriver.Chrome('/home/local/OPTIMUSDOM/ubuntu30/Desktop/python/chromedriver')
        abc.driver = webdriver.Firefox()
    def test_case1(abc):
        driver = abc.driver
        data.open_browser(driver)
        data.click_by_id(driver)
    def tearDown(abc):
        abc.driver.close()
if __name__ == "__main__":
    # del data
    data = keywords.KeyWord()
    unittest.main()

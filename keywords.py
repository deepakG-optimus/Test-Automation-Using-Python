# import arcgisscripting
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import testData

class KeyWord:
    def __init__(self):
        pass
        sys.stdout.write("Download progress")
    def click_by_xpath(self,driver):
        try:
            print "test case execution start"
            sign_up = driver.find_element_by_xpath(testData.sign_button)
            sign_up.click()
            email_field = driver.find_element_by_xpath(testData.email_field)
            email_field.click()
            email_field.send_keys(testData.email)
        except Exception as inst:
            print inst
    def window_handling(self,driver):
        try:
            driver.get(testData.cbse_Url)
            driver.switch_to_frame(testData.frame_Name)
            hindi_Link = driver.find_element_by_xpath(testData.hindi_Link)
            hindi_Link.click()
        except Exception as inst:
            print inst
    def click_by_id(self,driver,Id):
        try:
            search_Field = driver.find_element_by_id(Id)
            search_Field.click()
            search_Field.send_keys(testData.search_data)
        except Exception as inst:
            print inst
    def send_key(self,driver,data):
        try:
            search_Field.send_keys(data)
        except Exception as inst:
            print inst
    def open_browser(self,driver,Url):
        try:
            driver.get(Url)
        except Exception as inst:
            print inst

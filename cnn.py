# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:12:09 2018

@author: ktm
"""
#%%
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import lxml
from selenium import webdriver
import time

url='https://edition.cnn.com/search/?q=trump'
start=time.time()

driver=webdriver.Chrome('chromedriver')
driver.get(url)


#xpath=driver.find_element_by_xpath('//*[@id="search-input-field"]')
#xpath.send_keys("trump")
#xpath.send_keys(Keys.RETURN)

#trump_xpath=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/h3/a')
#print(trump_xpath.text)


trump_xpath=driver.find_element_by_class_name('cnn-search__result-headline')
print(trump_xpath.text)


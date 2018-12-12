# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:25:16 2018

@author: ktm
"""
##pip install selenium
##chrome driver install
from bs4 import BeautifulSoup
import requests as rq
import lxml
from selenium import webdriver
import os
os.getcwd()
os.chdir("C:\choidontouch\web crawling")
driver = webdriver.Chrome("chromedriver")
url = 'https://naver.com'
driver.get(url)

selected_id=driver.find_element_by_id('user-content-id01')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.find_element_by_class_name)


#%%
from bs4 import BeautifulSoup
import requests as rq
import lxml
from selenium import webdriver
import os
os.getcwd()
os.chdir("C:\choidontouch\web crawling")
driver = webdriver.Chrome("chromedriver")
url = 'https://news.naver.com/'
driver.get(url)

selected_id=driver.find_element_by_id('u_skip')
print(selected_id.tag_name)
selected_tag=driver.find_elements_by_tag_name('strong')
#print(selected_tag.text)
for i in selected_tag:
    print(selected_tag)

selected_class=driver.find_element_by_class_name()

#%%
from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
url = 'https://finance.naver.com/'
driver.get(url)

selected_class=driver.find_elements_by_class_name('tx')
#print(selected_class)
#print(selected_class.text)
#print(selected_class.tag_name)
selected_class[6].click()

#%% text박스에 정보를 보내고 enter를 누르기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("chromedriver")
url = 'https://www.naver.com/'
driver.get(url)

select_xpath=driver.find_element_by_xpath('//*[@id="query"]')
select_xpath.send_keys("컨볼루션")
select_xpath.send_keys(Keys.RETURN)





# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:17:32 2018

@author: ktm
"""
#%%
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N")
html = driver.page_source
html
#%%


soup = BeautifulSoup(html)




prodList = soup.find_all("p", {"class": "prodPrice"})
print(len(prodList))
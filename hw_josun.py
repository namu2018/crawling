# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:19:53 2018

@author: ktm
"""
#%%
from bs4 import BeautifulSoup
import requests as rq
import lxml
import os
import datetime

sdate = datetime.date.today() - datetime.timedelta(days = 7) #검색할 날짜 범위, 시작날짜(오늘로부터 7일 전)
edate = datetime.date.today() #검색할 날짜 범위, 끝날짜(오늘)
query = '트럼프' #검색할 키워드

url = 'http://search.chosun.com/search/news.search'
params = {
    'query':query, #검색할 키워드
    'pageno':0, #페이지 번호
    'orderby':'docdatetime', #정렬 순서(최신순)
    'sdate':sdate.strftime('%Y.%m.%d'), #시작날짜
    'edate':edate.strftime('%Y.%m.%d'), #끝날짜
}
r = rq.get(url, params)

print(r.content)


#%%
soup = BeautifulSoup(r.content, 'lxml')
print(soup)


#%%
soup2 = soup.find('div',attrs={'class':'search_news_box'}) #<section class="result news"> 가져오기
# for article in soup2.findAll('dd',attrs={'class':'thumb'}):
print(soup2)


#%%
for article in soup2.find_all('dl'):
    print (article.dt.a['href']) #기사 URL
    print (article.dt.a.text) #기사 제목

#%%
i = 0
item = []
for i in range(0,10):
    i = i + 1
    url = "http://search.chosun.com/search/news.search?query=%ED%8A%B8%EB%9F%BC%ED%94%84&pageno="+str(i)+"&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=paging&sdate=&edate=&premium="
    item.append(url)
    
print(item)
#%%
from bs4 import BeautifulSoup
import requests as rq


a_url = []
a_text=[]
soup_tr=[]
num=len(item)
for i in range(0, num):
    res = rq.get(item[i])
    soup = BeautifulSoup(res.content, 'lxml')
    soup_tr =soup.find_all('dl')
    for item_dt in soup_tr:
        a_url.append(item_dt.dt.a['href'])
        a_text.append(item_dt.dt.a.text)
a_url
a_text        
#%%        
        
import pandas as pd

a_url1=pd.Series(a_url)
a_text1=pd.Series(a_text)

#%%
dat=pd.DataFrame({"a_url":a_url,
                  "a_text":a_text}, columns=['a_url','a_text'])

dat.to_csv("chosun2.csv", index=False, encoding="utf-8")
dat
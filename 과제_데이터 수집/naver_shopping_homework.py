# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:41:55 2018

@author: USER
"""
#%%
import requests as rq
from bs4 import BeautifulSoup
import lxml

item =[]
for i in range(1,5):
    url = "https://search.shopping.naver.com/search/all.nhn?origQuery={}&pagingIndex={}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query={}".format("치즈",i,"치즈")
    item.append(url)

print(item)
#res = rq.get(url_bundle)
#res.url
#html = res.text
#soup = BeautifulSoup(html, 'lxml')
len(item)

#%%
soup_html=[]
num_item=len(item)

for i in range(0, num_item):
    res = rq.get(item[i])
    soup = BeautifulSoup(res.content, 'lxml')
    soup_item= soup.find_all("li", class_="_itemSection")
    soup_html.append(soup_item)

num=len(soup_find)
num_item
#%%


title = []
price_sales = []
review_num = []
company = []

for k in range(0, num_item):
    res = rq.get(item[k])
    soup = BeautifulSoup(res.content, 'lxml')
    soup_item = soup.find_all("li", class_="_itemSection")
    for i in range(0, num):
        # 상품명
        soup_title = soup_item[i].find("div",class_="info")
        if soup_title is not None:
            title_txt = soup_title.a.text
            print(title_txt)
            title.append(title_txt)
        else:
            title.append("")
        
        # 상품가격(할인적용금액)
        soup_price = soup_item[i].find("span", class_="num")
        if soup_price is not None:
            price_txt = soup_price.text
            price_sales.append(price_txt)
        else:
            price_sales.append("")
        print(price_sales[i])
        
        # 리뷰
        soup_review = soup_item[i].find("a", class_="graph")
        if soup_review is not None:
            review_num_txt = soup_review.em.text
            review_num.append(review_num_txt)
        else:
            review_num.append("")
        print(review_num[i])
        
        # 회사
        soup_multi = soup_item[i].find("a", class_="btn_compare")
        
        if soup_multi is not None:
            soup_company1 = soup_item[i].find("span", class_="mall_name")
            soup_company_txt = soup_company1.text
            company.append(soup_company_txt)
        else : 
            soup_company2 = soup_item[i].find("P", class_="mall_text")
            soup_company3 = soup_item[i].find("p", class_="mall_txt")
            if soup_company2 is not None:
                soup_company_txt = soup_company2.a.text
                company.append(soup_company_txt)
            elif soup_company3 is not None:
                soup_company_txt = soup_company3.a.text
                if soup_company_txt:
                    company.append(soup_company_txt)
                else :
                    soup_company_txt = soup_company3.a.img['alt']
                    company.append(soup_company_txt)
            else :
                company.append("")
        print(company[i])
#%%
import pandas as pd

print(title, len(title))
print(price_sales, len(price_sales))
print(review_num, len(review_num))
print(company, len(company))

title1 = pd.Series(title)
price_sales1 = pd.Series(price_sales)
review_num1 = pd.Series(review_num)
company_name = pd.Series(company) 

dat = pd.DataFrame({ "title" : title , 
                   "price_sales" : price_sales, 
                   "review_num" : review_num,
                   "company_name" : company_name }, columns=['title','price_sales','review_num', "company_name"] )
dat.info()        
#%% 데이터 베이스 연결
import mysql.connector
mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="qwer1234"
)

print(mydb)

mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="qwer1234",
        database="mydatabase"
    
)

print(mydb)

mycursor = mydb.cursor()

#%%데이터 베이스 설계
mycursor.execute("CREATE TABLE naver (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(64), price_sales VARCHAR(64), review_num VARCHAR(64), company_name VARCHAR(255))")

#%%데이터 베이스에 데이터 넣기
mycursor = mydb.cursor()
dat_list=dat.values.tolist()
for i in range(0,88):
    sql = "INSERT INTO auction ( title , price_sales , review_num , company_name ) VALUES (%s,%s,%s,%s)"
    val = (dat_list[i])
    mycursor.execute(sql, val)










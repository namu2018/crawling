# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:26:51 2018

@author: ktm
"""

import requests as rq

#%%
import requests as rq
url = "https://pjt3591oo.github.io"
res = rq.get(url)
print(res)


#%%
import requests as rq


def url_check(url):
    res = rq.get(url)

    print(res)

    sc = res.status_code

    if sc == 200:
        print("%s 요청성공"%(url))
    elif sc == 404:
        print("%s 찾을 수 없음" %(url))
    else:
        print("%s 알수 없는 에러 : %s"%(url, sc))


url_check("https://pjt3591oo.github.io/")
url_check("https://pjt3591oo.github.io//a")


#%% 03. URL정보를 가져온 후,  headers정보를 가져온다.

import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)
print(res.headers)

headers = res.headers
print(headers['Set-Cookie'])


#%% 04. 전체 헤더 정보를 가져오고 싶다. 
import requests as rq

url = "http://blog.naver.com/pjt3591oo"
res = rq.get(url)
print(res)
print(res.headers)
headers = res.headers

for keys in headers:
    print(headers[keys])


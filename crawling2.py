# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:54:35 2018

@author: ktm
"""
#%%

from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head>
 <body> 
<p><span>test1</span><span>test2</span></p> 
<div><p>THis is MY github </p>
 <a href="https://github.com/namu2018/crawling">crawing</a> </div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')

#tag_p_child = soup.p.children

#for child in tag_p_child:
#    print(child)

tag_div_child= soup.div.children
for child1 in tag_div_child:
    print(child1)
    
a_div=soup.div.text
print(a_div)


from bs4 import BeautifulSoup

html = """<html> 
<head><title>test site</title></head>
<body> 
<p>
  <span>test1</span>
  <span>test2</span>
</p> 
<div>
  <p>THis is MY github </p>
  <a href="https://github.com/namu2018/crawling">crawing</a> 
</div>
<div>
<p class="c1">p부분1 </p>
<p class="c2">p부분2 </p>
<p id='p2'>p부분2</p>
<p>p부분3</p>
</body>
</html>"""

soup = BeautifulSoup(html, 'lxml')
tag_span=soup.span
tag_span.next_sibling
tag_span.previous_sibling

p2= soup.find('p',id='p2')
p2.previous_sibling.previous_sibling
p2.next_sibling.next_sibling.next_sibling

soup_p_all=soup.find_all('p')
soup_p_all

for items in soup_p_all:
   # print(items)
    print(items.text)
#%%find_all(), find()
from bs4 import BeautifulSoup
html = """<html> 
<head><title>test site</title></head>
<body> 
<p>
  <span>test1</span>
  <span>test2</span>
</p> 
<div>
  <p>THis is MY github </p>
  <a href="https://github.com/namu2018/crawling">crawing</a> 
</div>
<div>
<p class="c1">p부분1 </p>
<p class="c1">p부분2 </p>
<p class1="c2">p부분3 </p>
<p class1="c2">p부분4 </p>
<p id='p2'>p부분2</p>
<p>p부분3</p>
</body>
</html>"""

soup = BeautifulSoup(html, 'lxml')
soup_p_one=soup.find('p', id='p2')
print(soup_p_one)

soup_p_class=soup.find_all('p', class_="c1")
soup_p_class

soup_p_class=soup.find_all(class_="c1")
soup_p_class2=soup.find_all(class_="c2")
soup_p_class2

soup_p_id=soup.find_all(id=True)
soup_p_id
soup_p_id=soup.find_all(id=False)
soup_p_id

#%%
#%%find_all(), find()
from bs4 import BeautifulSoup
html = """<html> 
<head><title>test site</title></head>
<body> 
<p>
  <span>test1</span>
  <span>test2</span>
</p> 
<div>
  <p>THis is MY github </p>
  <a href="https://github.com/namu2018/crawling">crawing</a> 
</div>
<div>
<p class="c1">p부분1 </p>
<p class="c1">p부분2 </p>
<p class1="c2">p부분3 </p>
<p class1="c2">p부분4 </p>
<p id='p2'>p부분2</p>
<p>p부분3</p>
</body>
</html>"""

soup = BeautifulSoup(html, 'lxml')
soup_p_id=soup.find_all(id=True)
soup_p_id
soup_p_id[0].parent
soup_p_id.parent

#%%  find_all( ), find() 
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
p_tag = soup.find_all('p', limit=3)
p_tag
p0 = p_tag[0].find_all('span')
p0
for items in p0:
    #print(items)
    print(items.text)

p_tag1=soup.find_all('p')
p4=p_tag1[4].find_all('span')
for items in p4:
    print(items.text)


p_tag=soup.find_all('p', id="a1")[0].find_all('span')
for item in p_tag:
    print(item.text)
    
#%%
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
soup.find_all(['title','p'])
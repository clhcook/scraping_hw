
# coding: utf-8

# In[49]:


from splinter import Browser
from bs4 import BeautifulSoup
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


# In[50]:


#https://splinter.readthedocs.io/en/latest/drivers/chrome.html
#get_ipython().system('which chromedriver')


# In[51]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[7]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#<a href="/news/8371/curiosity-on-the-move-again/" target="_self">Curiosity on the Move Again</a>
title = soup.find('div', class_='content_title')
title_text = title.text
title.text

#title_text = 
#<div class="article_teaser_body">


# In[8]:


#title = soup.find('div', class_='content_title')
title_text = title.text
title.text.strip()


# In[ ]:


par_text = soup.find('div', {'class':'article_teaser_body'})


# In[11]:


par_text = soup.find('div', class_= 'article_teaser_body')
par_text.text


# In[12]:


parag_text = par_text.text
parag_text


# In[13]:


par_text.attrs


# In[55]:


import pymongo

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


# In[14]:


mars_db=client.mars_db
#do shift tab tab to figure out syntax form, doing tab helps to figure out options


# In[15]:


mars_info = mars_db.info


# In[16]:


record = {'title':title_text, 
          'paragraph_text':parag_text}


# In[17]:


mars_info.insert_one(record)


# In[56]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#<a href="/news/8371/curiosity-on-the-move-again/" target="_self">Curiosity on the Move Again</a>
featured_image_url = soup.find({'div':'fancybox-lock'},'img')
featured_image_url


# In[46]:


url = 'https://space-facts.com/mars/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#<a href="/news/8371/curiosity-on-the-move-again/" target="_self">Curiosity on the Move Again</a>


# In[14]:


url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables


# In[36]:


df = tables[0]
df.columns = ['', '']
df.head()


# In[37]:


html_table = df.to_html()
html_table


# In[38]:


html_table.replace('\n', '')


# In[39]:


df.to_html('table.html')


# In[40]:


get_ipython().system('open table.html')


# In[28]:


import time
import math


# In[24]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_hemisphere=[]

try:
    for title_url in titles_and_urls:
        browser.click_link_by_partial_text('next')
except ElementDoesNotExist:
    print("Scraping Complete")


# In[52]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[53]:


results = soup.find_all('a', class_="itemLink product-item")
results


# In[73]:


results[0].find('img')['alt']


# In[72]:


title_3 = results[0].find('h3')
title_3


# In[93]:


output = []
for result in results:
    try:
    
        image = result.find('img')
        title = image['alt']
        title_1 = ' '.join(title.split()[:-1])
        pic = 'https://astrogeology.usgs.gov' + image['src']
        output.append({"title":title_1,
                      "url":pic})
    except:
        pass
print(output)


# In[75]:


' '.join("Cerberus Hemisphere Enhanced thumbnail".split()[:-1])


# In[95]:


outputs = []
for result in results:
    try:
    
        image = result.find('img')
        title = results.find_by_tag('h3')
        #title_1 = ' '.join(title.split()[:-1])
        pic = 'https://astrogeology.usgs.gov' + image['src']
        output.append({"title":title,
                      "url":pic})
    except:
        pass
print(outputs)


# In[92]:


#results[3].find('h3')


# In[34]:


results


# In[ ]:


#set is object type w/o duplicates
# kind like a dictionary without keys
# if you need to search for membership (is "_" in "[__]"), much faster than lists


# In[45]:


urls = ['https://astrogeology.usgs.gov' + result['href'] for result in results][::2]
urls


# In[ ]:


#for url in urls
  #  goto = 'https://astrogeology.usgs.gov/' + url


# In[59]:





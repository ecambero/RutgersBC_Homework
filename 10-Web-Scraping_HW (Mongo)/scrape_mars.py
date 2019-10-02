#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from splinter import Browser
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
# print(browser)


# In[3]:


url = "https://mars.nasa.gov/news/"
response = requests.get(url)
browser.visit(url)
response


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


print(soup.prettify())


# # NASA Mars News

# In[6]:


slide_elem = soup.find_all("div", class_="list_text")
news_title = []
news_p = []
news_dt = []

for elem in slide_elem:
    title = elem.find('div', class_='content_title')
    p = elem.find('div', class_='article_teaser_body')
    date = elem.find('div', class_='list_date')
    
    news_title.append(news_title)
    news_p.append(news_p)
    news_dt.append(news_dt)
    
    print('-------------')
    print(title.text)
    print(p.text)
    print(date.text)
       


# In[7]:


print(title.text)
print(p.text)
print(date.text)    


# # JPL Mars Space Images - Featured Image

# In[8]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
response2 = requests.get(url)
browser.visit(url2)
response2


# In[9]:


button = browser.find_by_xpath("//a[@class='button fancybox']")
featured_image_url = "https://www.jpl.nasa.gov" + button["data-fancybox-href"]
featured_image_url


# # Mars Weather

# In[10]:


url3 = 'https://twitter.com/marswxreport?lang=en'
response3 = requests.get(url3)
browser.visit(url3)
response3
soup = BeautifulSoup(response3.text, 'lxml')


# In[11]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[12]:


mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})


# In[13]:


print(mars_weather_tweet.prettify())


# In[14]:


mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# # Mars Facts

# In[15]:


# Html to DataFrame conversion
Mars_info_df = pd.read_html('https://space-facts.com/mars/')[1]
Mars_info_df


# In[16]:


# Inspect data and set columns 
Mars_info_df.columns=['Description','Mar_Facts']
Mars_info_df


# In[17]:


# Convert back to HTML
Mars_info_df.to_html()


# # Mars Hemispheres

# In[18]:


url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
response5 = requests.get(url5)
browser.visit(url5)
soup = BeautifulSoup(response5.text, 'lxml')


# In[19]:


results = soup.find_all('div', class_='item')
hemispheres = []

for result in results:
    hemisphere = result.find('h3')
    hemispheres.append(hemisphere.text)

hemispheres


# In[20]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()


# In[21]:


hemisphere_image_urls


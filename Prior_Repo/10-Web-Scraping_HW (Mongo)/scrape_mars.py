from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pymongo

def scrape():
    #mars_news()
    mars_feature_img()
    


def mars_news():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://mars.nasa.gov/news/'
    driver.get(url)

    html =  driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find('div', class_='list_text')

    title = articles.find('div', class_="content_title")
    desc = articles.find('div', class_="article_teaser_body")
    date = articles.find('div', class_="list_date")
    a_title=title.text
    a_desc=desc.text
    a_date=date.text

    article = {}

    article["title"] = a_title
    article["desc"] = a_desc
    article["date"] = a_date

    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_scrape
    db.marsnews.insert(article)
    print("Article Data Uploaded!")


def mars_feature_img():

    #options = Options()
    #options.add_argument('test-type')
    #browser = Browser('chrome', options=options)
    browser = Browser('chrome', executable_path='./chromedriver.exe', headless=True)
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    button = browser.find_by_xpath("//a[@class='button fancybox']")
    featured_image_url = "https://www.jpl.nasa.gov" + button["data-fancybox-href"]
    mars_img = {}
    mars_img["feature_img"] = featured_image_url
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_scrape
    db.marsimg.insert(mars_img)
    print("Feature Image Data Uploaded!")
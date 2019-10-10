{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from splinter import Browser\n",
    "import urllib.request\n",
    "import time\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "# print(browser)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://mars.nasa.gov/news/\"\n",
    "response = requests.get(url)\n",
    "browser.visit(url)\n",
    "response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "slide_elem = soup.find_all(\"div\", class_=\"list_text\")\n",
    "news_title = []\n",
    "news_p = []\n",
    "news_dt = []\n",
    "\n",
    "for elem in slide_elem:\n",
    "    title = elem.find('div', class_='content_title')\n",
    "    p = elem.find('div', class_='article_teaser_body')\n",
    "    date = elem.find('div', class_='list_date')\n",
    "    \n",
    "    news_title.append(news_title)\n",
    "    news_p.append(news_p)\n",
    "    news_dt.append(news_dt)\n",
    "    \n",
    "    print('-------------')\n",
    "    print(title.text)\n",
    "    print(p.text)\n",
    "    print(date.text)\n",
    "       \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "print(title.text)\n",
    "print(p.text)\n",
    "print(date.text)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "response2 = requests.get(url)\n",
    "browser.visit(url2)\n",
    "response2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "button = browser.find_by_xpath(\"//a[@class='button fancybox']\")\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\" + button[\"data-fancybox-href\"]\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "response3 = requests.get(url3)\n",
    "browser.visit(url3)\n",
    "response3\n",
    "soup = BeautifulSoup(response3.text, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "weather_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_weather_tweet = weather_soup.find('div', attrs={\"class\": \"tweet\", \"data-name\": \"Mars Weather\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(mars_weather_tweet.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()\n",
    "mars_weather"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Html to DataFrame conversion\n",
    "Mars_info_df = pd.read_html('https://space-facts.com/mars/')[1]\n",
    "Mars_info_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Inspect data and set columns \n",
    "Mars_info_df.columns=['Description','Mar_Facts']\n",
    "Mars_info_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert back to HTML\n",
    "Mars_info_df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "response5 = requests.get(url5)\n",
    "browser.visit(url5)\n",
    "soup = BeautifulSoup(response5.text, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find_all('div', class_='item')\n",
    "hemispheres = []\n",
    "\n",
    "for result in results:\n",
    "    hemisphere = result.find('h3')\n",
    "    hemispheres.append(hemisphere.text)\n",
    "\n",
    "hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []\n",
    "\n",
    "# Get a List of All the Hemispheres\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "for item in range(len(links)):\n",
    "    hemisphere = {}\n",
    "    \n",
    "    # Find Element on Each Loop to Avoid a Stale Element Exception\n",
    "    browser.find_by_css(\"a.product-item h3\")[item].click()\n",
    "    \n",
    "    # Find Sample Image Anchor Tag & Extract <href>\n",
    "    sample_element = browser.find_link_by_text(\"Sample\").first\n",
    "    hemisphere[\"img_url\"] = sample_element[\"href\"]\n",
    "    \n",
    "    # Get Hemisphere Title\n",
    "    hemisphere[\"title\"] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    # Append Hemisphere Object to List\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    # Navigate Backwards\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

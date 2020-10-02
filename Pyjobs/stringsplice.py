from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
import emailtesting as e
import sys


browser = webdriver.Chrome()


def scrapePosting(locations):

    response = requests.get(locations)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    # print(soup.find_all('a'))
    # jobs = soup.select(".result-row")
    for link in soup.find_all('a'):
        print(link.get('href'))

    # gets all text
  #


scrapePosting("https://www.craigslist.org/about/sites")


time.sleep(4)
browser.quit()

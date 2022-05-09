import bs4
import requests
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# CHROME_DRIVER_PATH = 'C:\\Users\\dinar\\Documents\\python_dep\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

search_url = 'https://www.google.com/search?q=car+parts&source=lnms&tbm=isch'
driver.get(search_url)
time.sleep(5)

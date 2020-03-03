from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import bs4 as bs

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com/')
driver.save_screenshot('sc.png')

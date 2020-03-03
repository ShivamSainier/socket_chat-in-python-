from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import requests
import bs4 as bs

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com/')
button=driver.find_element_by_xpath("//*[@id='logo-icon-container']")
action=ActionChains(driver)
action.context_click(button).perform() #mouse right click on youtube logo


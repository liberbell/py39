from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep

driver = webdriver.Safari()
URL = "https://www.yahoo.co.jp"
URL2 = "https://www.google.com"

driver.get(URL2)
search_bar = driver.find_element_by_name("q")
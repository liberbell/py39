from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep

driver = webdriver.Safari()
URL = "https://www.yahoo.co.jp"

driver.get(URL)
from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep

driver = webdriver.Safari()
URL = "https://www.yahoo.co.jp"
URL2 = "https://www.google.com"

driver.get(URL2)
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("Python")
search_bar.submit()

for elem_h3 in driver.find_elements_by_xpath("//a/h3"):
    print(elem_h3.text)
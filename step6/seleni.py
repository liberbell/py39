from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wdriver = webdriver.Safari()
URL = "https://www.yahoo.co.jp"
URL2 = "https://www.google.com"

wdriver.get(URL2)
search_bar = wdriver.find_element(By.NAME, "q")
search_bar.send_keys("Python")
search_bar.submit()

print(wdriver.find_elements(By.XPATH, "//a/h3"))
# for elem_h3 in wdriver.find_elements(By.XPATH, "//a/h3"):
#     print(elem_h3.text)
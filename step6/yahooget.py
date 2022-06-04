from bs4 import BeautifulSoup
import requests
import time
import re

# #tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span
URL = "https://www.yahoo.co.jp/"

yahoo_response = requests.get(URL)
soup = BeautifulSoup(yahoo_response.text, "html.parser")

elms = soup.find_all("a")
# print(elms)

elems = soup.find_all(href=re.compile("yahoo.co.jp/pickup"))
print(elems[0].span.string)
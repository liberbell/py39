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
# print(elems[0].span.string)
# print(elems[0].attrs["href"])

# #uamods-pickup > div.sc-bYzVrU.hUZPkx > div > p > a
for elem in elems:
    print(elem.span.string)
    print(elem.attrs["href"], end="\n\n")
    pickup_link = elem.attrs["href"]
    pickup_response = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_response.text, "html.parser")
    print(pickup_soup.prettify())
import re
from bs4 import BeautifulSoup
import requests

URL = "https://www.yomiuri.co.jp/"

response1 = requests.get(URL)
print(response1.status_code)
# print(response1.text)

soup = BeautifulSoup(response1.text, "html.parser")

# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(1) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(2) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(3) > div > h3 > a

elems = soup.select("div.headline > article:nth-child(1) > div > h3 > a")
# print(elems[0])
# print(elems[0].contents[0])
# print(elems[0].attrs["href"])

elems = soup.select("div.headline")
# print(elems[0])
# print(elems[0].prettify())

print(type(elems[0]))
print(elems[0].h3.a)
print(elems[0].h3.a.string)
print(elems[0].h3.a["href"])
print(elems[0].article.next_sibling.next_sibling.h3.a.string)
print(elems[0].article.next_sibling.next_sibling.h3.a["href"])
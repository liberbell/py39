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
print(elems[0])
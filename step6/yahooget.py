from bs4 import BeautifulSoup
import requests
import time

# #tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span
URL = "https://www.yahoo.co.jp/"

yahoo_response = requests.get(URL)
soup = BeautifulSoup(yahoo_response, "html.parser")

elms = soup.find_all("a")
print(elms)
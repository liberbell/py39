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
# for elem in elems:
#     print(elem.span.string)
#     print(elem.attrs["href"], end="\n\n")
#     pickup_link = elem.attrs["href"]
#     pickup_response = requests.get(pickup_link)
#     pickup_soup = BeautifulSoup(pickup_response.text, "html.parser")
#     # print(pickup_soup.prettify())
#     elems = soup.select("div.sc-bYzVrU.hUZPkx > div > p > a")
#     print(elems.text)

pickup_links = [elem.attrs["href"] for elem in elems]
# print(pickup_links)
for pickup_link in pickup_links:
    pickup_response = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_response.text, "html.parser")
    pickup_elem = pickup_soup.find("p", class_="sc-kvjbNB igDfka")
    # <p class="sc-kvjbNB igDfka"><a href="https://news.yahoo.co.jp/articles/0a62dabf598b8790042dcfa5b96c1d42cff5bb40" data-ylk="rsec:tpc_main;slk:headline;pos:2;" data-ual-gotocontent="true" class="sc-kREsUy fOkZWA" data-rapid_p="40">記事全文を読む</a></p>
    news_link = pickup_elem.a.attrs["href"]
    # print(news_link)

    news_response = requests.get(news_link)
    news_soup = BeautifulSoup(news_response.text, "html.parser")
    print("Title : ", news_soup.title.text)
    # print(news_link)
    
    detail_text = news_soup.find(class_=re.compile("Directlink"))
    print(detail_text.text if hasattr(detail_text, "text") else '', end="\n\n\n")
    time.sleep(1)
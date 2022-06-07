from bs4 import BeautifulSoup
import requests

URL = "https://kanagawa-park.jp/bbq/yoyaku/hatano/calender.html&kind=1"

bbqdata = requests.get(URL)
print(bbqdata.status_code)

bbqdata_soup = BeautifulSoup(bbqdata.text, "html.parser")
# print(bbqdata_soup.prettify())
elem1 = bbqdata_soup.find_all("td")
elem2 = bbqdata_soup.select("#main > section > div > table > tbody > tr > td > a")
print(elem2)

#main > section > div.sn > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(6) > a
#main > section > div.sn > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(6) > a
   #main > ul > li:nth-child(1) > a
# div#main > ul.items > li
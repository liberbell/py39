from bs4 import BeautifulSoup
import requests

URL = "https://kanagawa-park.jp/bbq/yoyaku/hatano/calender.html&kind=1"

bbqdata = requests.get(URL)
print(bbqdata.status_code)

bbqdata_soup = BeautifulSoup(bbqdata.text, "html.parser")
elem1 = bbqdata_soup.find_all("td")
elem2 = bbqdata_soup.select("tbody > tr:nth-of-type(1) > td:nth-of-type(6) > a")
print(elem2)

#main > section > div.sn > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(6) > a
   #main > ul > li:nth-child(1) > a
# div#main > ul.items > li
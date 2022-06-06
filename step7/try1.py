from bs4 import BeautifulSoup
import requests

URL = "https://kanagawa-park.jp/bbq/yoyaku/hatano/calender.html&kind=1"

bbqdata = requests.get(URL)
print(bbqdata.status_code)

bbqdata_soup = BeautifulSoup(bbqdata, "html.parser")
elem = bbqdata_soup.find_all("td")
print(elem)

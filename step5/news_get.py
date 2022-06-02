import re
from bs4 import BeautifulSoup
import requests

URL = "https://www.yomiuri.co.jp/"

response1 = requests.get(URL)
print(response1.status_code)
print(response1.get)
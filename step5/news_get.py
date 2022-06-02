import re
from bs4 import BeautifulSoup
import requests

URL = "https://www.yomiuri.co.jp/"

response = requests.get(URL)
print(response.status_code)
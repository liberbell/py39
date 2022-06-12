from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
import os
import time
import smtplib 

def beep(freq, dur=100):

    # @param freq
    # @param dur（ms）
    os.system('play -n synth %s sin %s' % (dur/1000, freq))

URL = "https://kanagawa-park.jp/bbq/yoyaku/hatano/calender.html&kind=1"

i = 0
search_section = "1部"
search_day = 19
search_keyword = "d=" + str(search_day)
match_count = 0

while True:
    bbqdata = requests.get(URL, headers={'Cache-Control': 'no-cache'})
    bbqdata_soup = BeautifulSoup(bbqdata.text, "html.parser")
    elem2 = bbqdata_soup.select("td > a")
    for i in range(len(elem2)):
        url_parse = urlparse(str(elem2[i]))
        # print(url_parse.path)
        # print(type(url_parse.path))
        if search_section in url_parse.path:
            # print(url_parse.path)
            url_path = url_parse.path
            if search_keyword in url_path:
                print(url_path)
                match_count = match_count + 1
        # print(elem2[i])
        # print(grep_target)
        i = i + 1
        time.sleep(30)
        print(match_count)
        if match_count == 0:
            print("No vacancy!")
        else:                
            beep(2000, 100)
    
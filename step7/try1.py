from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
import os
import time
import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEText import MIMEText

def beep(freq, dur=100):

    # @param freq
    # @param dur（ms）
    os.system('play -n synth %s sin %s' % (dur/1000, freq))


port_number =1234
msg = MIMEMultipart()
msg['From'] = 'sender@protonmail.com'
msg['To'] = 'receiver@protonmail.com'
msg['Subject'] = 'My Test Mail '
message = 'This is the body of the mail'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('localhost',port_number)
mailserver.login("sender@protonmail.com", "mypassword")
mailserver.sendmail('sender@protonmail.com','receiver@protonmail.com',msg.as_string())
mailserver.quit()

URL = "https://kanagawa-park.jp/bbq/yoyaku/hatano/calender.html&kind=1"

bbqdata = requests.get(URL)
# print(bbqdata.status_code)

bbqdata_soup = BeautifulSoup(bbqdata.text, "html.parser")
# print(bbqdata_soup.prettify())
elem1 = bbqdata_soup.find_all("td")
elem2 = bbqdata_soup.select("td > a")
elem3 = bbqdata_soup.find_all("a")
elem4 = bbqdata_soup.select('img[alt="1部"]')
# print(elem4)
# print(elem2)
# print(elem2[0])
# print(elem3)
# for elem in elem2:
    # print(elem.a.string)
    # print(elem.a["href"])
    # print(elem[0].a)


#main > section > div.sn > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(6) > a
#main > section > div.sn > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(6) > a
   #main > ul > li:nth-child(1) > a
# div#main > ul.items > li
i = 0
search_section = "1部"
search_day = 19
search_keyword = "d=" + str(search_day)
match_count = 0
# print(search_keyword)
while True:
    for i in range(len(elem2)):
        url_parse = urlparse(str(elem2[i]))
        # print(url_parse.path)
        # print(type(url_parse.path))
        if search_section in url_parse.path:
            # print(url_parse.path)
            if search_keyword in url_parse.path:
                print(url_parse.path)
                match_count = match_count + 1
        # print(elem2[i])
        # print(grep_target)
        i = i + 1
        time.sleep(30)
        print(match_count)
        if match_count != 0:
            beep(2000, 100)
            port_number =1234
            msg = MIMEMultipart()
msg['From'] = 'sender@protonmail.com'
msg['To'] = 'receiver@protonmail.com'
msg['Subject'] = 'My Test Mail '
message = 'This is the body of the mail'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('localhost',port_number)
mailserver.login("sender@protonmail.com", "mypassword")
mailserver.sendmail('sender@protonmail.com','receiver@protonmail.com',msg.as_string())
mailserver.quit()

# beep(2000, 100)
# for i in range(len(elem4)):

#     print(elem4[i])
#     i = i + 1

# print(elem2)
# section_list = [s for s in elem2.img if 'alt="1部"' in s]
# print(section_list)
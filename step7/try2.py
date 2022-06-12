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
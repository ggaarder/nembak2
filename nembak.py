#!/usr/bin/env python3
import datetime
import time
import json
import re
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import myid

def bs(x):
    return BeautifulSoup(x, 'html.parser')

wd = webdriver.Chrome()

HOME="http://music.163.com/#/user/home?id={}".format(ID)

dat = {}
dat['@home'] = HOME
dat['timestamp'] = time.time()
dat['strftime'] = datetime.datetime.strftime(datetime.datetime.now(), "%c")

wd.get(HOME)
soup = bs(wd.page_source)
dat['user'] = re.sub(r'^(.+) - 用户 - 网易云音乐$', r'\1', soup.title.text)
print('User: %s' % dat['user'])

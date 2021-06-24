#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:21:18 2021

@author: denish
"""

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/denish/Desktop/Temp/chromedriver")

Time_Delay_m1 = []
Time_Delay_sec = []
Time_Delay_m2 = []
Bus_Number = []

driver.get("https://bus.dabase.com/?id=44221")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'buses'}):
    
Time_Delay_t1 =a.find('time', attrs={'class':''})
Time_Delay_t2 =a.find('time', attrs={'class':''})
Time_Delay_t3 =a.find('time', attrs={'class':''})
Time_Delay_t1.append(Time_Delay_t1.text)
Time_Delay_t2.append(Time_Delay_t2.text)
Time_Delay_t3.append(Time_Delay_t3.text)

Bus_Number= a.find('div', attrs={'class':'')
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)

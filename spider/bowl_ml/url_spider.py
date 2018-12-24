import requests
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs
import csv
base = 'http://fine.gq/'
html = SpiderHtml(base).getHtml()
soup = bs(html, 'html.parser')
items = soup.find_all(class_='item item-0')
with open("item.csv", "a+", encoding = "utf-8") as f:
    writer = csv.writer(f)
    for i in items:
        a_s = i.find_all('a')
        for j in a_s:
            list=[]
            list.append(j['href'])
            list.append(j.text)
            writer.writerow(list)

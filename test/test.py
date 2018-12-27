import csv

from utils.SpiderUtil import SpiderHtml

url='http://www.mmjpg.com/more/'
base='http://www.mmjpg.com/'
soup=SpiderHtml(url=url).getBeautifulSoup(base)
tags=soup.find(id='morelist').find_all('li')
print(len(tags))
with open("mmjpg_tags.csv", "a+", encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in tags:
        print(i)
        list = []
        list.append(i.a['href'])#link
        list.append(i.a.img['src'])#img
        list.append(i.a.img['data-img'])#img
        list.append(i.find('i').text)#num
        list.append(i.a.text)#name
        writer.writerow(list)


import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import sys

sys.setrecursionlimit(10000)
url="https://guitar-saloon.ru/shop/ukulele/"

base_url = "https://guitar-saloon.ru"
r = requests.get(url)
soup = bs(r.content, "lxml")
products = soup.find_all("div", class_="goods")

urls = []
for product in products:
    link = product.find('a', itemprop='url').get("href")
    urls.append(base_url + link)
print(urls[99])
args = []
for a in urls:
    r = requests.get(a)
    soup = bs(r.content, "lxml")
    name = soup.find("h1", itemprop="name")
    if name:
        name=name.get_text(strip=True)
    price = soup.select_one("span.strong")
    if price:
        price=price.get('content')
    description = soup.find('div', id='goods_desc')
    if description:
        description=description.findNext('div', itemprop='description').text
    args.append((name, price, description))
            

conn = sqlite3.connect("mydata.db")

cursor = conn.cursor()

cursor.executemany("INSERT INTO ukuleles VALUES (?,?,?)", args)
conn.commit()
conn.close()

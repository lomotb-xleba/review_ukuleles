import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import sys
aa='3000 5000'
url="https://guitar-saloon.ru/shop/ukulele/"
def parser(url:str,aa):
    sys.setrecursionlimit(10000)
    alf=[" ",",","_","-","=",";",":"]
    aaa=list(aa)
    n=0
    m=0
    i=0
    while aaa[i] not in alf:
        n=n*10+int(aaa[i])
        i+=1
    i+=1 
    while i<len(aaa):
        m=m*10+int(aaa[i])
        i+=1
    base_url = "https://guitar-saloon.ru"
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    products = soup.find_all("div", class_="goods")

    urls = []
    for product in products:
        link = product.find('a', itemprop='url').get("href")
        urls.append(base_url + link)
    
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
            if n<=float(price)<=m:
        # description = soup.find('div', id='goods_desc')
        # if description:
        #     description=description.findNext('div', itemprop='description').text
                args.append((name, price, a))
    return args       

if __name__ == '__main__':
    print(parser(url="https://guitar-saloon.ru/shop/ukulele/",aa='3000 5000'))

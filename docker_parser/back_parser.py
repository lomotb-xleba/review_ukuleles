import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import sys

aa='3000 5000'
url="https://guitar-saloon.ru/shop/ukulele/"
def parser(url:str,aa):
    sys.setrecursionlimit(10000)
    numb=["0","1","2","3","4","5","6","7","8","9"]
    aaa=list(aa)
    n=0
    m=0
    i=0
    if aaa[i] in numb:
        while aaa[i] in numb:
            n=n*10+int(aaa[i])
            i+=1
        while aaa[i] not in numb:
            i+=1
            if i==len(aaa):
                args="ERROR"
                return args
        while i<len(aaa):
            if aaa[i] in numb:
                m=m*10+int(aaa[i])
                i+=1
            else:
                args="ERROR"
                return args
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
                    args.append((name, price, a))
        if len(args)==0:
            args=0
    else:
        args="ERROR"
    return args       

if __name__ == '__main__':
    print(parser(url="https://guitar-saloon.ru/shop/ukulele/",aa='3000 5000'))

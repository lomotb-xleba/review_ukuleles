import requests
from bs4 import BeautifulSoup
import sqlite3

def parser(url:str):
    base_url="https://guitar-saloon.ru"
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="goods")
    
    urls=[]
    for product in products:
        link = product.find('a', itemprop='url').get("href")
        urls.append(base_url+link)
    
    args = []
    for url in urls:
        response = requests.get(url=url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.find("h1", itemprop="name").text
        price = soup.select_one("span.strong").get('content')
        description =  soup.find('div', id='goods_desc').findNext('div', itemprop='description').text
        args.append((name, price, description))
       
    conn = sqlite3.connect("mydata.db")

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO ukulele VALUES (?,?,?)", args)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser(url="https://guitar-saloon.ru/shop/ukulele/")

   

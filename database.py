import sqlite3

sql = "CREATE TABLE ukuleles (name TEXT, price TEXT, description TEXT)"
sql = "SELECT * FROM ukuleles"
conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

cursor.execute(sql)

res =cursor.fetchall()

n, m=map(int, input("введите диапозон цены через пробел (пример: 3000 5000): ").split( ))
for r in res:
    if r[1]:    
        if n<=float(r[1])<=m:
            print("name   :",r[0])
            print("price  :",r[1])
            print("description   :",r[2])

conn.close()
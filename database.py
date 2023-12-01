import sqlite3

conn= sqlite3.connect("mydata.db")

sql = "CREATE TABLE ukulele (name TEXT, price TEXT, description TEXT)"
sql = "SELECT * FROM ukulele"
cursor = conn.cursor()

cursor.execute(sql)

res = cursor.fetchall()

for r in res:
    print("Name",r[0])

conn.close()


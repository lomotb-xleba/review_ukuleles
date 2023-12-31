import sqlite3

# sql = "CREATE TABLE ukuleles (name TEXT, price TEXT, description TEXT)"
# sql = "SELECT * FROM ukuleles"
# conn = sqlite3.connect("mydata.db")
# cursor = conn.cursor()

# cursor.execute(sql)

# res =cursor.fetchall()



# conn.close()
class DataAccessObject:
    __instance = None

    def new(cls):
        if cls.__instance is None:
            cls.__instance = super().new__(cls)
        return cls.__instance

    def init(self):
        self.connect = sqlite3.connect('mydata.db')
        self.tab = self.connect.cursor()
        self.tab.execute("CREATE TABLE IF NOT EXISTS ukuleles (name TEXT, price TEXT, url TEXT)")
        self.connect.commit()
    def create(self, args):
        i=0
        while i<len(args):
            self.tab.execute("INSERT INTO ukuleles VALUES (?,?,?)", args[i])
            self.connect.commit()
            i+=1
    def show_base(self):
        self.tab.execute('SELECT * FROM ukuleles')
        result = self.tab.fetchall()
        return result
    def close_database(self):
        self.connect.close()
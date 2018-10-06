import sqlite3
# defining a class
class Database:
    # constructor is defined in python using __init__(self).
    # self is needed in all variables defined in init and used in other methods
    # as it signals that you are calling it on to the instance of the object
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title text,author text,year integer,isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL ,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        # self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        row=self.cur.fetchall()
        # conn.commit()
        # self.conn.close()
        return row

    # add default "" so that user can type in only one parameter.
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        # conn.commit()
        # conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        # conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
        # conn.close()
    # when you close the program, you are essentially destroying the instance of the Database object created.
    # so when you close the program/delete the instance of object, you can also close the database connection
    def __del__(self):
        self.conn.close()

# connect()
# insert("the Sun","John Smith",1800,282000853)
# delete(2)
# update(3,"The Moon","Thot bois",1907,59930449)
# print(view())
# print(search(author="John Smith"))
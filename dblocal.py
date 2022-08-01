import sqlite3

def creteTable():
    try:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tiendas(
            nameshop text NOT NULL
        )''')
        return True
    except Exception as e:
        return e



def readTable():
    try:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''SELECT rowid, nameshop FROM tiendas''')
        return cur.fetchall()
    except Exception as e:
        return e;

def deleteItem(item):
    try:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''DELETE FROM tiendas WHERE rowid = ?''', (item, ))
        con.commit()        
    except Exception as e:
        return e


def insertTable(nameshop):
    try:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute("""
        INSERT INTO tiendas(nameshop)
        VALUES (?)
        """, (nameshop,))
        con.commit()
        con.close()
        return True
    except Exception as e:
        return e



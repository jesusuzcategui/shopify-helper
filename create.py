from db import conex
import mysql.connector
import menu

def create():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopify_list"
        )
        name = input('Write name of shop shopify: ')
        query = ("INSERT INTO shops(nameshop) VALUES (%(name)s)")
        data = {
            'name': name
        }
        dbo = mydb.cursor()    
        dbo.execute(query, data)
        mydb.commit()
        dbo.close()
        mydb.close()

        menu.menuRender()
    except mysql.connector.Error as e:
        print("Error ", e.msg)

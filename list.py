from db import conex
import mysql.connector
import menu

def list():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopify_list"
        )
        query = ("SELECT idshops, nameshop FROM shops")
        dbo = mydb.cursor()    
        dbo.execute(query)
        
        print("+-+-+- SHOPS -+-+-+")
        for(idshops, nameshop) in dbo:
            print(idshops, "- ", nameshop)
        
        dbo.close()
        mydb.close()
    except mysql.connector.Error as e:
        print("Error ", e.msg)
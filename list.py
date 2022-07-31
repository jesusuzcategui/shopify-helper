from db import conex
import mysql.connector
import os
import menu

def list():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopify_list"
        )
        query = ("SELECT idshops, nameshop FROM shops order by idshops DESC")
        dbo = mydb.cursor(dictionary=True)    
        dbo.execute(query)
        records = dbo.fetchall()
        
        print("+-+-+- SHOPS -+-+-+")
        for row in records:
            print(row["idshops"], "- ", row["nameshop"])
        
        
        numberSelected = int(input("Enter id shop or 0 to back menu: "))
        print(numberSelected)
        for row_new in records:
            if(int(row_new["idshops"]) == numberSelected):
                commandTo = "shopify login --store " + row["nameshop"]
                print("Haz seleccionado: ", row_new["nameshop"])
                os.system(commandTo);
        else:
            menu.menuRender(3)
        
        dbo.close()
        mydb.close()
    except mysql.connector.Error as e:
        print("Error ", e.msg)
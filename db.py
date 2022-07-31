import mysql.connector

def conex():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shopify_list"
    )
    return mydb;
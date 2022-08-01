import os
import menu
import dblocal

def deleteItem():
    print("DELETE A ITEM: ")
    records = dblocal.readTable()
    print("+-+-+- SHOPS -+-+-+")
    
    for row in records:
        print(row[0], ". ", row[1])
    
    optionNumber = int(input("Put a number to delete"))

    confirm = input("You want delete item? Press Y or N")

    if(confirm == "Y" or confirm == "y"):
        dblocal.deleteItem(optionNumber)
        print("Item deleted")
        menu.menuRender()
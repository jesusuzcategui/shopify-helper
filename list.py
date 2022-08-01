import os
import menu
import dblocal


def list():
    try:
        records = dblocal.readTable()

        print("+-+-+- SHOPS -+-+-+")
        for row in records:
            print(row[0], ". ", row[1])
        
        numberSelected = int(input("Enter id shop or 0 to back menu: "))

        for row_new in records:
            if(int(row_new[0]) == numberSelected):
                commandTo = "shopify login --store " + row[1]
                print("Haz seleccionado: ", row_new[1])
                os.system(commandTo);
        else:
            menu.menuRender(3)
    except Exception as e:
        print("Error ", e)
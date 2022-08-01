from create import create
from list import list
import delete
import utils
import dblocal
import os
def menuRender(numero=None):
    menuItems = ["Lista", "Crear", "Menu", "Cerrar", "Db Local - Crear", "Eliminar", "Theme serve"]
    print("=== MENU ===")
    for (item, i) in enumerate(menuItems, start=1):
        print(i, "- ", item)

    if numero == None:
        Option = int(input("Select a option: "))
    else:
        Option = numero
    
    utils.clear()
    if Option == 1:
        list()
    elif Option == 2:
        create()
    elif Option == 3:
        menuRender()
    elif Option == 5:
        result = dblocal.creteTable()
        print(result);
        print("Press 0 to back to menu");

        accion = int(input("Select a option: "))

        if(accion == 0):
            menuRender()
    elif Option == 6:
        delete.deleteItem()
    elif Option == 7:
        os.system("shopify theme serve")
    else:
        quit()
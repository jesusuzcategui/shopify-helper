from create import create
from list import list
import utils
def menuRender(numero=None):
    menuItems = ["Lista", "Crear", "Menu", "Cerrar"]
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
    else:
        quit()
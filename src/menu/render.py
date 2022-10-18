from tokenize import Number
import os
import termcolor
from cfonts import render as cfont_render
import prompt_toolkit
from rich.table import Table
from rich.console import Console
from ..database.db import Db
from ..git.helper import gitHelper

DbHelper = Db()
git = gitHelper()

def login():
    termcolor.cprint('Login into store development', "yellow")
    id = int( prompt_toolkit.prompt("Put id to login: ") )
    currentData = DbHelper.list(id=id)
    if( len(currentData) == 0 ):
        termcolor.cprint('The ID put does no information', "danger")
        render()
        return False
    
    os.chdir(currentData[0][2])
    print("You now are: ", os.getcwd())
    commandToLogin = "shopify login --store " + currentData[0][1]
    os.system(commandToLogin)


def formDelete(id):
    termcolor.cprint('Delete item', "yellow")
    confirm = prompt_toolkit.prompt("Do you want delete item: ")
    if( confirm in ["n", "N"] ):
        render()
    else:
        delete = DbHelper.delete(id)
        if(True == delete):
            termcolor.cprint('Store update!', "green")
        else:
            termcolor.cprint(delete, "red")

        render()            


def formEdit(id):
    currentData = DbHelper.list(id=id)
    if( len(currentData) == 0 ):
        termcolor.cprint('The ID put does no information', "danger")
        render()
        return False
    
    termcolor.cprint('Edit store data...', "yellow")
    print("\n")
    print("Url: ", currentData[0][1])
    print("Path: ", currentData[0][2])
    shopName = prompt_toolkit.prompt("Put shop name or press enter to keep current: ")
    shopPath = prompt_toolkit.prompt("Put shop path repository or press enter to keep current: ")

    if(shopName == ""):
        shopName = currentData[0][1]
    if(shopPath == ""):
        shopPath = currentData[0][2]
    
    update = DbHelper.update(shopName, shopPath, id)

    if( update == True ):
        termcolor.cprint('Store update!', "green")
    else:
        termcolor.cprint(update, "red")
    
    render()


def executeAction(num: Number):
    if num == 1:
        pass
    elif num == 2:
        termcolor.cprint('Register a shopify account', "yellow")
        shopName = prompt_toolkit.prompt("Put shop name: ")
        shopPath = prompt_toolkit.prompt("Put shop path repository: ")

        result = DbHelper.create(shopName, shopPath)

        if( True == result ):
            termcolor.cprint('Shop name saved', "green")
            render()
        else:
            print(result)
    elif num == 3:
        termcolor.cprint('Creating table on db local', "blue")
        result = DbHelper.inizialite();
        termcolor.cprint('Table create or existing', "green")
        print(result)
    elif num == 4:
        result = DbHelper.list(id=None);
        table = Table(title="Shops registered")
        tableCols = ["ID", "Url", "Path"]
        formatedRows = []

        for col in tableCols:
            table.add_column(col)

        for row in result:
            formatedRows.append([
                str(row[0]),
                row[1],
                row[2]
            ])
        
        for fr in formatedRows:
            table.add_row(*fr, style="bright_green")
        
        console = Console()
        console.print(table)

        print("\n--------------------------------------------------------------------------------")
        termcolor.cprint('Put a option: (e) Edit, (d) Delete, (l) Login, (m) Menu', "blue")

        listAction = prompt_toolkit.prompt("Do you want? ")

        if( listAction in ["e", "E"] ):
            id_edit = int( prompt_toolkit.prompt("Put id to edit: ") )
            formEdit(id_edit)
        if( listAction in ["d", "D"] ):
            id_delete = int( prompt_toolkit.prompt("Put id to delete: ") )
            formDelete(id_delete)
        elif( listAction in ["m", "M"] ):
            render()
        elif( listAction in ["l", "L"] ):
            login()

        render()
    
    elif num == 5:
        os.system("shopify theme serve");

    elif num == 7:
        termcolor.cprint('Good by', "blue")
        quit()
    elif num == 6:
        git.show()
    elif num == 8:
        os.system("cls")
        render()
        

def render():
    items = [
        {"icon": "❤️", "label": "Home"},
        {"icon": "💾", "label": "Register"},
        {"icon": "🗡️", "label": "Init Db"},
        {"icon": "📦", "label": "Records"},
        {"icon": "🚀", "label": "Theme serve"},
        {"icon": "🛖", "label": "Git"},
        {"icon": "🚪", "label": "Salir"},
        {"icon": "🧹", "label": "Limpiar"}
    ]

    output = cfont_render(
        text='Shopify Helper', 
        colors=['green', 'white'], 
        align='left',
        font='simple',
        size=[250, 80],
        line_height=0.2
    )

    print(output)
    termcolor.cprint("Tool created by Jesus Uzcategui\n", "green")

    for (i, item) in enumerate(items, start=1):
        label = str(i) + ") " + item['icon'] + "  " + item['label']
        termcolor.cprint(label, "blue")
    
    print("\n")

    option = prompt_toolkit.prompt("Put a option: ")
    option = int(option)
    executeAction(option)


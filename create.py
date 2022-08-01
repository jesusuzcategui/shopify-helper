import dblocal
import menu

def create():
    try:
        name = str(input('Write name of shop shopify: '))
        
        result = dblocal.insertTable(name);
        #screenR = "Record success" if result else "Has error"
        print("Result: ", result);
        menu.menuRender()
    except Exception as e:
        print("Error ", e.msg)

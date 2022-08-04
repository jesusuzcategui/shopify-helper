from termcolor import cprint
from cfonts import render, say
from prompt_toolkit import prompt
from ..menu.render import render as menuRender

def index():
    """
    Titulo de pantalla
    """
    output = render(
        'Shopify Helper', 
        colors=['green', 'white'], 
        align='left',
        font='simple'
    )
    print(output)

    cprint('Welcome  to application', 'green')

    menuRender()


from controllers.login_controller import Login_controller
from helpers.menu import Menu
import pprint

def iniciar_app():

    try:
        print('''
        =======================
            Sistema Colegio
        =======================
        ''')
        menu_principal = ["Login", "Salir"]
        respuesta = Menu(menu_principal).show()        
        
        if respuesta == 1:
            login = Login_controller()
            login.logeo()
            if login.salir:
                iniciar_app()
        print("\nGracias por utilizar nuestra app\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except ValueError as e:
        print(f'{str(e)}')

iniciar_app()
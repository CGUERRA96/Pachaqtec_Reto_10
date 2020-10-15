from classes.persona import Persona
from controllers.alumnos_controller import Alumnos_controller
from controllers.profesores_controller import Profesores_controller
from controllers.administrador_controller import Administrador_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Login_controller:
    def __init__(self):
        self.persona  = Persona()
        self.alumnos_controller = Alumnos_controller()
        self.profesores_controller = Profesores_controller()
        self.administrador_controller = Administrador_controller()
        self.salir = False
        
    def logeo(self):

        print('''
        =============
            Login
        =============
        ''')
        try:
            validar = self.persona.obtener_personas('id_persona')
            if validar:

                dni = input_data("Ingrese su DNI >> ")
                password = input_data("Ingrese su password >> ")
                login = self.persona.buscar_personas({'dni_persona' : dni, 'password': password })
                #print(print_table(login))
                if login:
                    lista_persona = []
                    for v in login:
                        id_persona  = v[0]
                        id_tipo_rol = v[1]
                        nombres = v[2]
                        dni_persona = v[5]
                        password = v[6]

                        usuario_login = self.persona.obtener_persona({
                            'id_persona': id_persona
                        })

                        lista_persona.append({
                            'id_persona' : usuario_login[0],
                            'id_tipo_rol' : usuario_login[1],
                            'nombres' : usuario_login[2],
                            'edad' : usuario_login[3],
                            'correo' : usuario_login[4],
                            'dni_persona' : usuario_login[5],
                            'password' : usuario_login[6],
                        })
                        print(f'''
                        ==========================================================
                                    Bienvenido : {nombres}
                        ==========================================================
                        ''')

                        if id_tipo_rol  == 1:
                            self.administrador_controller.menu()
                        elif id_tipo_rol  == 2:
                            self.profesores_controller.menu()
                        elif id_tipo_rol  == 3:
                            self.alumnos_controller.menu()
                        else:
                            self.salir = True
                            break
                return lista_persona
            else:
                print('Por favor ingresar el usuario maestro, contactarse con su administrador')
                self.administrador_controller.registro_maestro()
        except Exception as e:
            print(f'{str(e)}')
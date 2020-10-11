from classes.curso import Curso
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Cursos_controller:
    def __init__(self):
        self.curso = Curso()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Cursos
                ===============
                ''')
                menu = ['Listar cursos', 'Buscar curso', "Nuevo curso", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_cursos()
                elif respuesta == 2:
                    self.buscar_curso()
                elif respuesta == 3:
                    self.insertar_curso()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_cursos(self):
        print('''
        ========================
            Lista de Cursos
        ========================
        ''')
        cursos = self.curso.obtener_cursos('curso_id')
        print(print_table(cursos, ['ID', 'Nombre']))
        input("\nPresione una tecla para continuar...")

    def buscar_curso(self):
        print('''
        =====================
            Buscar Curso
        =====================
        ''')
        try:
            id_curso = input_data("Ingrese el ID del curso >> ", "int")
            curso = self.curso.obtener_curso({'curso_id': id_curso})
            print(print_table(curso, ['ID', 'Nombre']))

            if curso:
                if pregunta("¿Deseas dar mantenimiento al curso?"):
                    opciones = ['Editar curso', 'Eliminar curso', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_curso(id_curso)
                    elif respuesta == 2:
                        self.eliminar_curso(id_curso)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_curso(self):
        nombre = input_data("Ingrese el nombre del curso >> ")
        self.curso.guardar_curso({
            'nombre': nombre
        })
        print('''
        ==============================
            Nuevo Curso agregado !
        ==============================
        ''')
        self.listar_cursos()

    def editar_curso(self, id_curso):
        nombre = input_data("Ingrese el nuevo nombre del curso >> ")
        self.curso.modificar_curso({
            'curso_id': id_curso
        }, {
            'nombre': nombre
        })
        print('''
        ========================
            Curso Editado !
        ========================
        ''')

    def eliminar_curso(self, id_curso):
        self.curso.eliminar_curso({
            'curso_id': id_curso
        })
        print('''
        ========================
            Curso Eliminado !
        ========================
        ''')
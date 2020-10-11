from classes.profesor import Profesor
from classes.profesor_curso import Profesor_curso
from classes.curso import Curso
from classes.periodo import Periodo
from classes.salon import Salon
from classes.malla import Malla
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Habilitar_controller:
    def __init__(self):
        self.profesor = Profesor()
        self.curso = Curso()
        self.profesor_curso = Profesor_curso()
        self.periodo = Periodo()
        self.salon = Salon()
        self.malla = Malla()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =======================
                    Habilitar Cursos
                =======================
                ''')
                menu = ["Habilitar salon", "Salir"]
                respuesta = Menu(menu).show()
                if respuesta == 1:
                    self.habilitar_salones()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')


    def habilitar_salones(self):
        print('''
        =============================================
            Habilitar curso por salones y periodo
        =============================================
        ''')
        print('De la siguiente lista elija el periodo que se habilitara >>\n')
        periodos = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodos, ['ID', 'Nombre', 'Desde', 'Hasta']))
        id_periodo_elegido = input_data("\nEscriba el ID del periodo escolar >> ", "int")
        buscar_periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo_elegido})
        if not buscar_periodo:
            print('\nEl periodo elegido no existe !')
            return
        print(f'\nElija el salon para el periodo: {buscar_periodo[1]} >> ')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['ID', 'Nombre']))
        id_salon_elegido = input_data("\nEscriba el ID del salon >> ", "int")
        buscar_salon = self.salon.obtener_salon({'id_salon': id_salon_elegido})
        if not buscar_salon:
            print('\nEl salon elegido no existe !')
            return
        print(f'\nElija el curso a habilitar para el salon: {buscar_salon[1]} >> ')
        cursos_profesores = self.profesor_curso.obtener_profesor_cursos('id_profesor_curso')
        cursos_disponibles = []
        if cursos_profesores:
            for pro_cur in cursos_profesores:
                curso_id = pro_cur[2]
                profesor_id = pro_cur[1]
                id_profesor_curso = pro_cur[0]
                curso = self.curso.obtener_curso({'curso_id': curso_id})
                curso_nombre = curso[1]
                profesor = self.profesor.obtener_profesor({'profesor_id': profesor_id})
                profesor_nombre = profesor[1]
                mallas = self.malla.buscar_mallas({
                    'id_periodo': id_periodo_elegido,
                    'id_salon': id_salon_elegido,
                    'id_profesor_curso': id_profesor_curso
                })
                if not mallas:
                    cursos_disponibles.append({
                        'codigo': id_profesor_curso,
                        'curso': curso_nombre,
                        'profesor_asignado': profesor_nombre
                    })
                else:
                    for curso_disponible in cursos_disponibles:
                        if curso_disponible['curso'] == curso_nombre:
                            cursos_disponibles.remove(curso_disponible)

        print(print_table(cursos_disponibles))
        id_profesor_curso = input_data('\nEscriba el codigo del curso disponible >> ', 'int')
        buscar_profesor_curso = self.profesor_curso.obtener_profesor_curso({'id_profesor_curso': id_profesor_curso})
        if not buscar_profesor_curso:
            print('\nEl codigo escogido no existe como curso disponible')
            return
        mallas = self.malla.buscar_mallas({
            'id_periodo': id_periodo_elegido,
            'id_salon': id_salon_elegido
        })
        if mallas:
            for malla in mallas:
                pro_curso = self.profesor_curso.obtener_profesor_curso({'id_profesor_curso': malla[3]})
                if pro_curso[2] == buscar_profesor_curso[2]:
                    print('\nEste curso ya existe para el salon en el periodo escogido !')
                    return
        self.malla.guardar_malla({
            'id_periodo': id_periodo_elegido,
            'id_salon': id_salon_elegido,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        =============================================================
            Curso habilitado con exito para el salon y el periodo
        =============================================================
        ''')
        input('\nPresione una tecla para continuar...')

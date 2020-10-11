from classes.profesor import Profesor
from classes.curso import Curso
from classes.profesor_curso import Profesor_curso
from classes.periodo import Periodo
from classes.salon import Salon
from classes.malla import Malla
from classes.nota import Nota
from classes.alumno import Alumno
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Notas_controller:
    def __init__(self):
        self.profesor = Profesor()
        self.curso = Curso()
        self.profesor_curso = Profesor_curso()
        self.periodo = Periodo()
        self.salon = Salon()
        self.malla = Malla()
        self.nota = Nota()
        self.alumno = Alumno()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ========================
                   Registro de Notas
                ========================
                ''')
                menu = ["Listado de notas", "Registrar notas", "Salir"]
                respuesta = Menu(menu).show()
                if respuesta == 1:
                    self.listar_notas()
                elif respuesta == 2:
                    self.registrar_notas()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_notas(self):
        print('''
        ========================
            Listado de Notas
        ========================
        ''')
        notas = self.nota.obtener_notas('id_nota')
        lista_notas = []
        if notas:
            for nota in notas:
                buscar_alumno = self.alumno.obtener_alumno({'alumno_id': nota[1]})
                buscar_malla = self.malla.obtener_malla({'id_malla': nota[2]})
                nota_calificacion = nota[3]
                periodo = self.periodo.obtener_periodo({'id_periodo': buscar_malla[1]})
                salon = self.salon.obtener_salon({'id_salon': buscar_malla[2]})
                profesor_curso = self.profesor_curso.obtener_profesor_curso({'id_profesor_curso': buscar_malla[3]})
                curso = self.curso.obtener_curso({'curso_id': profesor_curso[2]})
                profesor = self.profesor.obtener_profesor({'profesor_id': profesor_curso[1]})
                lista_notas.append((
                    nota[0],
                    buscar_alumno[1],
                    periodo[1],
                    salon[1],
                    curso[1],
                    profesor[1],
                    nota_calificacion
                ))
        print(print_table(lista_notas, ['ID', 'Alumno', 'Periodo Escolar', 'Salon', 'Curso', 'Profesor', 'Nota']))
        input("\nPresione una tecla para continuar...")

    def registrar_notas(self):
        print('''
        ===================================================
            Registro de notas para los alumnos por salon
        ===================================================
        ''')
        print('Eliga el alumno que se le asignara una nota >> \n')
        alumnos = self.alumno.obtener_alumnos('alumno_id')
        print(print_table(alumnos, ['ID', 'Nombres', 'Edad', 'Correo']))
        id_alumno_elegido = input_data('\nEscriba el ID del alumno >> ', 'int')
        buscar_alumno = self.alumno.obtener_alumno({'alumno_id': id_alumno_elegido})
        if not buscar_alumno:
            print('\nEl alumno elegido no existe !')
            return
        print(f'\nElija el curso y periodo a ser añadido a {buscar_alumno[1]} >> ')
        mallas = self.malla.obtener_mallas('id_malla')
        lista_mallas = []
        if mallas:
            for malla in mallas:
                periodo = self.periodo.obtener_periodo({'id_periodo': malla[1]})
                salon = self.salon.obtener_salon({'id_salon': malla[2]})
                profesor_curso = self.profesor_curso.obtener_profesor_curso({'id_profesor_curso': malla[3]})
                curso = self.curso.obtener_curso({'curso_id': profesor_curso[2]})
                profesor = self.profesor.obtener_profesor({'profesor_id': profesor_curso[1]})
                notas_agregadas = self.nota.buscar_notas({
                    'id_alumno': id_alumno_elegido,
                    'id_malla': malla[0]
                })
                if not notas_agregadas:
                    lista_mallas.append((
                        malla[0],
                        periodo[1],
                        salon[1],
                        curso[1],
                        profesor[1]
                    ))

        print(print_table(lista_mallas, ['Codigo', 'Periodo Escolar', 'Salon', 'Curso', 'Profesor']))
        id_malla_elegida = input_data('\nEscriba el codigo de la malla >> ', 'int')
        buscar_malla = self.malla.obtener_malla({'id_malla': id_malla_elegida})
        if not buscar_malla:
            print('\nEsta malla no existe !')
            return
        notas_alumnos = self.nota.buscar_notas({
            'id_alumno': id_alumno_elegido,
            'id_malla': id_malla_elegida
        })
        if notas_alumnos:
            print(f'\nYa existe una nota para el alumno {buscar_alumno[1]} en el curso seleccionado !')
            return
        periodo = self.periodo.obtener_periodo({'id_periodo': buscar_malla[1]})
        salon = self.salon.obtener_salon({'id_salon': buscar_malla[2]})
        profesor_curso = self.profesor_curso.obtener_profesor_curso({'id_profesor_curso': buscar_malla[3]})
        curso = self.curso.obtener_curso({'curso_id': profesor_curso[2]})
        profesor = self.profesor.obtener_profesor({'profesor_id': profesor_curso[1]})
        while True:
            print(f'\nAlumno:   {buscar_alumno[1]}')
            print(f'Periodo:    {periodo[1]}')
            print(f'Salon:      {salon[1]}')
            print(f'Profesor:   {profesor[1]}')
            print(f'Curso:      {curso[1]}')
            nota_ingresada = input_data('\nNota: >> ', 'int')
            if nota_ingresada > 20:
                print("La nota ingresada debe ser menor a 20!")
            else:
                break
        self.nota.guardar_nota({
            'id_alumno': id_alumno_elegido,
            'id_malla': id_malla_elegida,
            'nota': nota_ingresada
        })
        print('''
        ==============================
            Se califico al alumno !
        ==============================
        ''')
        input("\nPresione una tecla para continuar...")

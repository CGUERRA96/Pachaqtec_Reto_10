from connection.conn import Conexion

class Profesor_curso:
    def __init__(self):
        self.model = Conexion('profesor_curso')

    def guardar_profesor_curso(self, profesor_curso):
        return self.model.insert(profesor_curso)

    def obtener_profesor_curso(self, id_profesor_curso):
        return self.model.get_by_id(id_profesor_curso)

    def obtener_profesor_cursos(self, order):
        return self.model.get_all(order)

    def buscar_profesor_cursos(self, data_profesor_curso):
        return self.model.get_by_column(data_profesor_curso)

    def modificar_profesor_curso(self, id_profesor_curso, data_profesor_curso):
        return self.model.update(id_profesor_curso, data_profesor_curso)

    def eliminar_profesor_curso(self, id_profesor_curso):
        return self.model.delete(id_profesor_curso)

from connection.conn import Conexion

class Curso:
    def __init__(self):
        self.model = Conexion('cursos')

    def guardar_curso(self, curso):
        return self.model.insert(curso)

    def obtener_curso(self, id_curso):
        return self.model.get_by_id(id_curso)

    def obtener_cursos(self, order):
        return self.model.get_all(order)

    def buscar_cursos(self, data_curso):
        return self.model.get_by_column(data_curso)

    def modificar_curso(self, id_curso, data_curso):
        return self.model.update(id_curso, data_curso)

    def eliminar_curso(self, id_curso):
        return self.model.delete(id_curso)

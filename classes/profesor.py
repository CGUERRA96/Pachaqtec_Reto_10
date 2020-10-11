from connection.conn import Conexion

class Profesor:
    def __init__(self):
        self.model = Conexion('profesores')

    def guardar_profesor(self, profesor):
        return self.model.insert(profesor)

    def obtener_profesor(self, id_profesor):
        return self.model.get_by_id(id_profesor)

    def obtener_profesores(self, order):
        return self.model.get_all(order)

    def buscar_profesores(self, data_profesor):
        return self.model.get_by_column(data_profesor)

    def modificar_profesor(self, id_profesor, data_profesor):
        return self.model.update(id_profesor, data_profesor)

    def eliminar_profesor(self, id_profesor):
        return self.model.delete(id_profesor)

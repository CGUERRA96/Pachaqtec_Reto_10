from connection.conn import Conexion

class Estado:
    def __init__(self):
        self.model = Conexion('estados')

    def guardar_estado(self, estado):
        return self.model.insert(estado)

    def obtener_estado(self, id_estado):
        return self.model.get_by_id(id_estado)

    def obtener_estados(self, order):
        return self.model.get_all(order)

    def buscar_estados(self, data_estado):
        return self.model.get_by_column(data_estado)

    def modificar_estado(self, id_estado, data_estado):
        return self.model.update(id_estado, data_estado)

    def eliminar_estado(self, id_estado):
        return self.model.delete(id_estado)
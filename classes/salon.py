from connection.conn import Conexion

class Salon:
    def __init__(self):
        self.model = Conexion('salones')

    def guardar_salon(self, salon):
        return self.model.insert(salon)

    def obtener_salon(self, id_salon):
        return self.model.get_by_id(id_salon)

    def obtener_salones(self, order):
        return self.model.get_all(order)

    def buscar_salones(self, data_salon):
        return self.model.get_by_column(data_salon)

    def modificar_salon(self, id_salon, data_salon):
        return self.model.update(id_salon, data_salon)

    def eliminar_salon(self, id_salon):
        return self.model.delete(id_salon)

from connection.conn import Conexion

class Malla:
    def __init__(self):
        self.model = Conexion('malla_curricular')

    def guardar_malla(self, malla):
        return self.model.insert(malla)

    def obtener_malla(self, id_malla):
        return self.model.get_by_id(id_malla)

    def obtener_mallas(self, order):
        return self.model.get_all(order)

    def buscar_mallas(self, data_malla):
        return self.model.get_by_column(data_malla)

    def modificar_malla(self, id_malla, data_malla):
        return self.model.update(id_malla, data_malla)

    def eliminar_malla(self, id_malla):
        return self.model.delete(id_malla)

from connection.conn import Conexion

class Periodo:
    def __init__(self):
        self.model = Conexion('periodo_escolar')

    def guardar_periodo(self, periodo):
        return self.model.insert(periodo)

    def obtener_periodo(self, id_periodo):
        return self.model.get_by_id(id_periodo)

    def obtener_periodos(self, order):
        return self.model.get_all(order)

    def buscar_periodos(self, data_periodo):
        return self.model.get_by_column(data_periodo)

    def modificar_periodo(self, id_periodo, data_periodo):
        return self.model.update(id_periodo, data_periodo)

    def eliminar_periodo(self, id_periodo):
        return self.model.delete(id_periodo)

from connection.conn import Conexion

class Tipo_rol:
    def __init__(self):
        self.model = Conexion('tipo_rol')

    def guardar_tipo_rol(self, tipo_rol):
        return self.model.insert(tipo_rol)

    def obtener_tipo_rol(self, id_tipo_rol):
        return self.model.get_by_id(id_tipo_rol)

    def obtener_tipo_roles(self, order):
        return self.model.get_all(order)

    def buscar_tipo_roles(self, data_tipo_rol):
        return self.model.get_by_column(data_tipo_rol)

    def modificar_tipo_rol(self, id_tipo_rol, data_tipo_rol):
        return self.model.update(id_tipo_rol, data_tipo_rol)

    def eliminar_tipo_rol(self, id_tipo_rol):
        return self.model.delete(id_tipo_rol)
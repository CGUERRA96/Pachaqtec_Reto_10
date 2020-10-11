from connection.conn import Conexion

class Nota:
    def __init__(self):
        self.model = Conexion('notas')

    def guardar_nota(self, nota):
        return self.model.insert(nota)

    def obtener_nota(self, id_nota):
        return self.model.get_by_id(id_nota)

    def obtener_notas(self, order):
        return self.model.get_all(order)

    def buscar_notas(self, data_nota):
        return self.model.get_by_column(data_nota)

    def modificar_nota(self, id_nota, data_nota):
        return self.model.update(id_nota, data_nota)

    def eliminar_nota(self, id_nota):
        return self.model.delete(id_nota)

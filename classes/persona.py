from connection.conn import Conexion

class Persona:
    def __init__(self):
        self.model = Conexion('personas')

    def guardar_persona(self, persona):
        return self.model.insert(persona)

    def obtener_persona(self, id_persona):
        return self.model.get_by_id(id_persona)

    def obtener_personas(self, order):
        return self.model.get_all(order)

    def buscar_personas(self, data_persona):
        return self.model.get_by_column(data_persona)

    def modificar_persona(self, id_persona, data_persona):
        return self.model.update(id_persona, data_persona)

    def eliminar_persona(self, id_persona):
        return self.model.delete(id_persona)
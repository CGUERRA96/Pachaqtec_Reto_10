from psycopg2 import connect

#date -> Y-m-d => 2020-03-05 / 2020-12-20

class Conexion:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='127.0.0.1', 
                    user='postgres', password='123456', database='DB_colegio')
        self.cursor = self.db.cursor()


    def ejecutar_sentencia(self, query):
        self.cursor.execute(query)
        self.commit()

    def get_all(self, order):
        query = f'SELECT * FROM {self.table_name} ORDER BY {order}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(self, id_object):
        query = f'SELECT * FROM {self.table_name} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_by_column(self, data):
        list_select_where = []
        for field_name, field_value in data.items():
            list_select_where.append(f"{field_name}='{field_value}'")
        query = f'SELECT * FROM {self.table_name} WHERE {" AND ".join(list_select_where)}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.db.close()

    def commit(self):
        self.db.commit()
        return True

    def rollback(self):
        self.db.rollback()
        return True

    def insert(self, data):
        values = "'" + "', '".join(map(str, data.values())) + "'"
        query = f'INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({values})'
        self.ejecutar_sentencia(query)
        return True

    def update(self, id_object, data):
        list_update = []
        for field_name, field_value in data.items():
            list_update.append(f"{field_name} = '{field_value}'") # SET nombre = ''
        query = f'UPDATE {self.table_name} SET {", ".join(list_update)} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.ejecutar_sentencia(query)
        return True

    def delete(self, id_object):
        query = f'DELETE FROM {self.table_name} WHERE {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}'
        self.ejecutar_sentencia(query)
        return True

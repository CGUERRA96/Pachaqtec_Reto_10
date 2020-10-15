from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_personas(self):     #usar dni_persona como usuario para login
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  personas(
                id_persona SERIAL PRIMARY KEY NOT NULL,
                id_tipo_rol int NOT NULL,
                nombres varchar(150) NOT NULL,
                edad int NOT NULL,
                correo varchar(150) COLLATE NOT NULL,
                dni_persona int NOT NULL,
                password varchar(32) NOT NULL,
                CONSTRAINT FK_TipoRol FOREIGN KEY (id_tipo_rol) REFERENCES tipo_rol(id_tipo_rol)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
    
    def crear_cursos(self):        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  cursos(
                curso_id SERIAL PRIMARY KEY NOT NULL,
                nombre varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_malla_curricular(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  malla_curricular(
                id_malla SERIAL PRIMARY KEY NOT NULL,
                id_periodo int NOT NULL,
                id_salon int NOT NULL,
                id_profesor_curso int NOT NULL,
                FOREIGN KEY (id_periodo) REFERENCE periodo_escolar(id_periodo),
                FOREIGN KEY (id_salon) REFERENCE salones(id_salon),
                FOREIGN KEY (id_profesor_curso) REFERENCE profesor_curso(id_profesor_curso)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_notas(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  notas(
                id_nota SERIAL PRIMARY KEY NOT NULL,
                id_persona integer NOT NULL,
                id_malla integer NOT NULL,
                nota double precision NOT NULL,
                FOREIGN KEY (id_persona) REFERENCE personas(id_persona),
                FOREIGN KEY (id_malla) REFERENCE malla_curricular(id_malla)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_periodo_escolar(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  periodo_escolar(
                id_periodo SERIAL PRIMARY KEY,
                nombre_periodo varchar(150) NOT NULL,
                fecha_desde date NOT NULL,
                fecha_hasta date NOT NULL,
                estado_periodo varchar(25) DEFAULT 'aperturado'
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_profesor_curso(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesor_curso(
                id_profesor_curso SERIAL,
                id_persona int NOT NULL,
                id_curso int NOT NULL,
                id_estado int NOT NULL,
                FOREIGN KEY (id_profesor) REFERENCE personas(id_persona),
                FOREIGN KEY (id_curso) REFERENCE cursos(curso_id),
                FOREIGN KEY (id_estado) REFERENCE estados(id_estado)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_tipo_rol(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  roles(
                id_tipo_rol SERIAL PRIMARY KEY NOT NULL,
                tipo_rol varchar(25) NOT NULL,
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_salones(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  salones(
                id_salon SERIAL PRIMARY KEY NOT NULL,
                nombre_salon varchar(150) NOT NULL,
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_estados(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS estados(
                id_estado SERIAL PRIMARY KEY NOT NULL,
                nombre_estado varchar(20) not null
            );
            '''
        conn.ejecutar_sentencia(create_table_query)


conn = Conexion('sistema_colegio')
db= Database(conn)
db.crear_personas()
db.crear_cursos()
db.crear_malla_curricular()
db.crear_notas()
db.crear_periodo_escolar()
db.crear_profesor_curso()
db.crear_tipo_rol()
db.crear_salones()
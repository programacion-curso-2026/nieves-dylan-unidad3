import sqlite3

class Database:
    def __init__(self, db_name: str = "taller_mecanico.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_tables()

    def connect(self):
        """Establece la conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Conexión establecida con {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def create_tables(self):
        """Crea las tablas necesarias para la aplicación"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS mecanico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            direccion TEXT,
            especialidad TEXT,
            tiempo_practica TEXT,
            costo_x_hora REAL DEFAULT 10.0
        )
        """
        self.execute_query(create_table_query)
        print("Tabla 'mecanico' creada/verificada")

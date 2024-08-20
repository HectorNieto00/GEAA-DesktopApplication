import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_data = 'database/geaa.db'
        self.conexion = sqlite3.connect(self.base_data)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
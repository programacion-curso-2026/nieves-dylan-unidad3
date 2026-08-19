from database import Database
from mecanico import Mecanico
class MecanicoDAO:
    """Data Access Object para la entidad Mecanico"""

    def __init__(self, database: Database):
        self.db = database

    def crear_mecanico(self, mecanico: Mecanico) -> bool:
        """Crea un nuevo registro de mecánico en la base de datos"""
        query = """
        INSERT INTO mecanico (nombre, telefono, direccion, especialidad,
                             tiempo_practica, costo_x_hora)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (mecanico.nombre, mecanico.telefono, mecanico.direccion,
                 mecanico.especialidad, mecanico.tiempo_practica, mecanico.costo_x_hora)

        success = self.db.execute_query(query, params)

        if success:
            print(f"Mecánico '{mecanico.nombre}' creado exitosamente")
        else:
            print(f"Error al crear el mecánico '{mecanico.nombre}'")

        return success
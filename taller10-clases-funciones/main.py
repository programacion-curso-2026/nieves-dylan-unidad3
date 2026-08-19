from mecanico import Mecanico
from database import Database
from mecanico_dao import MecanicoDAO

# 1. Inicializar la base de datos y el DAO
db = Database()
mecanico_dao = MecanicoDAO(db)

# 2. Crear objetos de tipo Mecanico
mecanico_1 = Mecanico("David Guevara", "0992848484", "Via a la Costa", "Popular Mechanics with IA", 100)
mecanico_2 = Mecanico("Juan Perez", "0992848484", "Alborada", "Microservicios", 120)

# 3. (Opcional) Guardarlos en la base de datos usando el DAO
mecanico_dao.crear_mecanico(mecanico_1)
mecanico_dao.crear_mecanico(mecanico_2)
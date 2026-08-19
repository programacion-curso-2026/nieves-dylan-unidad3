class Mecanico:
    def __init__(self,nombre,telefono,direccion,especialidad,tiempo_practica, costo_x_hora=10):
        print("Estas llamando al Constructor")
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.especialidad = especialidad
        self.tiempo_practica = tiempo_practica
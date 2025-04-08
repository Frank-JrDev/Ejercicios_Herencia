class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def imprimir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Año: {self.año}")



class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo

    def imprimir_info(self): 
        super().imprimir_info()
        print(f"Modelo: {self.modelo}")



coche = Coche("Toyota", 2021, "Corolla")


coche.imprimir_info()
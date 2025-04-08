class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")



class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        
        super().__init__(nombre, especie)
        self.raza = raza

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self.raza}")



perro = Perro("Bobby", "Canino", "Labrador")

perro.imprimir_info()
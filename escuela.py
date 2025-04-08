class persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        pass


    def imprimir_info(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")



class Estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imrpimir_info (self):
        super().imprimir_info()
        print(f"Grado: {self.grado}")


estudiante = Estudiante ("Juan Orozco", 16, "11º Grado")

estudiante.imprimir_info()
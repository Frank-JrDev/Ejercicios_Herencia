# Ejercicios_Herencia
Este código crea dos clases: Persona y Estudiante.

Clase Persona
La clase Persona representa a una persona en general. Tiene dos atributos (propiedades):

nombre: Guarda el nombre de la persona.

edad: Guarda la edad de la persona.

También tiene un método:

imprimir_info: Imprime el nombre y la edad de la persona.

Clase Estudiante
La clase Estudiante es una subclase de Persona, es decir, hereda las propiedades de Persona. Además, agrega una nueva propiedad:

grado: Indica el grado o curso en el que está el estudiante.

El método imprimir_info también se "modifica" en Estudiante para imprimir el nombre, la edad y el grado del estudiante.

¿Cómo funciona?
Se crea una instancia de la clase Estudiante con el nombre, edad y grado del estudiante.

Llamamos al método imprimir_info para que imprima la información del estudiante: nombre, edad y grado.

Estudiante: Hereda nombre y edad de Persona y agrega grado.

Herencia: La clase Estudiante usa las propiedades de Persona y agrega algo nuevo (el grado del estudiante).

Este código demuestra cómo heredar propiedades y métodos de una clase en Python, lo que hace que el código sea más fácil de entender y reutilizar.


Ejercicio vehiculo:
Este script define una jerarquía de clases en Python para modelar vehículos y coches. La clase Vehiculo es la clase base, y la clase Coche hereda de ella. Ambas clases incluyen un método para imprimir información relevante sobre los objetos.

Clases:
Clase Vehiculo:

Propósito: Representa un vehículo genérico con atributos básicos como la marca y el año de fabricación.

Atributos:

marca: La marca del vehículo (ej. "Toyota").

año: El año de fabricación del vehículo (ej. 2021).

Métodos:

__init__(self, marca, año): Constructor que inicializa los atributos marca y año.

imprimir_info(self): Imprime en consola la marca y el año del vehículo.

Clase Coche (hereda de Vehiculo):

Propósito: Representa un coche específico, añadiendo el atributo modelo además de los atributos heredados de Vehiculo.

Atributos:

marca: Atributo heredado de Vehiculo.

año: Atributo heredado de Vehiculo.

modelo: El modelo del coche (ej. "Corolla").

Métodos:

__init__(self, marca, año, modelo): Constructor que inicializa los atributos heredados de Vehiculo y el nuevo atributo modelo. Se usa super() para llamar al constructor de la clase base Vehiculo.

imprimir_info(self): Sobrescribe el método imprimir_info de la clase base para incluir también el modelo. Llama a super().imprimir_info() para imprimir la información básica (marca y año) antes de imprimir el modelo.

Resumen:
Este script muestra un ejemplo de herencia en programación orientada a objetos, donde Coche extiende la funcionalidad de la clase Vehiculo, añadiendo el atributo modelo y sobrescribiendo el método imprimir_info para personalizar la salida.





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

Ejemplo
Cuando creamos un estudiante con el nombre "Juan Orozco", 16 años, y "11º Grado", y llamamos al método imprimir_info, la salida será:

makefile
Copiar
nombre: Juan Orozco
edad: 16
Grado: 11º Grado
Resumen
Persona: Tiene nombre y edad.

Estudiante: Hereda nombre y edad de Persona y agrega grado.

Herencia: La clase Estudiante usa las propiedades de Persona y agrega algo nuevo (el grado del estudiante).

Este código demuestra cómo heredar propiedades y métodos de una clase en Python, lo que hace que el código sea más fácil de entender y reutilizar.







class Estudiante:
    def __init__(self, nombre, edad): #Constructor de la clase estudiante
        self.nombre = nombre
        self.edad = edad
        print(f"Estudiante {self.nombre} creado.")

    def __del__(self): #Destructor de la clase estudiante
        print(f"Estudiante {self.nombre} eliminado.")

class Curso: #Constructor de la clase curso
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        print(f"Curso {self.nombre} creado.")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} ha sido agregado al curso {self.nombre}.")

    def __del__(self):#Destructor de la clase curso
        print(f"Cerrando curso {self.nombre}.")#Se llama automáticamente cuando el objeto Curso es eliminado.
        #Libera los recursos asociados al curso, en este caso, elimina a todos los estudiantes.
        for estudiante in self.estudiantes:
            del estudiante
        print(f"Curso {self.nombre} cerrado.")

estudiante1 = Estudiante("Juan", 20)
estudiante2 = Estudiante("Ana", 22)

curso_python = Curso("Programación en Python")
curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)










        
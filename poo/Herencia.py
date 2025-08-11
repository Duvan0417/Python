class Persona:
    def __init__(self,nombre,edad, nacionalidad):
        self.nombre = nombre 
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad}')

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario, especialidad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario
        self.especialidad = especialidad
    def presentarse(self):
        print(f'{self.mostrar_habilidad()}')

roberto = EmpleadoArtista("Roberto", 30, "Mexicano", "Cantar", "Cantante", 50000, "Pop")
roberto.presentarse()
class estudiante:
    def __init__(self,nombre,apellido,edad,curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
carlos = estudiante("Carlos", "Gomez", 20, "Ingeniería")
print(carlos.nombre)
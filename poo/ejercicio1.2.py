class Estudiante:
    def __init__(self,nombre,apellido,edad,curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
    def estudiar(self):
        print("Estudiando...")
print("Ingrese los datos del estudiante:")
nombre = input("Ingrese el nombre:")
edad = int(input("Ingrese la edad:"))
apellido = input("Ingrese el apellido:")
curso = input("Ingrese el curso:")

estudiante = Estudiante(nombre, apellido, edad, curso)

print(f""" datos del estudiante:
           -----------
           nombre: {estudiante.nombre}
           apellido: {estudiante.apellido}
           edad: {estudiante.edad}
           curso: {estudiante.curso}
""")
while True:
    estudiar = input("ingresa la palabra 'estudiar'")
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break
    else:
        print("ingresa un valor valido")
"""
print(10>9) #mayor que
print(10<9) #menor que
print(10==9) #igual que
print(10!=9) #diferente que
print(10>=9) #mayor o igual que
print(10<=9) #menor o igual que

"""
"""
# Ejemplo de uso de operadores booleanos
a = 100
b = 200
if a < b:
    print("hola")
else:
    print("adios")
"""
#Todas las variables sin una asiganacion vacia devueleven True
#Las variables con una asignacion vacia devuelven False
"""
saludo = "Hola"
num = 12
fruits = ["manzana", "banana", "cereza"]
g = ""
print(bool(saludo))
print(bool(num))
print(bool(fruits))
print(bool(g))
"""
# Los siguientes ejemplos muestran cómo las variables vacías devuelven False
"""
bool("")  # False
bool(None)  # False
bool(0)  # False
bool([])  # False
bool({})  # False
bool(False)  # False
"""
"""
class myclass:
    def __len__(self): #self me permite acceder a la instancia de la clase
        return 0
myobj = myclass()
print(bool(myobj))  # False, porque __len__ devuelve 0
"""
# las funciones también pueden devolver valores booleanos
"""
def myfunction():
    return True
print(bool(myfunction()))
"""
"""
def myfunction():
    a = input("Ingrese un valor: ")
    return bool(a)
if myfunction():
    print("Es verdadero")
else:
    print("Es falso")
"""
# isinstance() sirve para verificar el tipo de una variable
"""
x = 10
print(isinstance(x, int))  # True, porque x es un entero
print(isinstance(x,str))  # False, porque x no es una cadena
"""


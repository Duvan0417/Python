# Tuplas y Bucles en Python
#De la siguiente manera puedo recorrer una lista utilizando un bucle for
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
for i in range(len(thislist)):
    print(thislist[i])  # Imprime cada elemento de la lista usando un bucle for
"""
# De la siguiente manera puedo recorrer una lista utilizando un bucle while
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
i = 0
while i < len(thislist):
    print(thislist[i])# Imprime cada elemento de la lista usando un bucle while
    i += 1
"""
# la siguiente forma es una manera corta de recorrer una lista
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
[print(x) for x in thislist]  # Imprime cada elemento de la lista usando una comprensión de lista
"""
# De la siguiente manera puedo filtrar una lista utilizando un bucle for
"""
fruits = ['apple', 'banana', 'cherry', 'orange', 'watermelon', 'kiwi']
#los datos de la lista pasaran a una nueva lista si cumplen con la condicion
# en este caso, si la fruta contiene la letra 'a'
newlist = []

# este for recorre cada elemento de la lista 'fruits'
# y verifica si contiene la letra 'a' mediante una condicional if
# si cumple la condicion, se agrega a la nueva lista 'newlist'
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)
"""
# Este metodo es una forma más corta de filtrar una lista
"""
object = ['mesa', 'silla', 'cama', 'escritorio', 'televisor']
filter= [x for x in object if 'l' in x]
print(filter)  # Imprime los objetos que contienen la letra 'l'
"""
# De esta forma puedo filtrar una lista utilizando un bucle for y una condicional pero solo si es diferente a un elemento especifico
"""
object = ['mesa', 'silla', 'cama', 'escritorio', 'televisor']
filter= [x for x in object if x != 'silla']  # Filtra los objetos que no son 'silla'
print(filter)  # Imprime los objetos que no son 'silla'
"""
object = ['mesa', 'silla', 'cama', 'escritorio', 'televisor']
#filter= [x for x in range(10)] # esta funcion crea una lista de números del 0 al 9
#filter= [x for x in range(10)  if x < 5] # esta funcion crea una lista de números del 0 al 4
#filter= [x.upper() for x in object]  # Convierte todos los objetos de la lista a mayúsculas
#filter= ['hello' for x in object]  # Crea una lista con el mismo número de elementos que 'object', pero todos son 'hello'
filter= [x if x != 'silla' else 'cama' for x in object] # Reemplaza 'silla' por 'cama' en la lista, manteniendo los demás elementos iguales
print(filter)  # Imprime todos los objetos de la lista

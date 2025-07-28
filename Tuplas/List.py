#La funcion len() me permite el numero de datos de una lista
"""
list = ["apple","banana", "cherry"]
print(len(list))
"""
#Estos son los tipos de datos para una lista
"""
list1 = ["apple","banana","cherry"]
list2 = [1,2,3,4,5,6]
list3 = [True, False, False]
"""
#En una misma lista pueden haber diferntes tipos de datos
"""
list1 = ["abc",34, True, 40, "male"]
"""
#En python el tipo de dato de una lista es list
"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
"""
#De la siguiente manera puedo consultar un solo elemento de una array
"""
mylist = ['apple','banana','cherry']
print(mylist[1])
"""
#De la siguiente manera puedo consultar el ultimo elemto del array
"""
mylist = ['apple','banana','cherry']
print(mylist[-1])
"""
#puedo especificar un rango
"""
mylist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
print(mylist[2:5])
"""
#asigno un limite para imprimir en la lista
"""
mylist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
print(mylist[:4])
"""
#Va a imprimir desde el indice dos del array
"""
mylist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
print(mylist[2:])
"""

# mylist[-4:-1] selecciona una porción de la lista usando índices negativos.
# En este caso, -4 corresponde al cuarto elemento desde el final ('cherry')
# y -1 corresponde al último elemento, pero el rango no lo incluye.
# Por lo tanto, imprime los elementos desde 'cherry' hasta 'watermelon' (sin incluir 'kiwi').
"""
mylist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
print(mylist[-4:-1])  # Salida: ['cherry', 'orange', 'watermelon']
"""
mylist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
x = input("Ingrese el nombre de una fruta: ")
if x in mylist:
    print("si, {} está en la lista".format(x))
else:
    print("no, {} no está en la lista".format(x))
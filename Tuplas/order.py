# sirve para ordenar una lista en el caso de las palabras lo hace en orden alfabetico
# en caso que sea numeros lo hace de menor a mayor
"""
thislist = ['apple', 'banana', 'cherry', 'orange', 'watermelon', 'kiwi']
thislist.sort()  # Ordena la lista en orden ascendente
print(thislist)  # Imprime la lista ordenada
"""
# orden la lista en orden descendente de mayor a menor
# el parametro de reverse es un booleano que indica si se debe ordenar en orden descendente
# este mismo se encuentra por defecto en False, por lo que si no se especifica, la lista se ordenará en orden ascendente.
"""
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse = True)
print(numbers)  # Imprime la lista ordenada en orden descendente
"""


# CONSULTAR EL FUNCIONAMIENTO



# con la siguiente funcion  puedo ordenar una lista en este caso le estoy especificando que ordene por la distancia a 50
# la funcion my_func toma un numero n y devuelve su distancia a 50
"""
def my_func(n):
    return abs(n - 50)
numbers = [100, 50, 65, 82, 23]
numbers.sort(key=my_func)
print(numbers)  # Imprime la lista ordenada según la función my_func
"""
# el metodo sort() prioriza las letras en ayusculas antes que las minúsculas al ordenar alfabéticamente.
# Por lo tanto, las palabras que comienzan con mayúscula aparecerán antes que las
"""
thislist = ['apple', 'Banana', 'cherry', 'Orange', 'watermelon', 'kiwi']
thislist.sort()
print(thislist)  # Imprime la lista ordenada en orden ascendente
"""
# uso de sort() con el parametro key y lower
# El método sort() con el parámetro key permite personalizar el criterio de ordenación.
"""
thislist = ['apple', 'Banana', 'cherry', 'Orange', 'watermelon', 'kiwi']
thislist.sort(key=str.lower) # con lower se ignoran las mayúsculas y minúsculas al ordenar
# Esto significa que las palabras se ordenarán alfabéticamente sin tener en cuenta si están
print(thislist)  # Imprime la lista ordenada en orden ascendente, ignorando mayúsculas y minúsculas
"""
# puedo invertir el orden de los elementos de una lista utilizando el metodo reverse()
# Este método invierte el orden de los elementos en la lista, sin ordenarlos alfabéticamente.
"""
thislist = ['apple', 'Banana', 'cherry', 'Orange', 'watermelon', 'kiwi']
thislist.reverse()
print(thislist)  # Imprime la lista en orden inverso
"""

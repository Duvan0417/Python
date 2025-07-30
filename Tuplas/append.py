
# De la siguiente manera puedo agregar un elemento al final de la lista
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
thislist.append("orange")  # Agrega 'orange' al final de la lista
print(thislist)  # Imprime la lista actualizada
"""
# De esta manera puedo agregar un elemento a la lista en la posicion que yo quiera
"""
thislist = ['apple','banana','cherry',]
thislist.insert(1,"orange")
print(thislist)  # Imprime la lista actualizada
"""
# De esta manera puedo agregar elemeentos de una lista a otra lista
# con el metodo extend() no solo puedo agregar cualquier objeto iterable como una lista,
# sino que también puedo agregar elementos de otro iterable como un conjunto o una tupla y diccionarios.
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
tropical = ['mango', 'papaya']
thislist.extend(tropical) # Este metodo agrega los elementos de otra lista al final de la lista thislist
print(thislist)  # Imprime la lista actualizada
"""


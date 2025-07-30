# De la siguiente manera puedo eliminar un elemento de la lista utilizando el metodo remove()
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
thislist.remove("banana")  # Elimina 'banana' de la lista
print(thislist)  # Imprime la lista actualizada
"""
# si hay mas de un elemento con el mismo nombre, solo elimina el primero que encuentra
"""
thislist = ['apple','banana','banana','banana','banana',]
thislist.remove("banana")
print(thislist)  # Imprime la lista actualizada
"""
# De la siguiente manera puedo eliminar un elemento de la lista utilizando el metodo pop()
# si no se especifica un indice, elimina el ultimo elemento de la lista
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
thislist.pop(1)  # Elimina el elemento en la posición 1 (índice 1)
print(thislist)  # Imprime la lista actualizada
"""
# al igual que el metodo remove() si hay mas de un elemento con el mismo nombre, solo elimina el primero que encuentra
"""
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
del thislist[1]  # Elimina el elemento en la posición 1 (índice 1)
print(thislist)  # Imprime la lista actualizada
"""
# El siguiente metodo elimina todos los elementos de la lista
# y deja la lista vacía, pero no elimina la lista en sí.
thislist = ['apple','banana','cherry','orange', 'watermelon','kiwi']
thislist.clear()  # Elimina todos los elementos de la lista
print(thislist)  # Imprime la lista actualizada, que estará vacía

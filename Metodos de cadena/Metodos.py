texto = "    hoLa, muNdo!, planet  "
text = "Hola, planet"
text1 = "Hola, planet"

print("Mayusculas:", texto.upper())  # Convierte a mayúsculas
print("minusculas:", texto.lower())  # Convierte a minúsculas
print("Capitalizado:", texto.capitalize())  # Capitaliza la primera letra
print("Titulo:", texto.title())  # Capitaliza la primera letra de cada palabra
print("swapcase:", texto.swapcase())  # Intercambia mayúsculas y minúsculas
print("remplazar:", texto.replace("muNdo", "universo"))  # Reemplaza una subcadena
print("Eliminar espacios:", texto.strip())  # Elimina espacios al inicio y al final
print("Eliminar espacios al inicio:", texto.lstrip())  # Elimina espacios al inicio   
print("Eliminar espacios al final:", texto.rstrip())  # Elimina espacios al final
print("Dividir  en palabras:", texto.split())  # Divide en palabras
print("Dividir en comas:", texto.split(","))  # Divide en comas
print("Unir con guiones:","-".join(texto.split()))  # Une con guiones
print("Longitud del texto:", len(texto))  # Longitud del texto
print("Contar 'a':", texto.count("a"))  # Cuenta ocurrencias de 'a' cuenta la cantidad de veces que aparece una letra
print("Encontrar 'mundo':", texto.find("mundo"))  # Encuentra la posición de 'mundo'
print("Encontrar 'muNdo':", texto.index("muNdo"))  # Encuentra la posición de 'muNdo' (lanza error si no lo encuentra)
print("Comienza con 'Hola':", text.startswith("Hola"))  # Verifica si comienza con 'hoLa'
print("Termina con 'planet':", text.endswith("planet"))  # Verifica si termina con 'planet'
print("Repetir texto:", texto * 2)  # Repite el texto dos veces
print("Comparar textos:", text1 == text)  # Compara si los textos son iguales
print("Comparar textos (ignore case):", text1.lower() == text.lower())  # Compara ignorando mayúsculas y minúsculas5
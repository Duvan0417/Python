#Este me permite utlizar comillas dobles, cuando no se permiten dentro de una cadena
text = "hola\"mundo\"desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El siguiente es para un salto de linea
text = "hola\nmundo\ndesdemarte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El siguiente es para un salto de linea y tabulacion
text = "hola\n\tmundo\ndesdemarte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El single quote me permite utilizar comillas simples dentro de una cadena con comillas simples
text = 'hola\'mundo desde marte\''
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El backslash permite utilizar \ dentro de una cadena
text = "hola\\mundo\\desde\\marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")   
#carriage return es un salto de linea que regresa al inicio de la linea
text = "hola\r mundo desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El backspace retroce del cursor un posicion
text = "hol\bla mundo desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El form feed este permite avanzar una pagina o a una seccion
text = "hola\fmundo desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El octal representa un caracter ASCCI en octal
text = "hola\101 mundo desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
#El hexadecimal representa un caracter ASCCI en hexadecimal
text = "hola\x41 mundo desde marte"
print(text)
print("////////////////////////////////////////////////////////////////////////")
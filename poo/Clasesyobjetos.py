class Celular ():
     def __init__(self, marca, modelo, color, precio):
          self.marca = marca
          self.modelo = modelo
          self.color = color
          self.precio = precio
     def llamar(self):
            print(f'Llamando... desde el celular de marca {self.modelo}')
     def enviar_mensaje(self):
            print(f'Enviando mensaje... desde el celular de marca {self.modelo}')

Celular1 = Celular("Samsung", "Galaxy S21", "Negro", 799)
Celular2 = Celular("Apple", "iPhone 13", "Blanco", 999)
Celular3 = Celular("Google", "Pixel 6", "Verde", 599)


Celular1.llamar()

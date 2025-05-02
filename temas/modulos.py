import math

print(math.sqrt(25))  # Imprime la raíz cuadrada de 25
print(math.pi)  # Imprime el valor de pi

from math import sqrt, pi

print(sqrt(36))  # Imprime la raíz cuadrada de 36
print(pi)  # Imprime el valor de pi (aún necesitamos el módulo math para acceder a pi)

from math import *
print(sqrt(49))  # Imprime la raíz cuadrada de 49

import random
import datetime
import os 

import random

# Generar un número entero aleatorio entre 1 y 10 (ambos incluidos)
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio: {numero_aleatorio}")

# Elegir un elemento aleatorio de una lista
lista_colores = ["rojo", "verde", "azul", "amarillo"]
color_elegido = random.choice(lista_colores)
print(f"Color aleatorio: {color_elegido}")

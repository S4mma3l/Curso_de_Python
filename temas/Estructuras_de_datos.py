# Listas

frutas = ["banana", "manzana", "pera", "naranja", "kiwi"]
print(type(frutas))

print(frutas[0])
print(frutas[-1])
frutas.append("mango")
print(frutas[-1])
print(frutas)

#  Tupla

coordenadas = (1, 2, 3, 4, 5)
print(type(coordenadas))

# Diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(type(persona))
print(persona["nombre"])
persona["edad"] = 26
print(persona["edad"])

# Conjuntos

colores = {"rojo", "verde", "azul"}
numeros_repetidos = [1, 2, 2, 3, 4, 4, 5]
conjunto_numeros = set(numeros_repetidos)

print(colores) # El orden puede variar
print(conjunto_numeros) # -> {1, 2, 3, 4, 5}
colores.add("amarillo") # Añadir un elemento
print(colores)
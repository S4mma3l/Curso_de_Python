#  for

# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar sobre una cadena de texto
for letra in "Python":
    print(letra)

# Iterar sobre un rango de números
# range(5) genera una secuencia de 0 a 4
for i in range(5):
    print(f"Contando: {i}") # Usamos f-strings para incluir el valor de i en el texto

# range

# range(5)  # Genera una secuencia de números del 0 al 4
# range(1, 10)  # Genera una secuencia de números del 1 al 9
# range(1, 10, 2)  # Genera una secuencia de números del 1 al 9 con un paso de 2 (1, 3, 5, 7, 9)
# range(10, 0, -1)  # Genera una secuencia de números del 10 al 1 (decreciente)

for j in range(2, 7): # Números del 2 al 6
    print(j)

for k in range(10, 0, -2): # Números del 10 al 2 (saltando de 2 en 2 hacia atrás)
    print(k)

#  while

contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador = contador + 1 # Importante: incrementamos el contador para que la condición eventualmente sea False

print("Fin del bucle while")


# break and continue

# Ejemplo con break
for numero in range(10):
    if numero == 5:
        break # Salimos del bucle cuando el número es 5
    print(numero) # Imprime 0, 1, 2, 3, 4

print("-" * 10) # Línea separadora

# Ejemplo con continue
for numero in range(10):
    if numero % 2 == 0: # Si el número es par
        continue # Salta al siguiente número
    print(numero) # Imprime 1, 3, 5, 7, 9 (solo números impares)
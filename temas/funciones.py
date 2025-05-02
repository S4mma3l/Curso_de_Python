#  funcion sencillas

def saludar():
    """Esta función simplemente imprime un saludo.""" # Esto es un docstring, explica qué hace la función
    print("¡Hola! Bienvenido al curso.")

# Llamando a la función para que se ejecute
saludar()
saludar() # Puedes llamarla múltiples veces

#  funciones con parametros

def saludar_a_persona(nombre):
    """Esta función saluda a una persona específica."""
    print(f"¡Hola, {nombre}!")

# Llamando a la función con diferentes argumentos (los valores que pasas a los parámetros)
saludar_a_persona("Ana")
saludar_a_persona("Pedro")
# saludar_a_persona(input("¿Cómo te llamas?")) # Puedes pedirle al usuario que ingrese su nombre

#  Funciones con múltiples parámetros
def sumar(num1, num2):
    """Esta función suma dos números e imprime el resultado."""
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")

sumar(5, 3)
sumar(10, -2)

# funciones con retorno (return)

def multiplicar(num1, num2):
    """Esta función multiplica dos números y devuelve el resultado."""
    resultado = num1 * num2
    return resultado # Devolvemos el resultado

# Llamamos a la función y guardamos el valor devuelto en una variable
mi_resultado = multiplicar(4, 6)
print(f"El resultado de la multiplicación es: {mi_resultado}")

# Puedes usar el valor devuelto directamente
print(f"El doble del resultado es: {multiplicar(4, 6) * 2}")
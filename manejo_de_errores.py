try:
    # Código que podría causar un error
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una división por cero
    print("¡Error! No se puede dividir por cero.")
except ValueError:
    # Código que se ejecuta si el usuario ingresa algo que no es un número entero
    print("¡Error! Debes ingresar números enteros válidos.")
except Exception as e:
    # Un except general para capturar cualquier otro error
    # 'as e' guarda la información del error en la variable 'e'
    print(f"Ocurrió un error inesperado: {e}")

print("El programa continúa después del manejo de errores.")
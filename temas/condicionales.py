#  condicional if

edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes votar.") # Este print también está dentro del bloque if porque está indentado.

print("Este mensaje siempre se muestra.") # Este print está fuera del bloque if.


# condicional if-else

temperatura = 15

if temperatura > 25:
    print("Hace calor.")
else:
    print("No hace calor.")
    print("Quizás hace frío o está templado.")


# condicional if-elif-else

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Notable")
elif nota >= 50:
    print("Aprobado")
else:
    print("Suspenso")
# Ejercicio 8. ¿Cuanto es el X por ciento de X numero?

numero= int(input("Introduce un numero: "))
porcentaje= int(input("Indtroduce el porcentaje que deseas obtener: "))

operacion=(numero*(porcentaje/100))

print(f"El {porcentaje} % de {numero} es {operacion}")
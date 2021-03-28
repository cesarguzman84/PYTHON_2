# Ejercicio 2. Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista. Plus:Usar while y for

coleccion = []

for contador in range (0,120):
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)
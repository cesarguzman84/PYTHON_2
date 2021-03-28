# Ejercicio 3. Escribir un programa que muestre los cuadrados de los primeros 60 numeros naturales

# WHILE

contador = 0

while contador<=60:

    cuadrado= contador*contador

    print(f"El cuadrado de {contador} es {cuadrado}")

    contador +=1


#FOR

for numero in range(61):
    
    cuadrado= numero*numero

    print(f"El cuandrado del {numero} es {cuadrado}")

    
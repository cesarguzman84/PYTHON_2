# Ejercicio 7. Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

numero1= int(input("Introduce primer numero: "))
numero2= int(input("Introduce segundo numero: "))

if numero1<numero2:

    for x in range (numero1, (numero2+1)):

        if x%2 == 0:
            print(f"{x} es par")

        else:
            print(f"{x} es impar")
else:
    print("El numero 1 debe ser mayor al numero 2")

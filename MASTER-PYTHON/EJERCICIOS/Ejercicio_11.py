"""Ejercicio 1.1 Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-Hacer funcion que recorra listas de numeros y devuelva string
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear  lista

numeros=[13,64,25,72,33,15,19,40]

# Crear funcion que recorra la lista y devuelva string

def mostrarLista(lista):
    resultado=""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"
    return resultado



#Recorrer y mostrar

print("#######Recorrer y mostrar#######")


for numero in numeros:
    print(numero)

# Ordenar y mostrar
print("###### Ordenar y mostrar")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar longitud
print("###### Mostrar longitud")
print(len(numeros))

# Busqueda en la lista
print("######### Busqueda en la lista ###############")

Busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(Busqueda, int)

while not comprobar or Busqueda <=0:

    Busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {Busqueda}")

print(f"########## Buscar en la lista el numero {Busqueda} ###########")

search = numeros.index(Busqueda)

print(f"El numero buscado existe en la lista, es el indice: {search}")
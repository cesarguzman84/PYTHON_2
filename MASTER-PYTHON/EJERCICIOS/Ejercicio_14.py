# Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable 

def comprobarTipado(dato, tipo):
    test= isinstance(dato, tipo)
    result = ""

    if test:
        f"El dato es del tipo: {type(dato)}"
    else:
        result= "El tipo de dato no es correcto"
    return result

mi_lista = ["Hola mundo", 77]
titulo = "Master en python"
numero = 100
verdadero = True

print(comprobarTipado(titulo, list))
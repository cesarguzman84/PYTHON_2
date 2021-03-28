class persona:
    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad
persona1 = persona("Cesar", 36)
persona2 = persona("Lina", 35)
persona3 = persona("Leidy", 30)


print(persona1.nombre)
print(persona2.nombre, persona2.edad)
print(persona3.nombre)


class animal:
    def __init__(self, raza, familia) :
        self.raza = raza
        self.familia = familia

animal1=animal("perro", "canino")
animal2 = animal("gato", "felino")

print(animal1.raza)
print(animal2.raza)

class coche(): # esta es la clase y sus propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar (self): #este es el metodo o comportamiento
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche = coche() #esto es instanciar o ejemplarizar una clase

print("El largo del coche es ", miCoche.largoChasis)
print("El coche tiene:  ", miCoche.ruedas, " ruedas")
#miCoche.arrancar()

print(miCoche.estado())
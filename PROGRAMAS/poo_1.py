class Coche(): # esta es la clase y sus propiedades

    def __init__(self): # este es el metodo constructor, define las propiedades iniciales de la clase

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #anteponiendo __ estamos encapsulando ruedas
        self.__enmarcha = False

    def arrancar (self, arrancamos): #este es el metodo o comportamiento
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and  chequeo==False):
            return "Algo a ido mal en el chequeo. No podemos arrancar"

        else:

            return "El coche esta parado"
            
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de  ", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        

miCoche = Coche() #esto es instanciar o ejemplarizar una clase


print(miCoche.arrancar(True))
miCoche.estado()

print("------------A continuacion creamos el segundo objeto")

miCoche2=Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()
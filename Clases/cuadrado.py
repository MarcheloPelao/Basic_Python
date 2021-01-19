#METODO ESTATICO Y METODO DE CLASE
#metodo es una funcion que esta asociad a una instacia de la clase
# la cual mofifica los atributos de instancia de la clase
#UN metodo estatico es realmente una función que puede ser utiliza tanto por
# la clase y por una instancia de la misma y en la cual no se modifican ni
# se acceden a atributos de instancias
# a diferencia de unmetodo de clase el cual esta asociado  unicamente a la
#clase y en el cual si se puede acceder a otros metodos estaticos o bien a
#atributos de clases

class Cuadrado:

    def __init__(self,lado):
        self.lado=lado

    @staticmethod
    def ayuda():
        print('Área del cuadrado= lado**2')

    def area(self):
        return self.lado**2
    @classmethod #metodo de clase
    def cuadrado_8(cls):
        cls.ayuda() #podemos llamr al metodo ayuda
        return cls(8) #cuando usamos metodo de clase se debe lalamr con cls




#una clase abstracta es aquella que no se puede instanciar, es decir no
# se pueden crear objeto de dicha clase
#para especidicar que un metodo es abstracto importaremos el modulo abc

from abc import abstractmethod,ABC

class Mascota(ABC):#con esto indicamos que Mascota es una clase abstracta

    def __init__(self,nombre,dueño):
        self.nombre=nombre
        self.dueño=dueño

    @abstractmethod
    # def sonido(self):# en este caso sonido es un metodo abstracto ya que
    #     # no sabemos que animal sera ingresado
    #     pass
    def sonido(self): #ahora implementamos el metodo para que el codigo
        # funcione al pasar la clase a abstracta
        print('Guauuu!!!')

class Perro(Mascota):

    def sonido(self):
        print('guauuu!!')


if __name__=='__main__':
    # mascota=Mascota('Rufo','Manuela') #no se puede instanciar este objeto
    # ya que mascota es una clase abstracta ahora
    perro=Perro('Nino','Luis')
    # mascota.sonido()
    perro.sonido()

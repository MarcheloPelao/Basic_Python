class Mascota:

    def __init__(self,nombre,dueño):
        self.nombre=nombre
        self.dueño=dueño

    def jugar(self):
        print(f'Juega {self.nombre}')

class Perro(Mascota):
    #redifiniendo el metodo init

    def __init__(self,nombre,dueño,raza):
        super().__init__(nombre,dueño)#llamamos al metodo init de la clase
        # padre con la funcion super(), pasando como argumento el nombre como
        # el dueño
        self.raza=raza #se crea para la clase Perro un atributo de instancia
        # con la raza del perro

    def jugar(self):
        super().jugar()#con está función podemos llamar al metodo jugar de
        # la clase padre REDEFINIENDO, ya que si no la colocamos estamos SOBREESCRIBIENDO
        #el metodo jugar de la clase padre.
        print('Correr y Ladrar')

    def sonido(self):
        print('Guauuu')

class PerroMordedor(Perro):
    #esta clase hereda de la clase Perro y a su vez como la clase Perro
    # como la clase Perro hereda de la clase Mascota, está tambien va a
    # heredar los atributos de la clase Mascota
    def morder(self):
        print('Mordiendo')


if __name__=='__main__':

    mascota=Mascota('Nieve','Maria') #definimos objeto mascota
    print(f'Nombre: {mascota.nombre} ; Dueño: {mascota.dueño}')
    perro=Perro('sultan','Manolo','Chihuahua') #definimos objeto perro
    perro.jugar()
    print(f'Nombre: {perro.nombre}; Dueño: {perro.dueño}')
    print(f'Raza: {perro.raza}')
    perro.sonido()
    p_mordedor=PerroMordedor('Rocky','Alberto','Caniche ') #definimos objeto
    # p_mordedor
    print(f'Nombre del perro mordedor: {p_mordedor.nombre}')
    p_mordedor.jugar()
    p_mordedor.sonido()
    p_mordedor.morder()
    #funciones importantes en clases
    print(isinstance(p_mordedor,Perro)) #p_mordedor es instancia de Perro
    # porque hereda de ella =True
    print(isinstance(perro, Perro)) #el objeto perro es instancia de Perro
    # porque directamente es objeto de está clase=True
    print(isinstance(perro, PerroMordedor)) #perro no es instancia de la clase
    # PerroMordedor, porque es una clase hija (subclase)=False
    print(issubclass(PerroMordedor,Mascota)) #vamos a ver que PerroMordedor es
    # subclase de Mascota=True
    print(issubclass(Mascota, Perro)) #mascota no es subclase de la clase perro
    #esto es al reves =False
    print(issubclass(Perro, Mascota)) #perro es subclase de Mascota es
    # verdadero
    #ahora para saber si un objeto tiene asociado un atributo podemos usar la
    #funcion hasattr(),primero se pasa el objeto y luego el atributo
    if hasattr(mascota,'raza') :
        print(getattr(mascota,'raza',None)) #le pasamos tres argumentos, el
        # tercero es por si no tuviera el atributo no hace nada, en este caso
        # será False porque el atributo raza es parte de las clase Perro
    else:
        print('Mascota no define el atributo raza')

    if hasattr(mascota,'sonido') :
        print(getattr(mascota,'sonido',None))

    else:
        print('Mascota no define el atributo sonido')

    #otra manera de ver lo mismo es con getattr
    raza=getattr(mascota,'raza',None) #si no es atributo devuelve None, si no
    # colocamos el tercer argumento devuelve una exepcion Atribute Error
    # indicando que no es atributo
    print(raza)
    raza = getattr(perro, 'raza', None) #acá si  tiene el atrubuto raza
    # el objeto perro ya que apunta a la clase Perro, por lo tanto va a
    # mostrar la raza por pantalla
    print(raza)




#atributos especialesque implemnta una clase en python comienzan y terminan con
#__

class Perro:

    def __init__(self,nombre): #Se usa para crear un objeto en una clase
        self.nombre=nombre

    def __str__(self):
        return f'soy el perro {self.nombre}'

    def __repr__(self): #muestra la representacion formal del objeto, los
        # programadores lo usan para debugear codigo
        return f'atributos_especiales.Perro({self.nombre})'

if __name__=='__main__': #el atributo name hace referencia al nombre del modulo
    # print(Perro.__name__) #hace referencia al nobre de la clase
    # print(Perro.__dict__) # espacio de nombres de la clase
    # print(Perro.__module__)# indica el modulo donde esta la clase
    perro=Perro('Maya')
    print(perro)
    print('Soy el perro {}'.format(perro))
    perro_str=str(perro)
    print(perro_str)
    print(repr(perro))
    perros=[perro]
    print(perros)

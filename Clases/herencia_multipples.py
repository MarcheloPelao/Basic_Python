class A:
    def saludar(self,nombre):
        print('hola', nombre)


class B(A):
    def saludar(self,nombre):
        super().saludar(nombre)
        print('¿Nos vamos de fiesta?')


#herencia multiple de a y b

class C(A):
    def saludar(self,nombre):
        super().saludar(nombre)
        print('¿Vamos al cine?')

class D(B,C):

    def saludar(self,nombre):
        super().saludar(nombre)
        print('Parece que va a llover')

#definiendo un punto de entrada principal al programa

if __name__=='__main__':
    #demostrando que el objeto c herera las funcionalidades de A y B
    obj_d=D()
    obj_d.saludar(' Marcelo')
    #metodo mro devuelve la jerarquia de herencia
    print(D.mro())
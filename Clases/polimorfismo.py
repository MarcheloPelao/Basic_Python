# en programacion orientada a objeto, polimmorfismo es la capacidad que
# tiene un objeto de tomar más de una forma
# permite que una entidad pueda referenciar a distintas instancias de
# diferentes clases

#bucle for es un polimorfismo, ya que oermite iterar sobre cualquier objeto
# de una clase iterable: listas, cadenas de caracteres, range, tupla, dict

# def listar_elementos(elementos):
#     for i in elementos:
#         print(i)
#
# print('for con lista')
# listar_elementos([1,2,3,4]) #pasando una lista
# print('\n\nfor con tupla')
# listar_elementos((4,5,6))#pasando una tupla
# print('\n\nfor con cadena de caracteres')
# listar_elementos('Hola mundo')#pasando una cadena de caracteres

#otro ejemplo de polimorfismo en las funciones, ya que en cada ejecucion toman
# objetos de tipos diferente

# def sumar(a,b):
#     print(f'tipo de a :{type(a)} ; tipo de b: {type(b)}')
#     print(a+b)
#
# sumar(1,3) #enteros
# sumar(2.4,9.3) #float
# sumar('hola', 'mundo') #caracteres concatenación

#POLIMORFISMOS CON CLASES, el objeto o es una parametro polimorfico, ya que en
# tiempo de ejecucion va a tomar diferentes objetos de diferente clases.
#
# def saludo(o):
#     o.saludar()
#
# class A:
#
#     def saludar(self):
#         print('hola soy A')
#
# class B:
#
#     def saludar(self):
#         print('Hola soy B')
#
#
# obj1=A()
# obj2=B()
# obj3=A()
# saludo(obj1)
# saludo(obj2)
# saludo(obj3)

#LO MISMO QUE LA FUNCION ANTERIOR
def saludo(entidades):
    for entidad in entidades:
        entidad.saludar()

class A:

    def saludar(self):
        print('hola soy A')

class B:

    def saludar(self):
        print('Hola soy B')


obj1=A()
obj2=B()
obj3=A()
objetos=[obj1,obj2,obj3]
saludo(objetos)
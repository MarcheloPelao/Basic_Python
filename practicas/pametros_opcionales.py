# def f():
#     '''ejemplo funcion sin parametros'''
#     print('soy la funcion f')
#
#
# f()

#parametros formales son los que definen la función
# def f(x):
#     '''ejemplo funcion con parametros'''
#     print(f'x={x}')
# dos espacios se dejan
#
# f(1)

#podemos ocupar parametros opcionales, definiedo uno de los parametros

def f(x,y=10):#dejando y como opcional dentro de la llamada
    print(f'x={x}')
    print(f'y={y}')

f(1) # pasando sólo un parametro, ya que definimos a y anteriormente


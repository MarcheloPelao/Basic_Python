# #funciones anidadas o internas sirven para encapsular informacion.
#
# def funcion1():
#     print('soy la funcion 1')
#
#     def funcion2():
#         print('soy la funcion 2')
#
#
#     funcion2() #la funcion 1 llama a la funcion 2
#
# funcion1()#llamamos a la funcion uno y mostrara ambas funciones

def suma(x,y):
    if isinstance(x,str):
        x=int(x)
    if isinstance(y,str):
        y=int(y)


    def suma_interna(a,b):
        return a+b
    return suma_interna(x,y)

valor1=input('introduce un valor > ')#aunque es str, se corrige con la
# llamadade la funcion
valor2=input('intgroduce un valor > ')
print(suma(valor1,valor2))



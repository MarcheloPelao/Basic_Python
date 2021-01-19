# import builtins
# print(dir(builtins))

# x=10
#
# def f():
#     y=20
#
#     def f2():
#         z=30
#         print(z)
#         print(dir())#mostramos el nombre definido de manera local en la
#         # funcion f2
#     f2()
#     print(y)#muestra el valor de y
#     print(dir())
#
#
# f()
# print(x)
# print(dir())

#moficando los valores de x
# x=10
#
# def f():
#     x=20
#
#     def f2():
#         x=30
#         print(x)
#         print(dir())#mostramos el nombre definido de manera local en la
#         # funcion f2
#     f2()
#     print(x)#la funcion f busca el valor de x dentro de su ambito local que
#     # es 20
#     print(dir())
#
#
# f()
# print(x)#valor x del ambito global
# print(dir())


#MODIFICACION 2 BORRANDO EL VALOR DE X
# x=10
#
# def f():
#     def f2():
#         print(x) #busca el valor de x en el ambito local, como no lo
#         # encuentra toma el valor de x del ambito global
#         print(dir())#mostramos el nombre definido de manera local en la
#         # funcion f2
#     f2()
#     print(x)#la funcion f busca el valor de x dentro de su ambito local que
#     # como no lo encutra toma el valor de la variable global que es 10
#     print(dir())
#
#
# f()
# print(x)#valor x del ambito global
# print(dir())

#COMO MOFICAR DENTRO DE UNA FUNCION EL VALOR DEFINIDO EN UN AMBITO GLOBAL
x=10

def f():
    global x #con esto decimos que busque en el ambito global y reemplace
    # por x =20
    x=20
    y=1
    def f2():
        nonlocal y #con esto nos referimos a la y de la funcion f y no a
        # la y del ambito local de f2
        y=2
        print(x)
        print(y)
        print(dir())
    f2()
    print(x)
    print(y)
    print(dir())


f()
print(x)#valor x del ambito global
print(dir())
# #string
# saludo='hola mundo'
# print(saludo.upper())
# print(saludo.lower())
# print(saludo.capitalize())
# print(saludo.title())
# print(saludo[::-1])#imprimir alreves
# print('al' in saludo)
# print('a' in saludo)#encontrar una letra dentro de una variable
# print(saludo.count('a')) #contar letras
# print(saludo[0])
# print(saludo.index('o'))

# intento=1
# while intento <=3:
#     password=input('introduzca una contraseña > ')
#     if len(password)<=5 or '-' not in password:
#         intento+=1
#         print('contraseña incorrecta')
#     else:
#         print('contraseña creada')
#         break
#
# else:
#     print('numero de intentos agotados')

#CONCATENAR CADENAS DE CARACTERES CON JOINS
# con metodo + no es eficiente por eso se una join
var_1='hola'
var_2='mundo'
print(var_1+' '+var_2)
# con el metodo join es mucho más eficiente en las cadenas
#como nos pide un sólo argumento creamos una lista para que lo tome

print(' '.join([var_1,var_2]))

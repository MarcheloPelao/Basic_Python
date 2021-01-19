#Escribe un programa que solicite al usuario que introduzca una expresión
# y muestre por pantalla el resultado de resolver dicha expresión.
# debe tener espacios el ingreso

# expresion = input('Introduce una expresión (Ej: 1 + 3 - 2 + 9) > ')
# if (expresion.startswith('+ ') or expresion.startswith('- ') or
#         expresion.endswith('+') or expresion.endswith('-') or
#         expresion.endswith(' ')):
#     # Comprobamos si la expresión no comienza o no termina
#     # con un número. En ese caso, mostramos un mensaje de error.
#     print('Expresión no válida')
# else:
#     resultado = 0  # Variable que acumula el resultado
#     elementos = expresion.split()  # Lista que contiene los operandos y
#     # operadores
#     op = None  # Último operador que se leyó
#     for elem in elementos:
#         if elem == '+':
#             op = '+'
#         elif elem == '-':
#             op = '-'
#         else:
#             num = int(elem)
#             if op is None:
#                 resultado = num
#             elif op == '+':
#                 resultado += num
#             else:
#                 resultado -= num
#     print(resultado)


#Escribe un programa que dada una lista de números enteros, encuentre el
# segundo elemento mayor y lo muestre por pantalla.

# l=[2,5,30,50,20]
# ordenado = []
#
# if len(l)<2:
#     print('No se puede encontrar el segundo mayor')
# else:
#     for i in l:
#         ordenado.append(i)
#         ordenado.sort(reverse=True)
#     # ordenado=ordenado.sort()
#     print(ordenado[1])

#cuenta vocales

# vocales = ['a', 'e', 'i', 'o', 'u',
#            'á', 'é', 'í', 'ó', 'ú',
#            'A', 'E', 'I', 'O', 'U',
#            'Á', 'É', 'Í', 'Ó', 'Ú',
#            'ü', 'Ü']
# texto = input('Introduce un texto > ')
# total = 0
# for i in texto:
#   if i in vocales:
#      total += 1
# print(f'El texto contiene {total} vocales')

#Escribe un programa que solicite un número de tarjeta de crédito y solo
# muestre por pantalla los 4 últimos dígitos. El resto de números deben
# ser reemplazados por *****, tantos como caracteres se oculten.

numero = input('Introduce un número de tarjeta > ')
# Quitamos espacios si los hay
numero = numero.replace(' ', '')
oculto = numero[-4:].rjust(len(numero),'*')
print(oculto)
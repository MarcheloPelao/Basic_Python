# import excepciones
#
# for _ in range(3):
#     try:
#         num=input('Introduce un número > ')
#         excepciones.divide(num)
#     except ValueError:
#         print('debes introducir un número distinto de cero') #se trata la
#         # excepcion que viene del modulo excepciones
#
#
# print('Fin del programa')
from exception import FueraDeRangoError

for _ in range(3):
    try:
        num = int(input('Introduce un número > '))
        if num <0 or num > 100:
            raise FueraDeRangoError(num,'el número se pasa de rango')
    except ValueError:
        print('el valor introducido no es un numero')
    except FueraDeRangoError as fdre:
        print(fdre)#se llama al metdo str por eso lo redefinidos en execption
        print(f'Número {fdre.valor}')
        print(f'Mensaje {fdre.mensaje}')


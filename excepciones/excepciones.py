#manejo de excepciones con try y except, manera correcta es manejar cada una
# de ña excepcines que se pueden producir en el programa
#podemos manejar nuestras propias excepciones con la sentencia raise
#si no se trata la excepcion el programa finaliza
def divide(num):
    try:
        num=int(num)
        resultado=100/num
        print(resultado)
    except ValueError:
        print('el valor introducido no es un número')
        raise #se relanza la excepcion hacia el modulo principal
    except ZeroDivisionError:
        print('No se puede dividir 100 entrre cero')
    else:
        print('Todo OK')




#UNA FUNCION RECURSIVA SE INVOCA A SI MISMA, CADA VEZ QUE SE INVOCA A SI MIMA
#LO QUE SE MODIFICA SON LOS ARGUMENTOS CON LO QUE SE REALIZA LA NUEVA
#LLAMADA, FINALIZA CUANDO UNO DE LOS PARAMETROS CUMPLEN UNA DETERMINADA
#CONDICION

def factorial(n):
    print(f'n={n}')#para ver cuantas veces se invoca
    if n==1:#con esta condicion la recursividad termina
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(4))

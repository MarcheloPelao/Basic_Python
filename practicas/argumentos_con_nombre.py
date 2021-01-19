def f(x,y,z=3):
    print(f'x={x} y={y} z={z}')

f(1,8,5)
f(1,y=8,z=5)
f(1,2)#z vale 3 ya lo asignamos en la funcion como argumento opcional
# argumentos con nombre y posicional que es el 1 que se asigna al
#primer parametro de la funcion que es x
#Reglas:
#1 los argumentos con nombres siempre deben aparecer despues de los posicionales
#2 solo se puede especificar un argumento una vez
#3 los nombres deben ser iguales a los argumentos de la funcion





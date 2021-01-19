numeros=[1,2,3,4,5]
print(numeros)
#par eliminar elementos segun posición [3]
del numeros[3]
print(numeros)
numeros=[1,2,3,4,5,6,7,8,9,10]
del numeros[1:3]
print(numeros)
#del para eliminar todos los elementos de la lista
del numeros[:]
print(numeros)
#del numeros[:] es equivalente a numeros.clear()

#si se aplica del sobre un nombre borra la referencia sobre el objeto ,
#por lo ya no queda definido
del numeros
print(numeros)
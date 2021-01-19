# numeros={1,3,8,4,'a',1}
# print(numeros)
# #creando conjunto con SET
# s='aprendiendo python'
# caracteres=set(s)
# print(caracteres)
# print(len(s))
# print(len(caracteres))
# #podemos saber si un elemnto pertenece al conjunto
# print('a' in caracteres)
# caracteres.add('w')
# print(caracteres)
# print('w' in caracteres)
# #ELIMINAR ELEMENTOS
#
# print(caracteres.discard('x')) #aparecera none porque no existe
# print(caracteres.discard('w'))
# print('w' in caracteres)
# caracteres.remove('a')

# TIPO FROZENSET ES TIPO INMUTABLE no se puede modificar

# s=frozenset([1,2,1,2,5,9])
# print(s)

#OPERACIONES DE LA LOGICA DE CONJUNTOS
a={1,2,7,8,4}
b={8,0,9,1}
#union de conjuntos
# c=a|b #a union b
# print(c)
# c=a.union(b) # esto es lo mismo, la diferencia que con esta operacion podemo
#pasar un iterable y con los operadores | & no acepta iterables solo
#conjuntos
#ejemlo
# c=a.union([4,9,1])
# print(c)
#INTERSECCION
c=a&b
print(c)
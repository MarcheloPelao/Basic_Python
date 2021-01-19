# r=range(5)
# print(r)
# print(list(r))
#PROGRAMA PARA CALCULAR LA TABLA DEL 5

# tabla=5
# for i in range(1,11):
#     print(f'{tabla}*{i} = {tabla*i}')

#truco _ con esto ignoramos el elemento de la secuencia, se lo salta
# for _ in range(3):
#     n=int(input('introduce un numero: > '))
#     print(f'{n}*3={n*3}')

#cuando no utilizar el tipo range
numeros=[1,3,-5,8,0]
for i in range(len(numeros)):
    print(numeros[i])
#esta forma no es pythonica, simplemente se puede hacer lo mimo de esta
#manera
for i in numeros:
    print(i, end=' ')
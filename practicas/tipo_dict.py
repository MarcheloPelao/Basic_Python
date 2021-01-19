#ARRAY ASOCIATIVOS, tipo mutable y ordenado.

# config={'tipo':'par','num_elementos':3,'solo_positivos':True}
# config_2=dict(tipo='par',num_elementos=3,solo_positivos=True)
# print(config)
# print(config_2)
#
# print(config==config_2) #ambos diccionarios continen las misma claves-valor

#el siguiente programa pide ingresar 3 nuemros de acuerdo con el valor
#que aparece en el diccionario, y que sean par y positivos
# config={'tipo':'par','num_elementos':3,'solo_positivos':True}
# config['tipo']='impar'
# config['print_error']=True

# for _ in range(config['num_elementos']):
#     n= int(input('introduzca un numero > '))
#     if config['tipo']=='par':
#         if n%2!=0:
#             print('el numero no es valido')
#     else:
#         if n%2==0: #por si cambiamos a impar
#             print('el numero no es valido')
#     if config['solo_positivos']:
#         if n<0:
#             print('el numero no es valido')

# print(config)

#ELIMINAR ELEMENTOS DE UN DICCIONARIO

# del config['print_error']
#
# print(config)
#
# v=config.pop('tipo')
# print(v)
# print(config)

#COMPROBAR SI UNA CLAVE EXISTE EN UN DICCIONARIO

# print('num_elementos' in config)

#RECORRER LOS ELEMENTOS DE UN DICCIONARIO
# PODEMOS RECORRER SOLAMENTE LAS CLAVES
#SÓLO LOS VALORES
# Y RECORRER CLAVE-VALOR

config={'tipo':'par','num_elementos':3,'solo_positivos':True}
#mostrar las claves
for i in config:
    print(i)

for i in config.keys():# hace lo mismo que el codigo aterior
    print(i)
#mostrar sólo los valores
for i in config.values():
    print(i)
#mostrar clave valor: devuelve una tupla
for k,v in config.items():
    print(f'clave={k} ; valor={v}')
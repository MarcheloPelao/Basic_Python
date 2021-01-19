#una funcion que recibe una cadena de caracteres y devuelve las consonantes
#cuando se crea una funcion se debe dejar dos espacios para llamarla y luego
# al final se deja uno despues del fichero completo
# def elimina_caracteres(texto):
#     texto_sin_vocales=[]
#     for c in texto:
#         if c not in 'aeiouáéíóú':
#             texto_sin_vocales.append(c)
#     return ''.join(texto_sin_vocales)
#
#
# t=elimina_caracteres('hola mundo')
# print(t)
# t=elimina_caracteres('guía para ser pythonista')
# print(t)

#funcion que comprueba si el primer parametro es mayor que el segundo
# parametro

# def es_mayor(a,b):
#     return a > b #responderá true or false
#
#
# print(es_mayor(1,5))
# print(es_mayor(5,1))

#que ocurre cuando modificamos los parametros dentro de una función
def modifica_parametros(x,lista):
    print(f'x={x} ; lista={lista}')
    x=10
    lista=[] #creando un nuevo objeto lista
    lista.append(1)
    print(f'x={x} ; lista={lista}')

var1=3
var2=[1,2]
#como se creo el objeto lista dentro de la funcion cuando imprimimos el valor
#de lista var2 no se modifica, pero si no creamos el objeto en la funcion
#esta si se modifica ya que es un objeto mutable.
modifica_parametros(var1,var2)
print(var1)
print(var2)


def modifica_parametros(x,lista):
    print(f'x={x} ; lista={lista}')
    x=10
    lista.append(1) #ahora se va a doficar la var2 agregando el 1
    print(f'x={x} ; lista={lista}')

var1=3
var2=[1,2]
modifica_parametros(var1,var2)
print(var1)
print(var2)


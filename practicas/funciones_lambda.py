#FUNCIONES ANONIMAS, NO SE ESPECIFICAN NOMBRES, SE ESPECIFICA UNA SOLA
#EXPRESION, ES UN OBJETO Y PUEDE SER DEFINIDO CON UN NOMBRE

suma=lambda x,y:x+y
print(suma(2,3))

#son utiles cuando se pasan como argumento de una funcion

def realiza_operacion(operacion,valores):
    resultados=[]
    for elemento in valores:
        resultados.append(operacion(elemento))#aplicamos la operacion a cada
        #elemento
    return resultados


numeros=[1,2,3,4]
print(realiza_operacion(lambda x:x**2,numeros))#buscamos el cuadrado de las
#lista de numeros con la funcion lambda como argumento
print(realiza_operacion(lambda x:x/2,numeros))#dividir el valor de x entre 2
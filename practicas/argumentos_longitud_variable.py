# en python una funcion no se puede asinar varias veces
# def f(x):
#     print(f'x={x}')
#
#
# def f(x,y):
#     print(f'x={x} y={y}')
#
# f(1)
# f(1,2)
#APARECE UN ERROR YA QUE LA FUNCION F SE PISA

#ARGUENTOS INDETERMINADOS
#kwargs siempre debe estar como ultimo argumento
def f(a,*args,b,**kwargs):#a y b son parametros formales
    print(f'a={a} b={b} args={args} kwargs={kwargs}')
    for a in args:
        print(a)
    for k,v in kwargs.items():
        print(f'key={k} value={v}')

#f(1,2,3,4,b=5)
#f(1,b=5)
#f(1,'hola',b=5)
f(1,2,3,5,b=5,casa=1,auto=2,z=3)
f(1,2,3,5,casa=1,auto=2,z=3,b=5) #no importa la posicion cuando uno le
#indica el nombre del arguemnto

#como a y b son arguementos formales si o si deben estar
# presentes en la llamada a la funcion, para args devuelve una tupla
#arg y kwargs son parametros opcionales.

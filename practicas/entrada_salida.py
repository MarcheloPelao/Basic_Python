# nombre=input('introduce tu nombre: ')
# print('hola ' + nombre)
# lado=input('introduce el lado del cuadrado: ')
# area= float(lado)**2
# print('el area de un cuadrado de lado '+str(lado)+' es '+str(area))
# #esto se puede optimizar con el metodo format o la funcion format
# #funcion print

# a=1
# b=2
# print('a=',a)#con sep='' le quitamos la separacion
# print('a=',a,sep='',end='')
# print(' b=',b,sep='')
# print('fin')

#concatenacion

# a=1
# b=2
# print('a='+str(a)+' b='+str(b))

#metodo format
# a=5
# b=7
# plantilla_vars='variable a={} y variable b={}'
# print(plantilla_vars.format(a,b))
# # variables segun indices
# print('a={0},b={1},a={0}'.format(a,b))
#tercera forma del metodo
#
# v1=2
# v2=9
# print('a={v2}, b={v1}, a={v2}'.format(v1=v1,v2=v2))
# print('a={v2}, b={v1}, a={v2}'.format(v1=v1,v2=v2))#cambiando el orden de los
# #argumentos la salida es la misma
#
# #F STRINGS PYTHON 3.6 EN ADELANTE
# plantilla=f'a={v1},b={v2},a={v1+v2}'
# print(plantilla)

#DIRECTIVAS DE FORMATOS

# a=4
# print(a)#decimal
# #ahora mostraremos el 4 en binario con f-strings, para aplicar las
# #directivas de formato debemos hacerlo con ':'
#
# print(f'{a:b}')#binario
# print('{:b}'.format(a)) #binario con metodo format
# print(f'{a:X}')#hexadecimal

a=1234.3489390382
print(f'{a:E}')#mostrar numero en notacion cientifica
print(f'{a:.2f}')#mostrar solo dos decimales

#ALINEACION Y ANCHO MINIMO
num1=0.8
num2=100320
print(f'{num1:*>10}')
print(f'{num2:>10}')
print(f'{num2:*^10}')
print(f'{num2:^10}')
print(f'{num1:.2f}')







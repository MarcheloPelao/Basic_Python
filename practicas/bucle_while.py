#mostrar los numeros del 1 al 10
# n=0
# while n<=10:
#     print(n, end=' ')
#     n+=1

# print('***Escoge una opcion***')
# print('opcion 1=suma')
# print('opcion 2= resta')
# print('opcion 3= multiplicacion')
# print('opcion -1= salir del programa')
# var1=5
# var2=3
# opcion=0
# while opcion !=-1:
#     opcion=int(input('introduzca una opcion ---> '))
#     if opcion==1:
#         print(f'{var1}+{var2} = {var1+var2}')
#     elif opcion==2:
#         print(f'{var1}-{var2} = {var1 - var2}')
#     elif opcion==3:
#         print(f'{var1}*{var2} = {var1 * var2}')
#     elif opcion==-1:
#         pass
#     else:
#         print('opcion incorrecta, escoge otra opcion')
# print('fin del programa')

# MEJORANDO EL CODIGO ANTERIOR CON TRUE y BREAK

# while True:
#     opcion=int(input('introduzca una opcion ---> '))
#     if opcion==1:
#         print(f'{var1}+{var2} = {var1+var2}')
#     elif opcion==2:
#         print(f'{var1}-{var2} = {var1 - var2}')
#     elif opcion==3:
#         print(f'{var1}*{var2} = {var1 * var2}')
#     elif opcion==-1:
#         break
#     else:
#         print('opcion incorrecta, escoge otra opcion')
# print('fin del programa')

#USO DE CONTINUE DENTRO DE WHILE
# suma=0
# while True:
#      num=int(input('introduce un numero ---> '))
#      if num==0:
#          break
#      else:
#          if num%2 !=0:
#              continue
#          else:
#              suma +=num
# print(f'la suma total es {suma}')

# INTENTOS CONTRASEÑA

intento=1
while intento <=3:
    password=input('introduce contraseña > ')
    if password=='1234':
        print('OK, acceso permitido')
        break
    else:
        print(f'contraseña {password} incorrecta, intentalo denuevo')
        intento+=1
else:
    print('el usuarioa no está logueado')


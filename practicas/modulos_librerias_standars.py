#ORDEN DE IMPORTACION DE MODULOS
#1 MODULOS LIBRERIA STANDAR
import random
import datetime
import math

#2 acá se debe importar los modulos de terceros si es que las tenemos

#3 desde acá los modulos personales

# #generar 100 numeros aleatorios entre 0 y 100
# for _ in range(101):
#     print(random.randint(0,100))

fecha_actual=datetime.datetime.now()
print(fecha_actual)

#creacion de fecha
fecha=datetime.datetime(2021,1,7)
print(fecha)
#sumar dias a fecha
fecha=fecha + datetime.timedelta(days=10)
print(fecha)

print(math.pi)
#REDONDEA AL NUMERO MÁS PEQUEÑO
print(math.floor(101.1))
print(math.floor(101.9))
#REDONDEA hacia arriba
print(math.ceil(101.1))
print(math.ceil(101.9))
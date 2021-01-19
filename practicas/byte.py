#tabla ascii

# b= b'f' #caracter
# print(b)
# b2=b'\x66' #hexadecimal se antepone \x
# print(b2)
#
# b3=bytes([102]) #numero entero
# print(b3)

# n=102
# print(n.to_bytes(1,byteorder='big'))
#  #se le pasan dos argumentos longitud de bytes, como es de
# # 0 a 255 le podemos poner 1 y como segundo argumento byorder indica como
# #se interpreta la secuencia de bytes
# print(n.to_bytes(3,byteorder='big'))
# b=n.to_bytes(3,byteorder='big')
# print(b)
# print(b.decode('utf-8')) #decodificar los bytes para que sea caracter
#
# #transformar bytes a enteros
# print(int.from_bytes(b,byteorder='big'))

n=26214
b=n.to_bytes(2,byteorder='big')
print(b) #secuencia de bites caracteres ff

print(list(b)) #pasando a enteros ff

#creando la palbra murcielago como bytes
b=bytes('murciélago','utf-8')
print(b) #secuencia de bytes que representa la palabra murcielago
#pasando la secuencia a numeros enteros
l=list(b)
print(l)
#creando palabra con una lista de bytes
palabra_oculta=[109, 117, 114, 99, 105, 195, 169, 108, 97, 103, 111]

b=bytes(palabra_oculta)
print(b)
#decoficiando la palabra oculta a texto
palabra=b.decode('utf-8')
print(palabra)

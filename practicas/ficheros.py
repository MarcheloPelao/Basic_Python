#EJEMPLO FICHERO DE TEXTO
# f=open('ejemplo.txt','w')
# try:
#     f.write('primera linea\n')
#     f.write('\n')
#     f.write('tercera linea\n')
#     f.write('cuarta linea')
#     f.write('\n')
#     f.write('sexta linea')
# finally:
#     f.close()
#esta manera es mas pythonista de abrir y escribir un fichero con with,
# asi no se necesita agregar finally para que cierre el fichero, ya que con
# with que es un manejador de contexto lo cierra y maneja excepciones

# with open('ejemplo.txt','w') as f:
#     f.write('primera linea\n')
#     f.write('\n')
#     f.write('tercera linea\n')
#     f.write('cuarta linea')
#     f.write('\n')
#     f.write('sexta linea')

#leer un fichero por caracteres

# with open('ejemplo.txt','r') as f:
#     contenido=f.read(3)#los tres primeros caracteres
#     print(contenido)
#     contenido = f.read(2)
#     print(contenido)

#leer un fichero por linea completo
# with open('ejemplo.txt','r') as f:
#     for linea in f:
#         print(linea.rstrip())#elimina los caracteres en blanco al final de la
#         # cadena de caracteres

#leer todas las lineas
# with open('ejemplo.txt','r') as f:
#     lineas=f.readlines()
#     for l in lineas:
#         print(l.rstrip())

#EJEMPLO DE FICHERO BINARIO (codigo asci)
#creando fichero binario
# with open('binario','wb') as f:
#     f.write(b'\x65\x66\x67')
#leyendo el fichero
# with open ('binario','rb') as f:
#     print(f.read())

#POSICION DE LOS DATOS EN EL FICHERO

#con Tell() y seek()

f=open('ejemplo.txt','r+') #r+ indica lectura y escritura
print(f.read(2))

print(f.tell()) #tell nos dice que se quedo en la posicion 2 y que a partir
# de allí volvera a leer el fichero, por lo tanto si llamamos denuevo a read
# comenzará desde la posicion 2
print(f.read(3))
print(f.tell()) #ahora queda en la posicion 5
f.write('hola')#escriendo al final del fichero
print(f.tell()) #ahora quedo en la posicion al final del fichero
print(f.read())# si queremos leer ahora no mostrará nada ya que la posicion
# esta al final del fichero
#solucionamos esto con Seek() ya que nos posiciona donde queramos
print(f.seek(0)) #nos posicionamos al principio
print(f.read())#y volvemos a leer todo el contenido
print(f.seek(0,2)) #con esto vamos al final del fichero
f.write('mundo')
f.seek(0)
print(f.read())
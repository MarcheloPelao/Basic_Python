# texto='''
# Las cadenas o strings son un tipo de datos compuestos por secuencias de
# caracteres que representan texto. Estas cadenas de texto son de tipo str y se
# delimitan mediante el uso de comillas simples o dobles'''
# print(len(texto))
# text2=texto.split(' ') #quito la cuenta de los espacios en blanco
# print(len(text2))
#
# # finding specific words
# #long words: words that are most than 3 letters long
#
# for i in text2:
#     if len(i)>3:
#         print(i)
# #capitalized words
# [print(i) for i in text2 if i.istitle()]
# #words that end with s
# [print(i) for i in text2 if i.endswith('s')]
#
# #find unique words. using set()
# text3= 'To be or not to be m4rc3l0 2021'
# text4=text3.split(' ')
# print(len(text4))
# print((set(i.lower() for i in text4)))
# print(len(set(i.lower() for i in text4))) #pasamos a minusculas el texto
#
# #some word comparison functions:
#
# [print(i) for i in text4 if i.startswith('t')]
# [print(i) for i in text4 if i.endswith('s')]
# [print(i) for i in text4 if i.islower()]
# [print(i) for i in text4 if i.isupper()]
# [print(i) for i in text4 if i.isalnum()]
# [print(i) for i in text4 if i.isdigit()]
#
# #STRING OPERATIONS:
# [print(i.lower()) for i in text4]
# [print(i.upper()) for i in text4]
# [print(i.title()) for i in text4]
# [print(i.split()) for i in text4]
# [print(i.splitlines()) for i in text4]
# [print(i.rstrip()) for i in text4]
#
# # SPLIT
# text5='ouagadougou'
# text6=text5.split('ou')
# print((text6))
# print('ou'.join(text6))
# print(list(text5))

# #CLEANING TEXT
# text8='   A quick brown fox jumped over the lazy dog.  '
# print(text8.split(' '))
# text9=text8.strip()
# print(text9)
# print(text9.split(' '))
#
# #CHANGING TEXT FIND AND REPLACE
#
# print(text9.find('o'))
# print(text9.rfind('o')) #reverse
# print(text9.replace('o','O'))

# #HANDLING LARGE TEXT
#
#file=open('texto','r')
# print(file.readline()) #leer una linea
#
# #read full file
# file.seek(0) #volver al inicio del texto
# text12=file.read()
# print(text12)
# print(len(text12))
# text13=text12.splitlines()
# print(text13)
# print(len(text13))
# print(text13[0]) #first line
# file.seek(0)
# print(file.read(20)) #read character

#remove the last newline character
file2=open('texto','r')
text14=file2.readline()
print(text14)
file2.seek(0)
print(text14.rstrip())

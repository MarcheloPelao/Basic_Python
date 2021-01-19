formatos=['jpg','png','avi','mp4']
print(formatos)
formatos.append('pdf')
print(formatos)
#otra forma de construir es con list
vocales=list('aeiou')
print(vocales)
formatos_doc=['docs','xlsx','pptx']
formatos.extend(formatos_doc)
print(formatos)
#comprobacion de elementos en una lista
print('pdf' in formatos)
print('txt'in formatos)
print(f'el numero de formatos soportados es {len(formatos)}')
formatos.extend(['html','css'])
print(formatos)
formatos.remove('pptx')
print(formatos)
print(formatos[2])
print(formatos[2:6])
del formatos[0] #eliminando el primer elemento de la lista
print(formatos)
print(f'los tipos  de formatos soportados son {formatos}')
formatos[0]='gif'
print(formatos)


from SerializarObjetos import  Configuracion
#serializando
# c=Configuracion('rojo',['pdf','png']) #se crea el objeto c
#
# c.save()

#deserializar el fichero creado config.pkl
c=Configuracion.load()
print(c.color)
print(c.formatos)
# #operador logicos and or not
# #tablas de verdad and
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
#
# #tablas de verdad or:
#
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
#
# #tabla de verdad not:y
#
# print(not True)
# print(not False)
#
# #ejemplo permiso de edicion:

# es_logueado=True
# permiso_edicion=False
# print(es_logueado and permiso_edicion)

es_logueado=True
es_administrador=True
permiso_edicion=False
print(es_logueado and (permiso_edicion or es_administrador))
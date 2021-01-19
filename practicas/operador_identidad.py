a=1
b=a
c=2

print(a is b)
print(a is c)
#a y b estan haciendo referencia a un mismo objeto, tienen el mismo id
#de almacenamiento.
print(id(a))
print(id(b))
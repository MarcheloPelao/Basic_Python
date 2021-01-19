#pila es una estrautura de datos,en donde los elementos se van agregando
#y se extrae el ultimo elemento que ingreso LIFO
#LAST IN FIRST OUT
#SIMULANDO UNA PILA
# l=[]
# l.append(1)
# print(l)
# l.append(7)
# print(l)
# l.append(-3)
# print(l)
# e=l.pop()
# print(e)
# print(l)
# e=l.pop()
# print(e)
# print(l)

#COLAS usando la clase deque, va eliminado el primero que entra
#FIFO /FIRST IN FIRST OUT
from collections import deque

cola=deque()
cola.append(1)
print(cola)
cola.append(7)
print(cola)
cola.append(-3)
print(cola)
e=cola.popleft() # con este metodo se elimina el primo que entra
print(e)
print(cola)


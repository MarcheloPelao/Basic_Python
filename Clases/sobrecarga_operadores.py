# class Punto:
#     #en las clases personales debemos pasar los metodos a mano
#
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def __str__(self): #metodo string
#         return f'x: {self.x} y: {self.y}'
#
#     def __add__(self, other):#metodo suma
#         x=self.x+other.x
#         y=self.y+other.y
#         return Punto(x,y)
#
# if __name__=='__main__':
#     p1=Punto(1,2)
#     p2=Punto(5,10)
#     p3=p1+p2 #funciona ya que se implemento el metodo especial __add__
#     print(p3)

#OPERADOR DE COMPARACION

class Coche:

    def __init__(self,matricula):
        self.matricula=matricula

    def __eq__(self, other): #agregamos este metodo para que funcione el
        # operador de iagualdad, sino lo hacemos funciona igual que el
        # operador de identidad is
        return self.matricula==other.matricula

if __name__=='__main__':
    coche=Coche('1234AA')
    coche2=Coche('1234AA')
    print(coche is coche2) #operador de identidad
    print(coche==coche2) #operador de igualdad
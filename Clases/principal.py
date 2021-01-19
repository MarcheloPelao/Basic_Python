from led import Led

if __name__=='__main__':
    l_azul=Led('azul')#instaciamos con solo un parametro al objeto ya
    # que esta definido en la clase
    l_rojo=Led('rojo',2)#instanciamos agrendo todos los parametros
    print(l_azul.color)
    l_azul.color='rojo'
    print(l_azul.color)
    print(l_azul.intensidad)
    print(l_azul.encendido)
    print(l_rojo.color)
    print(l_rojo.intensidad)
    print(l_rojo.encendido)
    # l_azul.encendido=True
    l_azul.aumentar_intensidad()#llamando al metodo
    print(l_azul.intensidad)
    Led.aumentar_intensidad(l_azul) #es lo mismo que
    # l_azul.aumentar_intensidad()
    print(l_azul.intensidad)
    l_azul.aumentar_intensidad()
    print(l_azul.intensidad)
    print(Led.intensidades) #intensidades de la clase
    l_azul.intensidades=[1,2,3,4] #solo para el objeto l_azul
    print(l_azul.intensidades) #intensidades del objeto = a la de la clase
    print(l_rojo.intensidades)



# l_azul.encendido=True #creando un atributo para el objeto l_azul, es
# mejor hacerlo directo en la clase






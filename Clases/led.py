class Led():
    '''atributos de clases'''
    intensidades=[1,2,3]
    colores=['azul','verde','amarillo']
    ''' inicializamos la clases con el metodo __init__'''
    #atributos de instancias
    #encapsulacion de atributos
    def __init__(self,color,intensidad=1):#self hace referencia al objeto que
        #se crea y creamos un parametro definido por defecto
        self.__color=color #con __ dejamos el atributo como privado para que
        # no se pueda acceder a él desde fuera de la clase
        self.__intensidad=intensidad
        self.__encendido=False

    # modificando el estado de la clase por medio de metodos
    def aumentar_intensidad(self):
        if self.__encendido and self.__intensidad <3:
            self.__intensidad+= 1

    def disminuir_intensidad(self):
        if self.__encendido and self.__intensidad >1:
            self.__intensidad-= 1
    #accedemos a los atributos privados con get y set
    #DECORADOR PARA LAS ENTRADAS CON @PROPERTY
    @property #metodo get de color
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        if color in Led.colores:
            self.__color=color
        else:
            self.__color='azul'
    @property
    def intensidad(self):
        return self.__intensidad

    # def set_intencidad(self,intensidad):
    #     print('metodo no permitido')
    @property
    def encendido(self):
        return self.__encendido
    @encendido.setter
    def set_encendido(self):
        self.__encendido=encendido


    #con lo de arriba ya no necesitamos esto:
    # color=property(get_color,set_color)
    # intensidad=property(get_intensidad)
    # encendido=property(get_encendido,set_encendido)





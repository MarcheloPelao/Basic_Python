#cuando creamos excepciones personalizadas se crea un modulo con este nombre
#exception que indica que son personalizadas

class MiExcepcionBaseError(Exception):
    pass

class FueraDeRangoError(MiExcepcionBaseError):
    def __init__(self,valor,mensaje='Fuera de Rango'):
        self.valor=valor
        self.mensaje=mensaje
        super().__init__(mensaje)

    def __str__(self):#redefiniendo el metodo
        return f'{self.valor} está fuera de rango (0-100)'
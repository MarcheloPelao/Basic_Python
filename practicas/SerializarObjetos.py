import pickle

class Configuracion:

    def __init__(self,color,formatos):
        self.color=color
        self.formatos=formatos

    def save(self): #serializar el objeto
        with open ('config.pkl','wb') as f:#se crea fichero binario
            pickle.dump(self,f) #metodo dump
    @staticmethod
    def load():#deserializar o cargar el objeto sera un metodo estatico que
        # devuelve la instancia
        with open('config.pkl','rb') as f:
            return pickle.load(f) #lo unico que hace es leer el fichero binario
            # en modo lectura y devuelve el contenido deserializado
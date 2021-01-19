from utilidades import mis_funciones

print('Soy el modulo principal')

def run():
    mis_funciones.f()

if __name__=='__main__':
    run()

#comandos por terminal 3 formas de ejecurtar el scripts:
#1)python principal.py
#2)python -m principal ejecutandolo así se busca en el directorio actual, o el
#directorio path o en los directorios de instalacion por defecto de python
#3)para ejecutar el modulo main se hace:python -m utilidades
#4)python -m utilidades.mis_funciones para ejecutar el modulo mis funciones
#como scripts

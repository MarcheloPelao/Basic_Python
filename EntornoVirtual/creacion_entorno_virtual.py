#se estcribe en la terminal
#python3 -m venv env(nombre por conversión)
#activacion: tutorial-env\Scripts\activate.bat
#para desaactivar: deactivate
#instalar librerias: pip install requests

import requests

response=requests.get('https://www.google.com')
print(response)

#pip freeze #dependencias del proyecto se ejecuta en la terminal
#esta salida se vuelca a un fichero: pip freeze>requirements.txt
#para instalar los requerimientos si es que estamos en un nuevo proyecto
#pip install -r requirements.txt (en la terminal para llamar al fichero creado
# y asi se instalan las dependencias del proyecto)
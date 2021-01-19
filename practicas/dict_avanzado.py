#diccionarios anidados

#aplicacion que guarda peliculas, series y documentles y cada categoria
#tendra subcategorias y cada categoria tendra listas de peliculas, series
#docuementales

catalogo={'peliculas':{},'series':{},'documentales':{}}

catalogo['peliculas']['drama']=['pelicula 1','pelicula 2']
catalogo['peliculas']['terror']=['pelicula 3','pelicula 4']
catalogo['series']['comedia']=['serie 1','serie 2', 'serie 3']
catalogo['documentales']['belicos']=[]
catalogo['documentales']['animales']=['documental 1','documental 2']

print(catalogo)

#dando formato
for medio in catalogo:#recorremos las claves
    print('Medio: ',medio)
    for categoria,medios in catalogo[medio].items():#recorremos los valores
        print(f'categoria:{categoria} > {medios}')

#accediendo a traves de clave-valor

print(catalogo['peliculas']['terror'][0])
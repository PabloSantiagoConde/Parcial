import random

'''
Datos a tener en cuenta:

Largo: 50
Cantidad de elementos: 1 - 100

EJECUCIÓN: 
    1) Crear una lista vacía con 50 elementos
    2) Cargarle los elementos
        3) Estos mismos tienen que ser cargados de manera aleatoria
    4) Devolver la lista


'''

def lista_aleatorios():
    
    lista = [0] * 50

    for i in range(len(lista)):
        lista[i] = random.randint(1,100)

    return lista
import random
from Package_Matrix import * 
def generar_biblioteca():
    
    biblio = inicializar_matriz(6,15,"")        ##Delego la responsabilidad al paquete de matrices (Package_Matrix/matrices.py/linea 5)
    cargar_libros_aleatorios(biblio)            ##Delego la responsabilidad al paquete de matrices (Package_Matrix/matrices.py/linea 22)

    return biblio               ##Devuelvo la matriz solicitada

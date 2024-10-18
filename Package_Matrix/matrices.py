from Package_Input import *
from Package_Arrays import lista_string
from .validar_ingreso_alfanumerico import *
import random

def inicializar_matriz(filas,columnas,valor_inicial):       ##Funcion hecha en clase
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila] 

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
            print(fila) 
    print()


def cargar_libros_aleatorios(matriz):
    libro = ""
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            
            libro = lista_string(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k=2))
                                                            ##random.choices elige dentro de las opciones que están entre comillas
                                                            ##recibe dos parametros, uno son los elementos que puede seleccionar
                                                            ##y el segundo parámetro es el largo de a lista de los elementos que se generan
                                                            ## Y lista_string(lista) recibe una lista y la convierte en un string
            while not validar_ingreso_alfanumerico(libro):
                libro = lista_string(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k=2))
            
            matriz[i][j] = libro        ##Se va asginando cada elemento a la matriz
             

    return matriz
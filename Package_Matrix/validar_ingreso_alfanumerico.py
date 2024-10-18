'''
Comentario: .isalnum() me indica si el string es numerico, es alfabetico o es alfanumerico, pro esa razón desarrollo el ejercicio evaluando si contiene tanto números como letras.

EJECUCION:
    1) Me aseguro que el string tiene algun numero
    2) Me aseguro que el string tenga alguna letra
    3) Me aseguro que las dos condiciones mencionadas se cumplan al mismo tiempo 

'''

def validar_ingreso_alfanumerico(cadena):
    return tiene_numero(cadena) and tiene_string(cadena)

def tiene_numero(cadena):
    flag = False
    for i in range(len(cadena)):
        if cadena[i].isnumeric():
            flag = True
    return flag

def tiene_string(cadena):
    flag = False
    for i in range(len(cadena)):
        if cadena[i].isalpha():
            flag = True
    return flag
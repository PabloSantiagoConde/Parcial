def valor_max(lista) -> list|int:
    max = float("-inf")                                                         
    
    for i in range(len(lista)):                 
        if lista[i] > max:
            max = lista[i] 
             
    return max   

def valor_min(lista):
    min = float("inf")                                                         
    
    for i in range(len(lista)):                 
        if lista[i] < min:
            min = lista[i] 
             
    return min  

def lista_string(lista):
    string = ""
    for i in range(len(lista)):
        string += lista[i]
    return string

def print_all(lista) -> list:
    for i in range(len(lista)):
        print(lista[i])

def validar_lista(lista):
    return lista != []

def validar_lista_existente(lista):
    if validar_lista(lista):
        return True
    else:
        print("\n Error, antes de realizar esta acción tiene que iniciar la lista (elegir la opción 1) \n")
        return False


def rango(cota_inf,cota_sup,lista):
    lista_nueva = []
    for i in range(len(lista)):
        if cota_inf <= lista[i] <= cota_sup:
            lista_nueva += [lista[i]]
    if validar_lista(lista_nueva):
        return lista_nueva
    else:
        return "No hay numeros en ese rango"
    
def total_de_elementos(lista): 
    return len(lista)

'''        
3. Buscar cuántos números están en un rango dado: Solicitar al usuario que ingrese un rango (por ejemplo, entre 10 y 50) e informar cuántos números de la lista generada en el punto 1 caen dentro de dicho rango.

1) recorra la lista verificando si el numero en el que estoy parado pertenece al rango
2) los numeros que pertenecen los quiero en una nueva lista

lista = [1,2,3,4,5,6]
rango(2,5,lista)

3) RDO: [2,3,4,5]
'''
'''

Para el desarrollo de este ejercició se implementara el ordenamiento bubble sort el cual dependiendo de la orientación va a variar si la lista que devuelva como resultado será ascendete o descendente.

EJECUCIÓN:
    1)Recibo en la función una lista y un string. La lista son los elementos que quiero ordenar y el string la orientación. Se asignará por default la orientación "ASC"
    2)Dependiendo la orientación elegida oriento la lista y una vez ya finalmente organizada la retorno.

'''

def ordenar_vector(lista,orientación = "ASC"):

    if orientación == "ASC": 
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] > lista[x+1]:
                    temp = lista[x]
                    lista[x] = lista [x+1]
                    lista[x+1] = temp
        return lista
    elif orientación == "DESC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] < lista[x+1]:
                    temp = lista[x]
                    lista[x] = lista [x+1]
                    lista[x+1] = temp
        return lista

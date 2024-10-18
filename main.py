from Package_Input import *
from Package_Matrix import * 
from Package_Funciones import *
from Package_Arrays import *

def biblioteca_conde():

    lista = []
    lista_acotada = []                                                      ## Se inicializa vacía para que al pasar por "validar_lista_existente", reciba al menos 
                                                                            ## una lista vacía y de False en lugar de romper
    while True:

        opcion = get_int("\n Bienvenido a la Biblioteca. ¿Qué accion desea realizar? \n 1.Generar una lista de enteros aleatorios \n 2.Ordenar la lista creada previamente \n 3. Buscar cuántos números están en un rango dado y cuáles son \n 4. Obtener el maximo y el mínimo de la lista de elementos que pertenecen al rango \n 5. Generar una matríz aleatoria. \n 6. Salir \n Opcion elgida: ", " \n Error, opcion inexistente \n", 1,6,50)

        match opcion:
            case 1:
                lista = lista_aleatorios()
                print(f" \n La lista de numeros aleatorios es: \n \n {lista} \n \n ")
            case 2:
                if validar_lista_existente(lista):                  ##Valido si el usuario primero eligió la opción 1 antes de la ejecución de ordenamiento
                    orientacion = get_str("\n Ingrese la orientación de la lista creada. Puede elegir 'ASC' para crearla de forma ascendente o 'DESC' para crearla de forma descendente. \n Orientación elegida: ","\n Error, orientación fuera de rango \n",4).upper()
                    print(f" \n La lista de números ordenados de manera {orientacion} es: \n {ordenar_vector(lista,orientacion)}")
            case 3:
                if validar_lista_existente(lista):
                    ##Le solicito al usuario que me diga los dos bordes de la lista que quiere verificar
                    cota_inferior = get_int("\n Ingrese el valor de la cota inferior. Esta misma tiene que estar entre los numeros de 1-100. \n Opcion elegida: ","Error, el valor tiene que estar entre 1 y 100 \n",1,100,50)
                    cota_superior = get_int("\n Ingrese el valor de la cota superior. Esta misma tiene que estar entre los numeros de 1-100. \n Opcion elegida: ","Error, el valor tiene que estar entre 1 y 100 y debe ser mayor a la cota inferior. \n",cota_inferior,100,50)
                    lista_acotada = rango(cota_inferior,cota_superior,lista)
                    print(f"\n Los valores dentro del rango solicitado son {total_de_elementos(lista_acotada)} y estos mismos son los siguientes: \n {lista_acotada} \n")
            case 4:
                if validar_lista_existente(lista):
                    print(f"\n El valor máximo es {valor_max(lista_acotada)} y el valor minimo es {valor_min(lista_acotada)} \n")
            case 5:
                print()
                imprimir_matriz(generar_biblioteca())
                print()
            case 6:
                break

biblioteca_conde()
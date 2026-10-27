#
from validaciones import cargar_nombre, cargar_entero

def crear_lista(valor_inicial:any, cantidad:int)->list:
    '''
    Crea una lista repitiendo un valor la cantidad de veces indicada.

    Args:
        valor_inicial: valor que se repetira.
        cantidad: cantidad de veces que se repetira.

    Return:
        list: lista creada.
    '''
    lista = [valor_inicial] *  cantidad
    return lista


def cargar_datos(nombres:list, notas_1:list, notas_2:list)->None:
    '''
    Carga los nombres y las notas de los alumnos.

    Args:
        nombres: lista de nombres.
        notas_1: lista de notas del primer parcial.
        notas_2: lista de notas del segundo parcial.

    Return:
        None
    '''
    for i in range(len(notas_1)):
        nombres[i] = cargar_nombre('Ingrese nombre del alumno: ')
        notas_1[i] = cargar_entero(1, 10, 'Ingrese nota parcial 1: ')
        notas_2[i] = cargar_entero(1, 10, 'Ingrese nota parcial 2: ')


def calcular_promedios(lista_promedio:list, notas_1:list, notas_2:list, cant_notas:int=2)->None:
    '''
    Calcula y guarda los promedios de los alumnos en una nuevva lista.

    Args:
        lista_promedio: lista donde se guardan los promedios.
        notas_1: notas del primer parcial.
        notas_2: notas del segundo parcial.
        cant_notas: cantidad usada para recorrer la lista.

    Return:
        None
    '''
    for i in range(len(lista_promedio)):
        lista_promedio[i] = (notas_1[i] + notas_2[i]) / cant_notas


def mostrar_datos(nombres:list, notas_1:list, notas_2:list, promedios:list)->None:
    '''
    Muestra los datos de todos los alumnos.

    Args:
        nombres: lista de nombres.
        notas_1: notas del primer parcial.
        notas_2: notas del segundo parcial.
        promedios: lista de promedios.

    Return:
        None: muestra los datos por la terminal.
    '''
    for i in range(len(nombres)):
        print(f'Nombre: {nombres[i]} P1: {notas_1[i]} P2: {notas_2[i]} Promedio: {promedios[i]}')


def mostrar_datos_individual(nombres:list, notas_1:list, notas_2:list, promedios:list, posicion:int)->None:
    '''
    Muestra los datos de un alumno según su posición en las listas.

    Args:
        nombres: lista de nombres.
        notas_1: notas del primer parcial.
        notas_2: notas del segundo parcial.
        promedios: lista de promedios.
        posicion: posición del alumno especifico.

    Return:
        None: muestra los datos por la terminal
    '''

    print(f'Nombre: {nombres[posicion]} P1: {notas_1[posicion]} P2: {notas_2[posicion]} Promedio: {promedios[posicion]}')

#4
def calcular_promedio_general(promedios:list)->int|float:
    '''
    Calcula el promedio general de todos los alumnos.

    Args:
        promedios: lista de promedios.

    Return:
        int|float: promedio general.
    '''
    acumulador = 0
    for i in range(len(promedios)):
        acumulador += promedios[i]

    return acumulador / len(promedios)


def buscar_mejor_promedio(promedios:list)->int|float:
    '''
    Busca el promedio más alto de la lista.

    Args:
        promedios: lista de promedios.

    Return:
        int|float: promedio más alto.
    '''
    promedio_max = 0
    for i in range(len(promedios)):
        if promedio_max < promedios[i]:
            promedio_max = promedios[i]
        
    return promedio_max


def buscar_peor_promedio(promedios:list)->int:
    '''
    Busca el promedio más bajo de la lista.

    Args:
        promedios: lista de promedios.

    Return:
        int|float: promedio más bajo.
    '''
    promedio_min = 0
    bandera = True
    for i in range(len(promedios)):
        if bandera == True or promedio_min > promedios[i]:
            promedio_min = promedios[i]
            bandera = False

    return promedio_min


def contar_alumnos_segun_condicion(promedios:list):
    '''
    Cuenta los alumnos según su promedio: menor a 4, entre 4 y 6,
    o igual o mayor a 6.

    Args:
        promedios: lista de promedios.

    Return:
        list: cantidad de alumnos de cada grupo (segun posicion).
    '''
    lista_contador = [0] * 3
    for i in range(len(promedios)):
        if promedios[i] < 4:
            lista_contador[0] += 1
        elif promedios[i] >= 6:
            lista_contador[2] += 1
        else:
            lista_contador[1] += 1

    return lista_contador


def buscar_posicion(lista:list, objetivo:any)->int:
    '''
    Busca un elemento y devuelve su posición en la lista.

    Args:
        lista: lista donde se busca.
        objetivo: elemento que se quiere encontrar.

    Return:
        int | None: posición del elemento o None si no existe.
    '''
    posicion_elemento = None
    for i in range(len(lista)):
        if lista[i] == objetivo:
            posicion_elemento = i
            break

    return posicion_elemento


#6
def contar_vocales(cadena:str, vocales:str='aeiouAEIOU')->int:
    '''
    Cuenta las vocales que aparecen en una cadena.
    Args:
        cadena: texto donde se buscan las vocales.
        vocales: vocales que se van a contar.

    Return:
        int: cantidad de vocales encontradas.
    '''
    contador = 0
    for i in range(len(cadena)):
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                contador += 1 
                break
    
    return contador    


def invertir_str(cadena:str)->str:
    '''
    Invierte el orden de los caracteres de una cadena.

    Args:
        cadena: texto que se quiere invertir.

    Return:
        str_invertido: cadena invertida.
    '''
    str_invertido = ""
    for caracter in range(len(cadena)-1,-1,-1):
        str_invertido += cadena[caracter]

    return str_invertido

#ordenamiento
def ordenamiento_burbuja(nombres:list, notas_1:list, notas_2:list, promedios:list)->None:
    n = len(promedios)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if promedios[j] < promedios[j + 1]:

                aux = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux

                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux

                aux = notas_1[j]
                notas_1[j] = notas_1[j + 1]
                notas_1[j + 1] = aux

                aux = notas_2[j]
                notas_2[j] = notas_2[j + 1]
                notas_2[j + 1] = aux

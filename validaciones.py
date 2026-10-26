#1
def cargar_entero(minimo:int, maximo:int, mensaje:str)->int:   
    '''
    Solicita un entero y valida que esté dentro del rango indicado.

    Args:
        minimo: valor mínimo permitido.
        maximo: valor máximo permitido.
        mensaje: mensaje al solicitar el número.

    Return:
        int: número ingresado y validado.
    '''
    entero_ingresado = int(input(mensaje))
    while entero_ingresado < minimo or entero_ingresado > maximo:
        entero_ingresado = int(input(f'Error. {mensaje}')) 
    return entero_ingresado
#2


def validar_caracteres(cadena:str):
    '''
    Verifica que la cadena tenga solo letras y espacios.

    Args:
        cadena: texto que se quiere validar.

    Return:
        bool: True si los caracteres son válidos, False si no.
    '''

    caracter_valido = True    
    for i in range(len(cadena)):
        caracter = cadena[i]
        es_minuscula = caracter >= "a" and caracter <= "z"
        es_mayuscula =  caracter >= "A" and caracter <= "Z"

        if not(es_minuscula or es_mayuscula or caracter == " "):
            caracter_valido = False
        if caracter_valido == False:
            break
    return caracter_valido


#2
def validar_cadena(cadena:str)->bool:
    '''
    Verifica que la cadena tenga al menos 5 caracteres
    y que sus caracteres sean válidos.

    Args:
        cadena: texto que se quiere validar.

    Return:
        bool: True si la cadena es válida, False si no.
    '''
    retorno = True
    if len(cadena) < 5 or validar_caracteres(cadena) == False:
        retorno = False
     
    return retorno


def cargar_nombre(mensaje:str):
    '''
    Solicita un nombre y valida que sea correcto.

    Args:
        mensaje: mensaje que se muestra al solicitar el nombre.

    Return:
        str: nombre ingresado y validado.
    '''
    nombre = input(mensaje)
    while validar_cadena(nombre) == False:
        nombre = input(f'Error. {mensaje}')
    
    return nombre


################################################################################


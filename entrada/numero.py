"""
Módulo que agrupa todas las funcionalidades
que permiten pedir entrada de números
"""

#----------------------------#1# IMPORTACIONES
import sys

#----------------------------#2# DECLARAR VARIABLES


#----------------------------#3# DEFINIR FUNCIONES
 
def pedir_entrada_numero(invitacion):
    """
    Esta funcion verifica que se ha introducido un número entero
    -ARGUMENTOS----------
    invitacion: str
        mensaje que se muestra al usuario para pedir la entrada (input)
    -OUTPUT---------
    entrada: int
        número entero introducido por el usuario
    """
    while True:
        entrada = input(invitacion)
        try: #intentamos convvertirlo a entero
            entrada = int(entrada)
        except: #si no se puede, damos un mensaje de error
            print("Solo los caracteres [0-9] están autorizados.", file=sys.stderr)
            #continue

        #si pasa la barrera de excepciones, es porque se puede transformar a entero
        else: #Tenemos lo que queremos, salimos del bucle saliendo de la función
            return entrada


def pedir_entrada_numero_delimitado(invitacion, min, max):
    """
    Esta función utiliza la anterior 
    y agrega una condición sobre los limites entre los que debe estar el número
    -ARGUMENTOS----------
    invitacion: str
        mensaje que se muestra al usuario para pedir la entrada (input)
    min: int
        límite inferior del rango
    max: int
        límite superior del rango
    -OUTPUT---------
    entrada: int
        número entero y dentro del rango introducido por el usuario
    """
    invitacion = "{} entre {} y {} (incluidos): ".format(invitacion, min, max)
    entrada = pedir_entrada_numero(invitacion)

    #bucle finito para salvar el error de introducir un numero fuera de los limites
    while entrada < min or entrada > max: #COND. SALIDA: min < entrada < max
        print("El número debe estar entre {} y {}.".format(min, max), file=sys.stderr) #contabilizamos el error
        entrada = pedir_entrada_numero(invitacion)
    
    return entrada

def decidir_limites():
    '''
    Esta funcion permite al usuario definir los limites del juego
    -OUTPUT---------
    (min, max): tup
        min: int
            limite inferior
        max: int
            limite superior
    '''
    while True:
        minimo = pedir_entrada_numero("Selecciona el limite inferior: ")
        maximo = pedir_entrada_numero("Selecciona el limite superior: ")
        if maximo > minimo:
            return minimo, maximo


def pedir_entrada_del_numero_incognita(min, max):
    '''
    Esta función pide al usuario que introduzca el número que va a tener que intentar adivinar
    este numero debe ser un entero dentro del rango dado
    -ARGUMENTOS----------
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
        número entero y dentro del rango introducido por el usuario
    '''
    return pedir_entrada_numero_delimitado("Introduce el número a adivinar",min, max)


def pedir_nivel_juego():
    #pedimos al usuario el nivel de dificultad que desea
    invitacion = "Selecciona el nivel de dificultad: \n1. Fácil\n2. Intermedio\n3. Avanzado\n4. Experto\n"
    entrada = pedir_entrada_numero(invitacion) #nos aseguramos de que es un numero entero
    
    #bucle para asegurarnos de que la entrada es un numero entre 1 y 4
    while entrada < 1 or entrada > 4:
        print("Debe ser un número entre 1 y 4.", file=sys.stderr)
        entrada = pedir_entrada_numero(invitacion)
    
    return entrada

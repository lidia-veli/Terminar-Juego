#----------------------------#1# IMPORTACIONES
from entrada.booleano import (
    pedir_entrada_si_o_no,
)

from entrada.numero import (
    pedir_entrada_numero_delimitado,
    decidir_limites,
    pedir_entrada_del_numero_incognita,
)

#----------------------------#2# DECLARACION VARIABLES
#c = 0 #contador de numero intentos

#----------------------------#3# DEFINICION FUNCIONES

#REALIZAR UN INTENTO
def jugar_una_vez(numero, min, max):
    '''
    Esta funcion modeliza jugar al juego: intentar adivinar un número en un rango
    -ARGUMENTOS----------
    numero: int
        numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    (victoria, min, max ): tup
        victoria: bool
            ganar (True) o perder (False)
        min: int
            limite inferior
        max: int
            limite superior
    '''
    #pedir entero dentro del rango
    intento = pedir_entrada_numero_delimitado("Intenta encontrar el número", min, max)
    #c+=1 #contabilizamos el intento
    if intento < numero:
        print("Demasiado pequeño")
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        victoria = False
    else:
        print("¡Has ganado!")
        victoria = True
    
    return victoria, min, max #devolvemos True si ha ganado, False si no

def jugar_una_vez_con_ayuda(numero, min, max):
    '''
    Esta funcion modeliza jugar al juego: intentar adivinar un número en un rango
    pero ayuda al usuario, actualizando el rango según el resultado de la jugada anterior
    -ARGUMENTOS----------
    numero: int
        Numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    (victoria, min, max ): tup
        victoria: bool
            bool de si ha ganado (True) o no (False)
        min: int
            limite inferior actualizado tras el intento
        max: int
            limite superior actualizado tras el intento
    '''
    #pedir entero dentro del rango
    intento = pedir_entrada_numero_delimitado("Intenta encontrar el número", min, max)
    #c += 1 #contabilizamos el intento
    if intento < numero:
        print("Demasiado pequeño")
        min = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        max = intento - 1
        victoria = False
    else:
        print("¡Has ganado!")
        victoria = True
        min = max = intento
    
    return victoria, min, max #devolvemos True si ha ganado, y los límites actualizados


#JUGAR UNA PARTIDA
def jugar_una_partida(numero, min, max):
    '''
    Esta funcion modeliza lo que es jugar una partida del juego.
    Mientras no se adivine el numero, se sigue jugando
    -ARGUMENTOS----------
    numero: int
        Numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    -
    '''
    victoria=False
    while not victoria: #mientras no se gane, se repite el juego
        victoria, min, max = jugar_una_vez(numero, min, max)
    return #una vez que salimos del bucle, salimos de la funcion

def jugar_una_partida_con_ayuda(numero, min, max):
    '''
    Esta funcion modeliza lo que es jugar una partida del juego.
    Mientras no se adivine el numero, se sigue jugando
    -ARGUMENTOS----------
    numero: int
        Numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    -
    '''
    victoria=False
    while not victoria: #mientras no se gane, se repite el juego
        victoria, min, max = jugar_una_vez_con_ayuda(numero, min, max)
    return #una vez que salimos del bucle, salimos de la funcion


#CUESTION AYUDA AL USUARIO
def jugar(min,max):
    '''
    Funcion que redirige el juego en funcion de si el usuario quiere ayuda o no
    '''
    if pedir_entrada_si_o_no("¿Quieres jugar con ayuda? "): #si el usuario quiere ayuda
            numero = pedir_entrada_del_numero_incognita(min, max)
            jugar_una_partida_con_ayuda(numero, min, max)
    
    else: #si no quiere ayuda
            numero = pedir_entrada_del_numero_incognita(min, max)
            jugar_una_partida(numero, min, max)



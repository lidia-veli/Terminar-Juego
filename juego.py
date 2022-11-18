#----------------------------#1# IMPORTACIONES
from entrada.booleano import (
    pedir_entrada_si_o_no,
)

from entrada.numero import (
    pedir_entrada_numero_delimitado,
    pedir_entrada_del_numero_incognita,
    pedir_numero_intentos
)

#----------------------------#2# DECLARACION VARIABLES

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
def jugar_una_partida(numero, min, max, att):
    '''
    Esta funcion modeliza lo que es jugar una partida del juego.
    Mientras no se adivine el numero, se sigue jugando
    pero cuando se llega al limite de intentos (attepts -att), se pierde
    -ARGUMENTOS----------
    numero: int
        Numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    bool
    '''
    victoria = False
    i=0 #contador de intentos
    #BUCLE INFINITO
    while True:
        if not i < att: #si nos quedamos sin intentos
            print("Te has quedado sin intentos")
            print("Has perdido")
            return victoria

        else: #si tenemos intentos
            print("Tienes", att-i, "intentos")
            i += 1
            victoria, min, max = jugar_una_vez(numero,min,max) #volvemos a intentar adivinar el numero
            if victoria: #si hemos ganado (if True)
                return victoria

def jugar_una_partida_con_ayuda(numero, min, max, att):
    '''
    Esta funcion modeliza lo que es jugar una partida del juego.
    Mientras no se adivine el numero, se sigue jugando
    pero cuando se llega al limite de intentos (attepts -att), se pierde
    -ARGUMENTOS----------
    numero: int
        Numero a adivinar
    min: int
        limite inferior
    max: int
        limite superior
    -OUTPUT---------
    bool
    '''
    victoria = False
    i=0 #contador de intentos
    #BUCLE INFINITO
    while True:
        if not i < att: #si nos quedamos sin intentos
            print("Te has quedado sin intentos")
            print("Has perdido")
            return victoria

        else: #si tenemos intentos
            print("Tienes", att-i, "intentos")
            i += 1
            victoria, min, max = jugar_una_vez_con_ayuda(numero,min,max) #volvemos a intentar adivinar el numero
            if victoria: #si hemos ganado (if True)
                return victoria
    
  

#CUESTION AYUDA AL USUARIO
def jugar(min,max):
    '''
    Funcion que redirige el juego en funcion de si el usuario quiere ayuda o no
    '''
    #preguntamos al usuario cuantos intenos quiere
    att = pedir_numero_intentos()
    
    if pedir_entrada_si_o_no("¿Quieres jugar con ayuda? "): #si el usuario quiere ayuda
            numero = pedir_entrada_del_numero_incognita(min, max)
            jugar_una_partida_con_ayuda(numero, min, max, att)
    
    else: #si no quiere ayuda
            numero = pedir_entrada_del_numero_incognita(min, max)
            jugar_una_partida(numero, min, max, att)




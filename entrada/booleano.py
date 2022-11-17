"""
Módulo que agrupa todas las funcionalidades
que permiten pedir una entrada cuya respuesta es VERDADERO/SI o FALSO/NO
"""

#----------------------------#1# IMPORTACIONES

#----------------------------#2# DECLARAR VARIABLES
SI = ("s", "si", "y", "yes", "1")
VERDADERO = ("v", "verdadero", "t", "true", "1")


#----------------------------#3# DEFINIR FUNCIONES

def pedir_entrada_si_o_no(invitacion):
    """
    Función que pide una entrada al usuario y comprueba si es un SI
    Por defecto, toda respuesta no comprendida será NO
    -ARGS-----
    invitacion: str
        mensaje que se muestra al usuario para pedir la entrada
    -OUTPUT-----
    entrada: str in SI
        respuesta afirmativa
    False: bool
        respuesta negativa o no comprendida
    """
    try:# si la respuesta es positiva
        entrada = input(invitacion).lower() #ponemos la respuesta en en minusculas
        if entrada in SI: #si es un SI
            return entrada 
    
    except: #si no es un SI, o hay problemas, devolvemos un bool negativo
        return False



def pedir_entrada_verdadero_o_falso(invite):
    """
    Función que pide una entrada al usuario y comprueba si es VERDADERO
    Por defecto, toda respuesta no comprendida será FALSO
    -ARGS----------
    invitacion: str
        mensaje que se muestra al usuario para pedir la entrada
    -OUTPUT----------
    :str in VERDADERO
        respuesta afirmativa
    False: bool
        respuesta negativa o no comprendida
    """
    try:
        return input(invite).lower() in VERDADERO
    except:
        return False

from entrada.numero import pedir_nivel_juego
from entrada.booleano import pedir_entrada_si_o_no
from juego import jugar

def jugar_nivel_facil():
    min, max = 0, 100
    jugar(min,max)
    
def jugar_nivel_intermedio():
    min, max = 0, 1000
    jugar(min,max)

def jugar_nivel_avanzado():
    min, max = 0, 1000000
    return jugar(min,max)

def jugar_nivel_experto():
    min, max = 0, 1000000000000
    return jugar(min,max)


def jugar_con_niveles():
    nivel = pedir_nivel_juego()

    if nivel == 1:
        jugar_nivel_facil()

    elif nivel == 2:
        jugar_nivel_intermedio()

    elif nivel == 3:
        jugar_nivel_avanzado()

    elif nivel == 4:
            jugar_nivel_experto()


def jugar_a_adivinar_un_numero():
    print("Bienvenido al juego de adivinar un número")
    while True:
        jugar_con_niveles()
        if not pedir_entrada_si_o_no("¿Quieres jugar otra vez? "):
            print("¡Hasta la próxima!")
            return

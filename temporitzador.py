# Fa que tot el programa s'aturi durant un temps determinat en funció de si s'activa o no el reg

from time import sleep

def temporitzador(temps_pausa):
    try:
        sleep(temps_pausa)
    except Exception as e:
        print(f"Hi ha hagut un error amb el temporitzador >>>>> {e}") 
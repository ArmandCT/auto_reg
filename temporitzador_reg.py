# Estableix el temps de reg

from time import sleep

def temporitzador_reg(estat_reg, temps_reg):
    try:
        if estat_reg == False:
            print("Reg desactivat")
            sleep(temps_reg)   
        elif estat_reg == True:
            print("Reg activat")
            sleep(temps_reg)
            estat_reg == False
            print("Reg desactivat")
    except Exception as e:   
        print(f"Hi ha hagut un error amb el temporitzador del reg >>>>> {e}")
# Estableix el temps de reg

from time import sleep

def temporitzador_reg(estat_reg, temps_reg):
    try:
        if estat_reg == False:
            print("\n Reg desactivat \n")
            sleep(temps_reg)   
        elif estat_reg == True:
            print("\n Reg activat \n")
            sleep(temps_reg)
            estat_reg == False
            print("\n Reg desactivat \n")
    except Exception as e:   
        print(f"Hi ha hagut un error amb amb la funció temporitzador_reg >>>>> {e}")
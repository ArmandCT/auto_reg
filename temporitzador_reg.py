# Estableix el temps de reg

from time import sleep
from termcolor import colored

def temporitzador_reg(estat_reg, temps_reg):
    try:
        if estat_reg == False:
            print(colored("\n REG DESACTIVAT \n", attrs=["bold"]))
            sleep(temps_reg)   
        elif estat_reg == True:
            print(colored("\n REG ACTIVAT \n", attrs=["bold"]))
            sleep(temps_reg)
            estat_reg == False
            print(colored("\n REG DESACTIVAT \n", attrs=["bold"]))
    except Exception as e:   
        print(f"Hi ha hagut un error amb amb la funció temporitzador_reg >>>>> {e}")
# EXPLICACIÓ

from temps_status import get_status
from cultius_data import cultius_data
from cultius import cultius
from informador import informador
from activador_reg import reg
from temporitzador_reg import temporitzador_reg
from temporitzador import temporitzador
from reset import reset

# Falta crear API

poble = input("Introdueix les coordenades decimals d'on es troba el cultiu: ") # Exemple 42.197069, 2.191079
poblacio, pais, temperatura, humitat, presio, data, pluja, condicions = get_status(poble)

cult_data = cultius_data()

humitat_optima, cultiu = cultius(cult_data)

informador(poblacio, pais, temperatura, humitat, presio, data, pluja, condicions, humitat_optima, cultiu)

estat_reg, temps_reg, temps_pausa = reg(pluja, humitat, humitat_optima)

temporitzador_reg(estat_reg, temps_reg)

temporitzador(temps_pausa)

reset(poble, humitat_optima, cultiu)

# Fa un reset al programa un cop ha passat el temps definit pel temporitzador
# Es queda amb les dades de cultiu i de poble indicades al iniciar el programa

from temps_status import get_status
from cultius import cultius
from informador import informador
from activador_reg import reg
from temporitzador_reg import temporitzador_reg
from temporitzador import temporitzador

def reset(poble, humitat_optima, cultiu):
    try:
        poblacio, pais, temp, humitat, presio, data, pluja, condicions = get_status(poble)

        informador(poblacio, pais, temp, humitat, presio, data, pluja, condicions,humitat_optima,cultiu)

        estat_reg, temps_reg, temps_pausa = reg(pluja, humitat, humitat_optima)

        temporitzador_reg(estat_reg, temps_reg)

        temporitzador(temps_pausa)

        reset(poble, humitat_optima, cultiu)
    except Exception as e:
        print(f"Hi ha hagut un error amb amb la funció reset >>>>> {e}")
# En funció de la pluja i de les condicions d'humitat comparades amb l'humitat òptima del cultiu seleccionat encèn o apaga el reg
# En funció de si el reg s'encèn o no defineix el temps de reg i el d'espera per la següent consulta sobre condicions meteorològiques

def reg(pluja, humitat, humitat_optima):
    try:
        if pluja > 0 or humitat > humitat_optima:
            estat_reg = False
            temps_pausa = 3600
            temps_reg = 0
            return estat_reg, temps_reg, temps_pausa    
        elif pluja == 0 and humitat < humitat_optima:
            estat_reg = True
            temps_pausa = 3600*48
            temps_reg = 3600*2
            return estat_reg, temps_reg, temps_pausa
    except Exception as e:   
        print(f"Hi ha hagut un error amb la funció activador_reg >>>>> {e}")
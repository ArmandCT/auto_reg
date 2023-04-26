# Permet escollir sobre quin dels cultius es volen mirar les condicions per encendre el reg i en retorna l'humitat òptima

def cultius(cult_data):
    try:
        cult_data
        cult_data_key_str = ', '.join(cult_data.keys())
        while True:
            print(f"Cultius disponibles: {cult_data_key_str}")
            cultiu = input("Quin cultiu hi ha? ")
            if cultiu in cult_data:
                humitat_optima=cult_data[cultiu] 
                return humitat_optima,cultiu
            else:
                print("No tenim dades d'aquest cultiu")
    except Exception as e:
        print(f"Hi ha hagut un error intentant seleccionar el cultiu >>>>> {e}")
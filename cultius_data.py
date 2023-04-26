# Aporta la informació d'humitat òptima dels cultius disponibles i permet incorporar noves dades

def cultius_data():
    try:
        while True:
            cult_data={"tomàquet":50,"esbarginia":55,"carbassó":75,"meló":65,"xindria":65,"olivera":65,"vinya":60}
            cult_data_key_str = ', '.join(cult_data.keys())
            print(f"Cultius disponibles: {cult_data_key_str}")
            cultiu_nou_q = input("Vols afegir algun cultiu? (S/N) ")
            if cultiu_nou_q == "N":
                return cult_data
            elif cultiu_nou_q == "S":
                cultiu_nou = input("Introdueix el nom del cultiu en minúscules: ")
                humitat_nou = int(input("Introdueix l'humitat òptima (%) en número sencer: "))
                cult_data.update({cultiu_nou: humitat_nou})
                return cult_data
    except Exception as e:
        print(f"Hi ha hagut un error amb la funció cultius_data >>>>> {e}")
# Auto reg

El programa automatitza el funcionament d'un sistema de reg en funció del cultiu pel qual es seleccioni i les condicions meteorològiques del lloc on es trobi la plantació.

# Features

Consulta regular de les condicions meteorològiques de lloc de cultiu per obtenir dades de temperatura, humitat, pressió, pluja i condicions generals.
Consulta de les condicions d'humitat òptima del cultiu a partir d'una base de dades.
Possibilitat d'introduir noves dades de cultius amb l'humitat òptima corresponent.
Retorna tota aquesta informació consultada anteriorment de manera ordenada.
Comparant la pluviometria amb les dades d'humitat relativa i humitat òptima del cultiu encèn o no el reg.
Temporitza el reg quan s'encèn a dues hores.
En funció de si s'encèn o no el reg el programa queda en pausa esperant per fer la següent consulta sobre les condicions meteorològiques (48 hores en cas que s'hagi encès i 1 hora en cas que no).

# Usage

1) El programa demanarà les coordenades decimals d'on es troba el cultiu. Copiar directament les obtingudes a Google Maps (p. ex. 42.197069, 2.191079).
2) Retornarà un llistat amb els cultius dels quals es tenen dades d'humitat òptima.
3) Demanarà si es vol afegir un cultiu nou (en cas afirmatiu introduir "S", en cas negatiu introduir "N").
    3.1) Si s'ha introduit "S" demanarà que s'introdueixi el nom del cultiu. Preferiblement s'ha d'aportar únicament el nom en minúscula i singular (p. ex. "pebrot").
    3.2) Posteriorment demanarà que s'introdueixi l'humitat òptima del cultiu. S'ha d'aportar l'humitat òptima en número sencer directament (p. ex. "56").
3) Escriure el cultiu que es vol seleccionar tal com es mostra a la llista. Si s'aporta un nom que no figura retornarà la pregunta.
4) El programa ja funciona de manera autònoma fins que s'apaga.
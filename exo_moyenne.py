# %%
# faire un calcul de moyenne arithmétique
# 1. saisir d'un coup une série de nombres espacé par "," avec input
# ex. de saisie: 1,2.6,truc,...
# 2. analyser chaque valeur de la saisie pour déterminer s'il s'agît
# d'un nombre (commencer par entier, puis entier relatif)
# HINT: regarder la fonction str.isnumeric()
# 3. les valeurs numériques sont placées dans une nouvelle liste
# 4. calcul de la moyenne à partir de la nouvelle liste, 
# uniquement s'il n'y a pas eu erreur de saisie

DELIM = ','
values = input(f"entrer une série d'entiers séparés par {DELIM}: ").split(DELIM)
# values = values.split(DELIM)
nums = []
for val in values:
    if (
        val.isnumeric() 
        or val.startswith("-") and val[1:].isnumeric()
    ):
        nums.append(int(val))

if len(values) == len(nums) and values:
    moy = sum(nums) / len(nums)
    print(f"moyenne de {nums}: {round(moy, 2)}")
else:
    print(f"{set(values) - set(list(map(str,nums)))} non convertible !!!")
# %%
import sys
import re
# 1ère amélioration: break et else
# 2ème modif: une seule liste => enumerate
# 3ème modif: regex
DELIM = ','
FLOAT_PATTERN = "(-?[0-9])+(?:\.[0-9]*)?"
values = input(f"entrer une série d'entiers séparés par {DELIM}: ").split(DELIM)
# values = values.split(DELIM)
if not values: 
    print("liste vide")
    sys.exit(0)

for i, val in enumerate(values):
    if re.match(FLOAT_PATTERN, val):
        values[i] = float(val)
    else:
        print(f"{val} non convertible !!!")
        break

# exécution du bloc else ssi la boucle termine normalement
## for: itérable complètement consommé
## while: sortie par condition fausse
else:
    moy = sum(values) / len(values)
    print(f"moyenne de {values}: {round(moy, 2)}")
# %%
# encapsulation en fonction
import re
# *values: un ou n paramètres positionnels, disponibles
# dans la foncition dans le tuple values
# => les params positionnels officiels doivent être à gauche
# les paramètres nommés à droite
# **opts: arguments nommés supplémentaires qui sont dispo
# dans un dictionnaire
def calcul_moyenne(*values, float_pattern: float=FLOAT_PATTERN, precision: int=2, **opts):
    values = list(values)
    if not values: 
        print("liste vide")
        sys.exit(0)

    for i, val in enumerate(values):
        if re.match(float_pattern, val):
            values[i] = float(val)
        else:
            if "debug"in opts and opts["debug"]:
                print(f"{val} non convertible !!!")
            break
    else:
        moy = sum(values) / len(values)
        return round(moy, precision)

calcul_moyenne("1.3", "truc", "3.14", precision=3)
calcul_moyenne(*["1.3", "truc", "3.14"], precision=3, debug=True)
# %%
# %%
# effet des arguments * à l'appel
def func(p1, p2):
    return p1, p2

params = ["p1", "p2"]
func(params[0], params[1])
func(*params)
# %%

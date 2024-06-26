# %%
"""
1/ se donner trois variables de valeurs entières
et ou réelles
2/ calculer la moyenne arith.
3/ présenter le résultat avec 2 chiffres sign.  
"""

# %%
import sys
"""
1/ se donner n variables de valeurs entiers relatifs
HINT: saisir une chaine constitués de nombres séparés par ,
2/ on veut itérer sur les valeurs pour vérifier
qu'on puisse convertir en entier
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer depuisla liste
4/ présenter le résultat avec 2 chiffres sign.  
"""

values = input("insérez des valeurs séparées par ,")
if not values:
    # sortir du programme de manière normale (code 0)
    # comportement normal avec la commande python
    sys.exit(0)

values = values.split(",")
print(values)

# %%
numbers = []
for value in values:
    value = value.strip()
    if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
        numbers.append(int(value))
    else:
        # interrompre la boucle
        print(f"bad value: {value}")
        break
# le bloc du else ne s'exécute que si on a pas de break
else:
# if numbers:
    moy = sum(numbers)/len(numbers)
    f"ma moyenne: {moy.__round__(2)}"
    print(f"ma moyenne: {round(moy, 2)}")
    # print(f"ma moyenne: {sum(numbers)/len(numbers):.2f}")



# %%
# 1. trouver le bon bloc pour être générique (réutilisable)
# 2. trouver un nom cohérent, et les paramètres primaires (pos. oblig.) 
#    vs param. secondaires => valeur par défaut
# 3. faire le refactoring (valeur en dur vs variables)
# 4. print vs return
def ctrl_mean(values: str, delim: str=",", nb_sign: int=2):
    values = values.split(delim)
    numbers = []
    for value in values:
        value = value.strip()
        if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
            numbers.append(int(value))
        else:
            return None, f"bad value: {value}"
    else:
        return round(sum(numbers)/len(numbers), nb_sign), None

val, error = ctrl_mean("1;-6;34", delim=";")
if error is None:
    print(f"ma moyenne: {val}")
else:
    print(error)

# %%

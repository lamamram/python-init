# %%
# opérateur ternaire
condition = True

if condition:
    var = "value"
else:
    var = "other"
var

var = "value" if condition else "other"

# %%
# itérer sur une gamme d'entiers

# for(i=0;i<10;i++){ ... }
list(range(10))

# %%
# transformation d'une liste via une boucle
# non destructif
fruits = ["pomme", "poire", "fraise"]

frtuits_maj = []
for f in fruits:
    frtuits_maj.append(f.upper())
frtuits_maj
# %%
# %%
# transformation d'une liste via une boucle
# destructif => pas besoin de laisser fruits minuscule
fruits = ["pomme", "poire", "fraise"]

i = 0
for f in fruits:
    fruits[i] = f.upper()
    i += 1
fruits
# %%
# MIEUX
fruits = ["pomme", "poire", "fraise"]

list(enumerate(fruits))

for i, f in enumerate(fruits):
    fruits[i] = f.upper()
fruits
# %%
# SUCRE SYNTAXIQUE: liste en intension == définition

# je veux la liste des éléments majuscules pour un élément "f" dans la liste fruits
[ f.upper() for f in fruits ]

# idem si les fruits commencent par "p"
[ f.upper() for f in fruits if f[0] == "p" ]

# même avec les dico

{ f"k_{i}": f"val_{i}" for i in range(3) }
# %%
# instructions break, continue, else, pass

from decimal import Decimal
prix = [19.89, 24.50, 2.328, 3.4]
for i, p in enumerate(prix):
    # prix négatif => STOP !!
    if p <= 0: 
        print(f"prix {p} négatif !!")
        break
    d = Decimal(str(p))
    nb_decim = -1 * d.as_tuple().exponent
    # prix bien formé: RAS
    if nb_decim <= 2: continue
    # prix mal formé: on arrondit à 2 décimale
    prix[i] = round(p, 2)
# s'il n'y a pas de prix abérrant
else:
    print(f"tous les prix sont OK: {prix}")
# %%

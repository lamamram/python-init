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
import sys
# import avec espace de nom
# import utils.maths
# import direct des noms
# dans les 2 cas la totalité du module est exécuté
# et compilé dans le dossier __pycache__
# from utils.maths import calcul_moyenne as moyenne
# from utils.maths import *
## avec imports simplifiés dans __init__.py
from utils import calcul_moyenne as moyenne

calcul_moyenne = 2

if __name__ == "__main__":
    try:
        #    calcul_moyenne(*["1.3", "truc", "3.14"], precision=3, debug=True)
        m = moyenne(*["1.3", "3.14"], precision=3)
        # 3/0
    except (ValueError, TypeError) as e:
        print(e)
    # except Exception as e:
    #     print("erreur non anticipée")
    # s'exécute en cas de try sans exception levée,
    # sans crash
    else:
        print(f"résultat: {m}")
    # s'exécute même après exit, 
    # même après un crash
    finally:
        print("before leaving !!!")

# %%
# %%
# effet des arguments * à l'appel
def func(p1, p2):
    return p1, p2

params = ["p1", "p2"]
func(params[0], params[1])
func(*params)
# %%
# * force les paramètres à droite à être appelés
# de manière nommée
def connect(*, host, username, passwd, dbname, port=3306, encoding="utf-8"):
    print("connect")

connect(username="root", host="127.0.0.1", passwd="123456", dbname="project")
# %%
import utils.maths as module

print(module.__name__)
# %%

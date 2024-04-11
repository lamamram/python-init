# %%
### structure normale en python
# dossier projet: racine
# les dossiers à la racine se sont les packages
# les modules à la racine sont des programmes principaux
# à partir on utilise les imports dans le packages à partir de la racine du package

# import ...
## import essaye de trouver un fichier à la racine du dossier 
# ou un sous dossier
# ou dans la bibliothèque standard et les paquets installés par pip
# import sys, math
# le chemin python (pythonpath)
# import utils.arith
# bad
# from utils import arith

## import sans espace de nom (sécurisation par des alias en cas de conflits de nom !!)
# from utils.arith import ctrl_mean as arith_ctrl_mean
## si on a un import relatif dans __init_.py
from utils import ctrl_mean as arith_ctrl_mean

# def fct...
def ctrl_mean():
    return "prout"
# CONSTANT = ....

# convention
if __name__ == "__main__":
    values = "1;-6;34"
    # "utils.arith" : espace nom : mécanisme pour distinguer des objets de même nom
    # moy, err = utils.arith.ctrl_mean(values, delim=";")
    moy, err = arith_ctrl_mean(values, delim=";", debug=True)
    if err is None:
        print(f"ma moyenne: {moy}")
    else:
        print(err)
    
# %%
# 1. un import exécute toute la source importé
# 2. l'attribut __name__ de l'objet module
#  est "__main__" si le module est directement exécuté par python
#  ou est le chemin python du module,  si le module a été importé
import utils.arith


if __name__ == "__main__":
    
    print(utils.arith.__name__)
# %%
import main_bank

print(main_bank.__name__)
# %%

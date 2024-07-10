import imported_module

## REM: quand python doit importer un nom
# 1. il cherche le nom dans la librairie standard (modules installés avec python)
# 2. un module local de même nom (depuis du dossier racine du module appelant)
# 3. un module pip de même nom
from requests import truc
# from math import ctrl_mean
from math import sqrt
print(truc)
# print(ctrl_mean("1,-1"))
print(sqrt(2))
# pip install requests
# r  = requests.get("https://dawan.fr")

if __name__ == "__main__":
    # espace du nom du module: garantit l'unicité du nom
    print(imported_module.my_var)
    print(imported_module.my_func())

    # print(dir(imported_module))
    print(imported_module.__name__)

    print(__name__)
# ---------------------------------------
# import sans espace de nom
# from imported_module import my_func
# idem avec alias
# from imported_module import my_func as mine_my_func

# def my_func():
#     return "prout"

# print(mine_my_func())

# ---------------------------------------------
# import de tous les noms sans espace de noms
# from imported_module import *

# print(my_func())
# print(my_var)

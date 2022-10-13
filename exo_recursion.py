## fonction de recherche des dossiers __pycache__
# 1. on part du dossier dans lequel on lance la fonction
# "." soit os.getcwd()
# 2. on parcourt le dossier avec os.listdir
# 3. pour chaque élément, si l'élément est un dossier
# on boucle sur la fonction (attention à la valeur de retour)
# 4. enregister les chemins de pycache dans une liste qu'on retourne
## supprimer sequentiellement les chemins retournés

def py_find(root, name, type="d") -> list:
    found = []
    # ...
    return found

py_caches = py_find(".", "__pycache__")
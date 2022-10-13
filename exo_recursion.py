# %%
## fonction de recherche des dossiers __pycache__
# 1. on part du dossier dans lequel on lance la fonction
# "." soit os.getcwd()
# 2. on parcourt le dossier avec os.listdir
# 3. pour chaque élément, si l'élément est un dossier
# on boucle sur la fonction (attention à la valeur de retour)
# 4. enregister les chemins de pycache dans une liste qu'on retourne
## supprimer sequentiellement les chemins retournés
import os, shutil
def py_find(root, name, type="d") -> list:
    found = []
    for elem in os.listdir(root):
        # vérifier que le chemin est un dossier de nom demandé
        # penser à transformer le nom de fichier retourné
        # par listdir en chemin
        path = f"{root}/{elem}"
        if type == "d" and os.path.isdir(path):
            if elem == name:
                found.append(path)
            else:
                found += py_find(path, name, type)
    return found

py_caches = py_find(".", "__pycache__")
[ shutil.rmtree(p) for p in py_caches ]
# %%
# import os 
# os.listdir(".")
# %%

# %%
# les fonctions bas niveau : type langage C
# 1/ ouverture d'un fichier en écriture : mode "w" création / écrasement
# spécifier un chemin, et un mode
# ajouter l'encodage (par défaut utf8)
## REM: il faut toujours fermer un fichier
## surtour avec jupyter
f = open("./mon_fic.txt", mode="w", encoding="utf8")
# write retourne un nb de caractères encodés
print(f.write("je suis dans cet état."))
f.close()


# %%
# mode "r" : lecture
# les lectures sont effectuées à partir de la position
# du curseur du fichier
f = open("./mon_fic.txt", mode="r", encoding="utf8")
# ou partialement
# read() déplace le curseur ici de 10 caractères
print(f.read(10))
# lirer le contenu
print(f.read())

f.close()
# %%
# mode "a": append
# écriture à la fin du fichier
# => on dispose le curseur sur la fin 
# with [objet fichier / cnx] as objet [fichier/ cnx]:
    # ici le fichier/cnx ouvert
# en sortant du bloc le fichier / cnx est fermé

## point de vue POO: le comportement ici est __enter__ et __exit__
with open("./mon_fic.txt", mode="a", encoding="utf8") as f:
    f.write("\nnouvel état.")

# f.write("\nnouvel état.")

# %%

# ex: r+: on a un curseur en lecture au début du fichier
# et un curseur à la fin pour écriture
with open("./mon_fic.txt", mode="r+", encoding="utf8") as f:
    f.read(6)
    f.write("\nautre truc")

# %%
# WARNING sur le seek parce que il ne manipule que des octets
with open("./mon_fic.txt", mode="r", encoding="utf8") as f:
    # j'ai déplacé le curseur sur le deuxième octet du é
    # é en utf8 fait 2 octets
    f.seek(18)
    # donc on ne peut plus lire des caractères
    # f.read(4)


# %%
# supprimer le dossier python-init
import os, shutil

# chemin absolu
BASE_DIR = "C:/Users/Admin stagiaire.DESKTOP-8967908/Desktop/dawan/formations/python/init/080424"
# pwd: print working directory
print(os.getcwd())
# cd ..
os.chdir(BASE_DIR)

os.chdir("..")
tmp_dir = os.getcwd()

# appel system => je veux utiliser une command linux ou windows
# en linux rm -rf python-init
# en windows je veux
try:
    code = os.system('powershell.exe Remove-Item -Recurse python-init')
    print(code)
except Exception as e:
    print(e)

## si l'appel system ne fct => windows
## shutil.rmtree (rm -rf) sauf droits windows trop grands
try:
    shutil.rmtree("./python-init")
except Exception as e:
    print(e)

# %%
import os, shutil
# recloner le dépôt
# chemin absolu
BASE_DIR = "C:/Users/Admin stagiaire.DESKTOP-8967908/Desktop/dawan/formations/python/init/080424"

# pwd: print working directory
print(os.getcwd())
# cd ..
os.chdir(BASE_DIR)
os.chdir("..")
os.system("git clone https://github.com/lamamram/python-init.git")
# %%
import os, shutil
BASE_DIR = "C:/Users/Admin stagiaire.DESKTOP-8967908/Desktop/dawan/formations/python/init/080424"
target = "matt_cours_fichiers.py"
# séparer le nom du dossier du bout ou le nom du fichier
_, my_dir = os.path.split(BASE_DIR)

print(os.getcwd())
# cd ..
os.chdir(BASE_DIR)
os.chdir("../python-init")

# copier un fichier avec ses métadonnées
shutil.copy2(f"./{target}", f"../{my_dir}/{target[5:]}")
# %%

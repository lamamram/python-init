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

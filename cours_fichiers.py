# %%
# création d'un fichier txt
# conseil: renseigner l'encodage désiré
f = open("./test_fic.txt", "w", encoding="utf8")
# write renvoie le nb de caractères écrits (haut niveau)
print(f.write("première ligne\n"))
f.close()

f = open("./test_fic.txt", "r", encoding="utf8")
# f.read(n) lit n caractère depuis la position courante
# et déplace le curseur
print(f.read(8))
# f.read(): idem jusqu'à la fin du fichier
print(f.read())
f.close()

f = open("./test_fic.txt", "a", encoding="utf8")
print(f.write("second row\n"))
f.close()

# %%
import os
# manipulation du curseur interne du fichier
f = open("./test_fic.txt", "r", encoding="utf8")
# f = open("./test_fic.txt", "rb")
print(f.read(6))
# attention : tell compte des octets !!! (bas niveau)
print(f.tell())
# déplacement de 6 OCTETS depuis le début du fichier (bas niveau)
f.seek(6, os.SEEK_SET)
# UnicodeDecodeError: le curseur est entre deux octets d'un
# caractère utf8 non ascii
# octets = f.read()
# print(octets, type(octets))
f.close()
# %%
# str <-> bytes
# encodage utf8: caractère -> octet
octets = b"hello"
octets = bytes("hello", "utf8")
octets

# décodage utf8: octet -> caractère
octets.decode("utf8")

# %%
# bonne pratique: uitlisation du gestionnaire de contexte with
# mode r+ : lecture et écriture avec déplacement du curseur
with open("./test_fic.txt", "r+", encoding="utf8") as f:
    print(f.readlines())
    f.writelines([
        "3rd row\n",
        "4th row\n"
    ])
# sortie du bloc: fichier automatiquement refermé

# %%
with open("./test_fic.txt", "r+", encoding="utf8") as f:
    header = next(f)
    for row in f:
        print(row, end="")

# %%

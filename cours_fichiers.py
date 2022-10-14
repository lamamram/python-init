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
# os: fonctions de manipulation de chemins
import os, platform, subprocess

# diverses infos sur l'archi ou le système
os.name, os.cpu_count(), os.stat("./test_fic.txt")

# certains modules sont plus spéclialisés qu'os
platform.uname()

# appel système (déprécié)
# exécute et renvoie le code retour
os.system("dir")
# exécute et renvoie la sortie
os.popen("dir").read()

# %%
# moyen moderne: appel bloquant l'exécution
# possibilité de lancer des appels asynchrones (non bloquants)
# pour exécuter du code entre temps (réel)
# p = subprocess.Popen(["cmd", "/c", "dir"],
p = subprocess.Popen(["dir"],
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)
p.communicate()
# %%
import os, shutil
# manipulation du file system
# idempotence : même état final qq soit le nb d'exécution
path = "./temp"
file_name = "test_fic.txt"
if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(f"{path}/{file_name}"):
    shutil.copy(f"./{file_name}", f"{path}/{file_name}")

# %%
# créer un fichier csv
import csv

users = [
    ["bob", "smith", 38, "read;cook"],
    ["jane", "Doe", 24, "sport;farniente"]
]

header = ["first", "name", "age", "hobbies"]
# différence de gestion du caractère de fin sous unix et windows
# newline="" permet d'écrire de la même façon sous les deux système
# et d'éviter les lignes vides sous windows
with open("test.csv", "w", encoding="utf8", newline="") as csv_f:
    wr = csv.writer(
        csv_f, 
        delimiter=";", 
        quotechar="/",
        # stratégie d'échappement
        # none: pas d'échappement (unsafe, rapide, léger)
        # minimal : uniquement quand le délimiteur est détecté (lent, léger, safe)
        # all: tout le temps (safe, rapide, lourd)
        quoting=csv.QUOTE_MINIMAL,
    )
    wr.writerow(header)
    wr.writerows(users)

with open("test.csv", "r", encoding="utf8") as csv_f:
    rd = csv.reader(
        csv_f,
        delimiter=";",
        quotechar="/"
    )
    # print(list(rd))
    header = next(rd)
    for row in rd:
        print(row)
        print(dict(zip(header, row)))


# %%
import json

# le map applique une fonction à tous les élements
# d'un (ou plusieurs itérables) et retourne
# un itérable contenant les valeurs retournées par la fonction
users_dict = list(map(
    lambda row: dict(zip(header, row)), 
    users
))


with open("test.json", "w", encoding="utf8") as json_f:
    # écriture compacte
    # json.dump(users_dict, json_f, separators=(",", ":"))
    # écriture dépliée
    json.dump(users_dict, json_f, indent=2)
    # stringification de l'objet (str)
    # json_f.write(json.dumps(users_dict))

with open("test.json", "r", encoding="utf8") as json_f:
    obj = json.load(json_f)
    # obj = json.loads(json_f.read())
    print(type(obj))

# %%
# gestionnaire de ctx custom
from traceback import print_tb
MODE_CAPTURE = False
class Ctx:
    def __enter__(self):
        print("à l'ouverture du with")
        # le retour se place dans as
        return self
    
    def __exit__(self, x_typ, x_msg, x_trace):
        print("à la sortie du bloc with")
        print(x_typ, x_msg)
        print_tb(x_trace)
        # le bloc with fonctionne comme un try
        # on peut capturer l'exception si on retourne
        # qqch de vrai
        # possible source de confusion
        # return MODE_CAPTURE

with Ctx():
    print("dans le bloc")
    3/0

# %%

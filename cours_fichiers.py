# %%
# lecture écriture haut niveau
f = open("./test_fic.txt", "w", encoding="utf-8")
content = 'first row\nsecond_row\n'
print(f"{f.write(content)} caractères écrits")
f.close()

f = open("./test_fic.txt", "r", encoding="utf-8")
print(f.read(10))
f.close()
# %%
# idem bas niveau: wirte et read compte des octets
f = open("./test_fic.txt", "wb")
# raw_content = b'first row\nsecond_row\n'
raw_content = bytes('première ligne\nsecond_row\n', "utf-8")
print(f"{f.write(raw_content)}")
f.close()

f = open("./test_fic.txt", "rb")
print(f.read(10))
f.close()
# %%
# gestionnaire de contexte with
with open("test_fic.txt", encoding="utf-8") as f:
    # print(f.read())
    print(next(f), end="")
    for row in f:
        print(row, end="")
# le fichier est fermé à la sortie du bloc
# f.read()
# %%
header = ["id", "name", "age", "sex"]
users = [
    [1, "bébert", 27, "M"],
    [2, "jane", 33, "F"]
]
# %%
import json
# transformation format à plats en objets json
json_obj = list(map(lambda u: dict(zip(header, u)), users))
# par défaut json.dump écrit uniquement de l'ascii
# quelque soit l'encodage
with open("test_fic.json", "w", encoding="utf-8") as json_f:
    # json.dump(json_obj, json_f, separators=(",", ":"))
    json_f.write(json.dumps(json_obj, indent=2, ensure_ascii=False))

with open("test_fic.json", "r", encoding="utf-8") as json_f:
    print(json.load(json_f))
# %%
import csv

with open("test_fic.csv", "w", 
          encoding="utf-8", newline="") as csv_f:
    wr = csv.writer(
        csv_f, 
        delimiter=";"
        # quotechar='"',
        # quoting=csv.QUOTE_MINIMAL,
    )
    wr.writerow(header)
    wr.writerows(users)

with open("test_fic.csv", "r", 
          encoding="utf-8") as csv_f:
    rd = csv.reader(csv_f, delimiter=";")
    print(next(rd))
    print(list(rd))

# %%

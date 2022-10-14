"""
d'après l'url suivante
http://www.afnic.fr/wp-media/ftp/documentsOpenData/202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip
1. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

2. renommer le fichier csv en dns.csv
3. ne faire ce qui précède qui si ce n'est pas déjà fait


4. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- appelle une fonction qui
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""
# %%
import zipfile, shutil, os, csv

file_name = "202105_OPENDATA_A-NomsDeDomaineEnPointFr.csv"
zip_path = "./202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
csv_name = "dns.csv"
nb_slices = 2
slice_len = 100000

if not os.path.exists(f"./{csv_name}"):
    with zipfile.ZipFile(zip_path, "r") as zipf:
        for name in zipf.namelist():
            if name == file_name:
                zipf.extract(name)
    if os.path.exists(f"./{file_name}"):
        shutil.move(f"./{file_name}", f"./{csv_name}")


def handle_slice(f_name: str, rows: list, header: list=None, sep=";", encoding="utf8"):
    with open(
        f_name, "w", 
        encoding=encoding, newline="") as write_f:
        wr = csv.writer(
            write_f, 
            delimiter=sep
        )
        if header: wr.writerow(header)
        wr.writerows(rows)
        # vider le conteneur de lignes pour reprendre
        # uniquement 100000
        # attention: dans une fonction,
        # réaffecter un paramètre créé une variable locale
        # décorrélation avec la référence de la variable
        # globale passée en paramètre
        # rows = []
        # opération en interne (mutable)
        rows.clear()

# %%
# 1. trouver le séparateur de colonnes et l'encodage du fichier
# avec une preview
with open(f"./{csv_name}", "r", encoding="iso-8859-1") as csv_f:
    rd = csv.reader(
        csv_f,
        delimiter=";"
    )
    header = next(rd)
    rows = []
    # on doit compter par 100000 donc on a besoin des indices
    for i, row in enumerate(rd, start=1):
        rows.append(row)
        # si on a pas accumulé un multiple de 100000 lignes
        # on passe à l'itération
        if i % slice_len != 0: continue
        # si on dépasse le nb de lignes pour le nb de tranches demandé         
        if i > nb_slices * slice_len: break
        # écriture
        handle_slice(f"dns_{i}.csv", rows, header)
    else:
        handle_slice(f"dns_{i}.csv", rows, header)

# %%
# introduciton à pandas
import pandas as pd
url = "http://www.afnic.fr/wp-media/ftp/documentsOpenData/202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"

if not os.path.exists("pandas_dns.zip"):
    dns_df = pd.read_csv(
        url,
        sep=";",
        encoding="iso-8859-1",
        usecols=["Nom de domaine", "Pays BE"],
        nrows=1000000,
        # na_values=["--", "N/A"], 
        # na
    )
    dns_df.to_csv(
        "pandas_dns.zip",
        encoding="utf8",
        compression={
            "method": "zip",
            "archive_name": "pandas_dns.csv"
        },
        index=False
    )
dns_df = pd.read_csv("pandas_dns.zip")
gb = dns_df.groupby("Pays BE")
# nombre de noms deomaines par pays
count_df = gb["Nom de domaine"].count()
count_df.dropna()



# %%

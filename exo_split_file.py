# %%
"""
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
import os, csv
from zipfile import ZipFile

ZIP_PATH = "./202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
DNS_PATH = "./dns.csv"
ENCODING = "iso-8859-1"
DELIMITER = ";"
SLICE_LENGTH = 100000
NB_SLICES = 2

def create_slice(path, header, rows: list, encoding="utf-8"):
    with open(path, "w", encoding=encoding, newline="") as csv_f:
        wr = csv.writer(csv_f, delimiter=DELIMITER)
        wr.writerow(header)
        wr.writerows(rows)
        # attention : par réaffeaction,
        # rows devient une variable LOCALE
        # rows = []
        # par action interne on reste sur l'emplacement mémoire
        # de la globale
        rows.clear()

if __name__ == "__main__":
    if not os.path.exists(DNS_PATH):
        with ZipFile(ZIP_PATH, "r") as zip_f:
            zip_f.extractall()
        filename = os.path.basename(ZIP_PATH)
        base, ext = os.path.splitext(filename)
        os.rename(base + ".csv", os.path.basename(DNS_PATH))
    
    with open(DNS_PATH, "r", encoding=ENCODING) as csv_f:
        rd = csv.reader(csv_f, delimiter=DELIMITER)
        header = next(rd)
        rows = []
        for i, row in enumerate(rd, start=1):
            rows.append(row)
            if i > SLICE_LENGTH * NB_SLICES: break
            if i % SLICE_LENGTH: continue
            create_slice(f"dns_{i}.csv", header, rows, ENCODING)
            # rows = []

# %%

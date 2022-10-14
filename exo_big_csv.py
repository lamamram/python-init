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
import zipfile, shutil, os

file_name = "202105_OPENDATA_A-NomsDeDomaineEnPointFr.csv"
zip_path = "./202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
csv_name = "dns.csv"

if not os.path.exists(f"./{csv_name}"):
    with zipfile.ZipFile(zip_path, "r") as zipf:
        for name in zipf.namelist():
            if name == file_name:
                zipf.extract(name)
    if os.path.exists(f"./{file_name}"):
        shutil.move(f"./{file_name}", f"./{csv_name}")

# %%

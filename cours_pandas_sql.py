# %%
import os
import sqlite3
import pandas as pd
from time import time
import numpy as np

# pip install SQLAlchemy
# créer une connexion de bdd
from sqlalchemy import create_engine
# pour créer / modifier un schéma de db
from sqlalchemy.types import Integer, String, Text

# %%
# fabriquer un gestionnnaire de contexte

class Timer:
    def __init__(self, title):
        self.title = title

    def __enter__(self):
        self.start = time()

    def __exit__(self, x_typ, x_msg, x_trace):
        print(f"{self.title}: {round(time() - self.start, 3)} s")

# %%
# créer un client de connexion pour créer la base et les tables
try:
    with sqlite3.connect("dns.db") as conn:
        cur = conn.cursor()
        with open("domain_name_sqlite3.sql", "r", encoding="utf8") as f:
            cur.executescript(f.read())
except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
    print(e)
except ConnectionError as ce:
    print(ce)

# %%
df_conn = create_engine("sqlite:///dns.db")
pays_df = pd.read_sql("pays", df_conn, index_col="iso2")
pays_df = pd.read_sql("select * from pays", df_conn, index_col="iso2")
pays_df
# %%
## télécharger les données
# 1. se donner un dataframe avec l'url
# observer le fichier : sep=";" encoding="iso-8859-1"
# 2. écrire le df en local dans un .zip
# 3. ne faire ceci que si ce n'est pas déjà fait

# 4.-  pendre le sous df contenant uniquement les colonnes nécessaire
#   -  faire correspondre les noms de colonnes du df 
# avec les noms des champs de la table domain_name
#   - utiliser la méthode df.to_sql()

file_path = "./dns.zip"
url = "http://www.afnic.fr/wp-media/ftp/documentsOpenData/202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
encoding = "iso-8859-1"

# %%
if not os.path.exists(file_path):
    with Timer("téléchargement"):
        dns_df = pd.read_csv(url, sep=";", encoding=encoding)
    with Timer("écriture"):
        dns_df.to_csv(
            file_path,
            encoding=encoding,
            compression={
                "method": "zip",
                "archive_name": "dns.csv"
            },
            index=False
        )

# %%
with Timer("lecture SSD 1000000"):
    dns_df = pd.read_csv(
        file_path,
        encoding=encoding,
        usecols=["Nom de domaine", "Pays BE"],
        nrows=1000000
    )
dns_df.rename(columns={
    "Nom de domaine": "name",
    "Pays BE": "iso2"
}, inplace=True)

# %%
with Timer("insert 1000000 rows"):
    print(dns_df.to_sql(
        "domain_name",
        df_conn,
        # écriture en insert à la fin de la table
        # if_exists="append",
        # suppression de la table, recréation à partir d'un shchéma
        # et insertion
        if_exists="replace",
        index=False,
        # en cas de replace, on doit fournir
        # le schéma de la table pour la recréer
        dtype={
            "dns_id": Integer,
            "name": String,
            "iso2": String,
            "created_at": Text
        }
    ))

pd.read_sql("select count(1) from domain_name", df_conn)

# REM: pour effectuer des update à partir d'un dataframe
# 1/ écriture en replace sur une table temporaire copie de la vrai table
# 2/ updates entre la table tmp et la vraie table
# %%

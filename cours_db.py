# %%
# DBAPI
import sqlite3

# 1. cnx
with sqlite3.connect("./dns.db") as conn:
    # classe de réponse de type dict
    conn.row_factory = sqlite3.Row
    # acquisition d'un prompt
    cur = conn.cursor()
    # exécution
    cur.execute("SELECT SQLITE_VERSION() as version")
    # récupération
    row = cur.fetchone()
    print(dict(row))
# closed
# %%
# exécution du script .sql avec la méthode executescript
with sqlite3.connect("./dns.db") as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    with open("domain_names_sqlite3.sql", "r", encoding="utf-8") as sql_f:
        cur.executescript(sql_f.read())
    cur.execute("SELECT COUNT(1) as nb FROM pays")
    row = dict(cur.fetchone())
    print(f"{row['nb']} lignes")
# %%
import sqlite3, csv

class Sqlite3Client:
    def __init__(self, path, hydration="dict") -> None:
        self.__path = path
        self.__hydration = hydration
    
    # entrée dans le with
    def __enter__(self):
        self.__conn = sqlite3.connect(self.__path)
        # retour du "as"
        return self
    
    # sortie de with
    # les params x_ décrivent une possible exception
    def __exit__(self, x_typ, x_msg, x_trace):
        # gestion de transactation
        if x_typ:
            self.__conn.rollback()
        else:
            self.__conn.commit()
        self.__conn.close()

    def executescript(self, script_path, encoding="utf-8"):
        if self.__hydration == "dict":
            self.__conn.row_factory = sqlite3.Row
        cur = self.__conn.cursor()
        with open(script_path, "r", encoding=encoding) as sql_f:
            cur.executescript(sql_f.read())
    
    def insert(self, table_name: str, fields: tuple, values: list):
        req = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({','.join((['?'] * len(fields)))})"
        cur = self.__conn.cursor()
        cur.executemany(req, raw_values)
        return cur.rowcount
        
if __name__ == "__main__":
    # db = Sqlite3Client("./dns.db")
    # db.executescript("domain_names_sqlite3.sql")
    with open("dns_100000.csv", "r", encoding="iso-8859-1") as f:
        rd = csv.reader(f, delimiter=';')
        next(rd)
        raw_values = list(map(lambda r: r[:2] + [r[10]], list(rd)))
        # print(raw_values[:5])
    
    try:
        with Sqlite3Client("./dns.db") as db:
            db.executescript("domain_names_sqlite3.sql")
            print(db.insert("domain_name", ("name", "iso2", "created_at"), raw_values))
    except sqlite3.OperationalError as e:
        print(e)
# %%
# créer une méthode publique insert
# prends en paramètre 
# - le nom de la table
# - la liste des 3 champs de la table
# - une liste de vecteurs de données
# 3 champs (nom de domaine, pays, date de création)
# pour construire la requête
# "INSERT INTO domain_name (name, iso2, created_at) VALUES (?, ?, ?)"

def insert(self, table_name: str, fields: tuple, values: list):
    pass
# %%

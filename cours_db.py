# %%
import sqlite3
# %%
# 1. cnx
with sqlite3.connect("./dns.db") as conn:
    # hydration : résultats sous forme de dicos
    conn.row_factory = sqlite3.Row
    # 2. prompt sur la cnx
    cur = conn.cursor()
    # 3. exécution de requêtes sur le prompt
    cur.execute("SELECT SQLITE_VERSION() as version")
    # 4. fetch des données (un, plusieurs, tous)
    row = cur.fetchone()
    print(dict(row)["version"])
# %%
# créer les tables avec la méthode executescript
with sqlite3.connect("./dns.db") as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        with open("domain_names_sqlite3.sql", "r", encoding="utf-8") as sql_f:
            cur.executescript(sql_f.read())
    except sqlite3.OperationalError as e:
        print(e)
    cur.execute("SELECT count(1) as nb FROM pays")
    row = dict(cur.fetchone())
    print(row["nb"])
# %%
# class client
# 1. ajouter une méthode publique insert_each qui utilise la méthode executemany
# du modeule sqlite3
# 2. idem avec la méthode insert_once (utiliser judicieuseent str.join)
# à chaque fois on peut récupérer le paramètre cur.rowcount affected_rows
import sqlite3, csv
class SqliteClient:
    def __init__(self, db_path, hydration="dict") -> None:
        self.__db_path = db_path
        self.__hydration = hydration
    
    def __enter__(self):
        self.__conn = sqlite3.connect(self.__db_path)
        if self.__hydration == "dict":
            self.__conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, x_typ, x_msg, x_trace):
        if x_typ:
            print("rollback !!")
            self.__conn.rollback()
        else:
            self.__conn.commit()
        self.__conn.close()
    
    def insert_each(self, table: str, fields: tuple, values):
        cur = self.__conn.cursor()
        # INSERT INTO TABLE (F1, F2, F3, ..., Fp) VALUES (?, ?, ?, ..., ?)
        q = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['?'] * len(fields))})"
        # print(q)
        cur.executemany(
            q,
            values
        )
        return cur.rowcount

    def executescript(self, file_path, encoding="utf-8"):
        # ici le curseur n'a pas besoin d'être persistent
        cur = self.__conn.cursor()
        with open(file_path, "r", encoding=encoding) as sql_f:
            cur.executescript(sql_f.read())

if __name__ == "__main__":
    with open("dns_100000.csv", "r", encoding="iso-8859-1") as f:
        rd = csv.reader(f, delimiter=';')
        next(rd)
        raw_values = list(map(lambda r: r[:2], list(rd)))
        # print(raw_values[:5])

    try:
        with SqliteClient("./dns.db") as db:
            db.executescript("domain_names_sqlite3.sql")
            affected_rows = db.insert_each(
                "domain_name", 
                ("name", "iso2"), 
                raw_values
            )
            print(affected_rows)
    except sqlite3.OperationalError as e:
        print(e)
# %%

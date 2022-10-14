# %%
import sqlite3

# 1. une connexion bdd s'ouvre et se ferme:
with sqlite3.connect("dns.db") as conn:
    # bonus: modifier la classe de gestion
    # des retours d'enregistrement
    conn.row_factory = sqlite3.Row
    # 2. se doter d'un curseur
    cur = conn.cursor()
    # 3. exécuter une ou des requêtes
    cur.execute("SELECT SQLITE_VERSION() as version")
    # 4. tirer les résultats
    row = cur.fetchone()
    print(row["version"])
# 5. fermeture de la connexion: conn.close()
# %%
# 1. exécuter le script .sql grâce au module sqlite3
#   et la méthode executescript

# 2. vérifier l'import avec une requête select
# select count(1) from pays

# 3. protéger les requête par une exception
import sqlite3
with sqlite3.connect("dns.db") as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        with open("domain_names_sqlite3.sql", "r", encoding="utf8") as sql_f:
            cur.executescript(sql_f.read())
        cur.execute("select count(1) as nb from pays")
        row = cur.fetchone()
        print(row["nb"])
    except sqlite3.OperationalError as e:
        print(e)
    # print(cur.lastrowid)
# %%
# 1. insérer 100000 lignes depuis dns_100000.csv dans la base
# en 1 seule fois: 
# insert into domain_name (name, iso2) 
# values ('aaa.fr', 'FR'), ('bbb.de', 'DE'), ... x 100000
# 2. afficher cur.rowcount après pour vérifier
import csv
with open("dns_100000.csv", "r", encoding="utf8") as csv_f:
    rd = csv.reader(csv_f, delimiter=";")
    header = next(rd)
    # 1. version pro
    # values = "'), ('".join(list(map(lambda row: "', '".join(row[:2]), rd)))
    # y = f°g°h°i°j(x)
    # 2. version classique:
    values = []
    for row in rd:
        # sélection des 2 premiers champs
        sub_row = [row[0], row[1]]
        # fabriquer chaque enregistrement de l'insert
        sub_row = "', '".join(sub_row)
        values.append(sub_row)
    # relier les enregistrements de l'insert
    values = "'), ('".join(values)


req = f"insert into domain_name (name, iso2) values ('{values}')"
with sqlite3.connect("dns.db") as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(req)
        print(cur.rowcount)
    except sqlite3.OperationalError as e:
        print(e)
# %%
import csv
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
        self.__conn.close()
    
    def executescript(self, file_path, encoding="utf8"):
        cur = self.__conn.cursor()
        with open(file_path, "r", encoding=encoding) as sql_f:
            cur.executescript(sql_f.read())

    def execute_write(self, query):
        cur = self.__conn.cursor()
        cur.execute(query)
        return cur.rowcount
    
    # paramètres: table, champs, valeurs
    # mode d'insertion (1 * n ou n * m)
    def insert_all(self, table, fields, values):
        values_str = "'), ('".join(list(map(lambda row: "', '".join(row), values)))
        req = f"insert into {table} ({', '.join(fields)}) values ('{values_str}')"
        return self.execute_write(req)

with open("dns_100000.csv", "r", encoding="utf8") as csv_f:
    rd = csv.reader(csv_f, delimiter=";")
    header = next(rd)
    values = list(map(lambda row: row[:2], rd))

try:
    with SqliteClient("dns.db") as db:
        db.executescript("domain_names_sqlite3.sql")
        print(db.insert_all("domain_name", ("name", "iso2"), values))
except sqlite3.OperationalError as e:
    print(e)
        
# %%

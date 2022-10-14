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
    values = "'), ('".join(list(map(lambda row: "', '".join(row[:2]), rd)))
    # y = f°g°h°i°j(x)

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

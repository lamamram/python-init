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
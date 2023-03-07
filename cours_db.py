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

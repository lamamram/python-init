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

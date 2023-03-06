# %%
# instanciations

# litéral
dico = {
    "k": "v",
    2: "v2"
}

# depuis une liste de tuples
tuples = [("k", "v"), (2, "v2")]
dico = dict(tuples)
dico

# fonction zip
keys = ["k", 2, "ok"]
values = ("v", "v2")
dict(zip(keys, values))
# %%
# in joue sur les clés
'k' in dico
for k in dico: pass
"v" in dico.values()
for v in dico.values(): pass
('k', 'v') in dico.items()
for k, v in dico.items(): pass
# %%
if "nawak" in dico:
    dico["nawak"]

dico.get("nawak", "default")
# %%
# suppression d'une reférence à un emplacement mémoire
del dico["k"]
l = [1, 2]
del l[0]
c = 1
del c
c
# %%

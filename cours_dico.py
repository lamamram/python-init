# %%
# création dico

dico = {
    "key": "value",
    42: [1, 2, 3],
    3.14: "hello",
    (-1.666, 46.324): "NANTES"
}
dico
# %%
# accès aux valeurs par les clés
dico["key"]
dico["key"] = 2
dico["key"]
dico["new_key"] = "new_value"
del dico["new_key"]
dico
# %%
# attention aux clés inexistantes
# KeyError
key = "unknown_key"
if key in dico: print(dico[key])
else: print("default")

print(dico.get(key, "default"))
# %%
# itération sur un dico
# par défaut sur les clés
for k in dico:
    print(k)

# %%
# objet proche d'une liste
values = list(dico.values())
print(values)
for v in dico.values():
    print(v)

# %%
# itération sur les paires clé / valeurs
items = dico.items()
print(list(items))
for k, v in dico.items():
    print(k, v)
# %%
# un dico est très proche d'une liste de tuple

tuples = [("k1", "v1"), ("k2", "v2"), (3.14, 42)]
dico = dict(tuples)
dico
# %%
keys, values = ["k1", "k2", 3.14], ["v1", "v2", 42]
dict(zip(keys, values))
# %%

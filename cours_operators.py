# %%
# opérateurs arithmétiques
## saisir un nombre entre 0 et 86400
# indiquer l'heure qu'il est depuis minuit
entry = input("entrer un entier entre 0 et 86400: ")
# "conversion"
entry = int(entry)
heures = entry // 3600
minutes = (entry % 3600) // 60
sencondes = entry % 60

# %%
# formatage
# mauvais: pas de conversions implicites
print("il est" + str(heures) + "h " + str(minutes) + "mn")
# avec print
print("il est ", heures, "h", minutes, "mn")

# operateurs de formatage python2
print("il est %dh %dmn" % (heures, minutes))
# methode de formatage python3
print("il est {1}h {0:06.2f}mn".format(heures, minutes))
print("il est {h}h {mn:06.2f}mn".format(h=heures, mn=minutes))
# injecter directement des expressions python
print(f"il est {heures}h {minutes + 0.5:06.2f}mn")
# %%
# opérateurs de comparaison et logiques
entry = input("entrer un entier entre 0 et 86400: ")
# str.isnumeric
if entry.isnumeric():
    entry = int(entry)
    # if entry >=0 and entry < 86400:
    if 0 <= entry < 86400:
        heures = entry // 3600
        minutes = (entry % 3600) // 60
        sencondes = entry % 60
        print(f"il est {heures}h {minutes}mn")
    elif entry < 0:
        print(f"{entry} négatif !!!")
else:
    print(f"{entry} n'est pas un int !!!")
# %%

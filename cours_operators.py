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
# injecter directement des expressions python
print(f"il est {heures}h {minutes + 0.5:06.2f}mn")
# %%

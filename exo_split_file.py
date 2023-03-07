# %%
import os
"""
1. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

2. renommer le fichier csv en dns.csv
3. ne faire ce qui précède qui si ce n'est pas déjà fait


4. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- appelle une fonction qui
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""
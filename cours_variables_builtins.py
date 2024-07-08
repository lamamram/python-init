# %%

x = 1
# la fonction id va retourner un identifiant
# géré par l'interpréteur, 
# lui même capable de connaître l'emplacement adresse
# en RAM (en héxa)
id(x)
# %%

# nommage de variables en pthon [a-zA-z_][a-zA-Z0-9_]* : écriture en "snake_case"

ma_variable = "truc"
# ERROR 1ère_variable = ...

# pas de constante en python une convention (écriture ALL_CAPS)
PI = 3.14
PI = 3.2
# %%

# passages par référence 

x = 1
y = x
z = 1

# y = x veut dire que y référence le même emplacement (id) que x
# z = 1 après x = 1 => optimisation de la mémoire en allouant le même id que x
print(y, id(y), id(x), id(z))
# %%
# écriture "inline" uniquement dans le terminal
x = 1;y=2
# ex : python -c 'x=1;y=2;print(x,y)'

# %%

# chaines de caractère: str

single = 'hello world'
# échappement du single quote
single = 'j\'ai bien mangé'
double = "j'ai bien mangé"

# couper une longue str en une ligne, en  échappant le saut de ligne pour la lisibilité
long_sentence = "blabla blabla blabla blabla blabla blabla \
    blabla blabla blabla blabla blabla "
long_command = "cmd subcmd \
    --option1=...\
    --option2=..."
# spécifité python

# gérer le saut de ligne dans la str
paragraph = """blabla blabla blabla blabla blabla blabla 
blabla blabla blabla blabla blabla blabla blabla blabla 
blabla blabla blabla blabla blabla blabla blabla blabla 
blabla blabla blabla blabla blabla blabla blabla."""
print(paragraph)

# %%
## types composites

# list: ensemble d'objets hétérogènes et indexables modifiable

# hétérogènes
user = ["bob", "smith", 33, 175.7]
# indexable
user[1]
# modifiable
user[1] = "cavendish"
# %%
## types composites

# t-uple: ensemble d'objets hétérogènes et indexables non modifiable
# t-uplet => ensemble de t valeurs
# hétérogènes
user = ("bob", "smith", 33, 175.7)
# indexable
user[1]
# non modifiable
user[1] = "cavendish"

# %%

## types composites

# dictionnaire : dict

# enseble de paires clés / valeurs hétérogènes, 
# dont les clés sont uniques
# et de types "non modfiables"

dico = {
    "key": "value",
    3.14: 33
}
# accès aux valeurs depuis les clés
dico["key"]


# %%
# intro: opérateurs

# + - * / //(quotient) %(modulo) **(exposant)

# 1.on prend un entier entre 0 et 86400
# 2. je veux connaître l'heure
# 3. présenter le résultat joliment

saisie = input("saisissez un entier entre 0 (minuit auj.) et 86400 (minuit demain) :")
saisie
# pas de conversion implicites en python !!! (sauf int et float)
# on doit utiliser des fonctions de conversion
saisie = int(saisie)

nb_heures = saisie // 3600
nb_minutes = saisie % 3600 // 60
nb_secondes = saisie % 60

# BAD PRACTICE: conversion explicite + gérer les espaces
# print("il est " + str(nb_heures) + "h, " + str(nb_minutes))
# MIEUX: conversion implicites + ajout des espaces
print("il est", nb_heures, "h,", nb_minutes, "mn,", nb_secondes, "s", sep="|")

# %%
# TEMPLATING

# old-fashion
tpl = "il est %d h, %d mn, %ds"
print(tpl % (nb_heures, nb_minutes, nb_secondes))

# python3
tpl1 = "il est {1}h, {2}mn, {0}s"
tpl2 = "il est {hour}h, {minute}mn, {second}s"
# fonction interne de la variable de type str
# print(tpl1.format(nb_heures, nb_minutes, nb_secondes))
print(tpl2.format(
    second=nb_secondes, 
    minute=nb_minutes, 
    hour=nb_heures))
# %%
# f-string: spécificité python3.6 + SUCRE SYNTAXIQUE
print(f"il est {nb_heures}h, {nb_minutes}mn, {nb_secondes + 10}s")
# %%

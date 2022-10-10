# %%


print("hello")

# %%
x = 1
x = "bonjour"
x
# %%
# convention de nommage
# snake_case
ma_variable = "valeur"
# "constante"
# type float
PI_APPROX = 3.14

# %%
# syntaxes d'affectations
# standard : y affecté APRES x
x = 1
y = 2

# inline => python en CLI
# ex. python -c "x = 1;y = 2;print(x, y)"
x = 1;y = 2

# "UNPACKING" : affectation en ligne
# x et y sont affectés "en même temps"
x, y = 1, 2

print(x, y)
# %%
# mécanismes de mise en mémoire
# type int
x = 42
# 1. passage par référence
# y désigne de le même emplacement mém que x
y = x
print(id(x), id(y))

# 2. optimisation de la mémoire
# pour les entiers et les flottants
# si une valeur "non modifiable"
# est déjà référencée, alors python
# ajoute toute nouvelle variable sur cette valeur
# comme nouvelle référence
z = 42
id(z)
# %%
# présentation chaines de caractères
# "\" dans une chaine '' ou "" échape le saut de ligne
# type str
single = 'bonjour \
     "monde"'
double = "bonjour m'dame"

triple = """
bonjour tout le monde
blabla "" ''
"""
triple
# %%
# présentation liste, tuple, et dictionnaire
# éléments indéxés par des entiers (position)
# type list
liste = [10, "hello", triple]
# tuple = liste non modifiable
# type tuple
tup = (10, "hello", triple)
# ensemble de paires clé / valeur
# on accède aux valeurs par les clés
# type dict
dico = {"number": 10, "msg": "hello", 3.14: triple}
# %%
# attention à ne pas redéfinir le fonctions
# de la librairie standard
# print = 2
# TypeError
# print(print)
# del print
# %%
# fonction fondamentales
# print
print(x, triple, sep=",", end="-")

# input
# affectation de la valeur de retour de la fonction input
entry = input("Veuillez entrer un nb entier: ")
entry

# type d'une variable
type(entry)
# %%
# fonctions de conversions
value = "33"
# les types de données sont également
# des fonctions de conversion
int(value)
# value n'est pas modifiée => int retoure une transformation
value
# réaffectation de value avec la conversion
value = int(value)
# %%
# pas de conversion explicite int, float => str
str(3.14159)
"j'ai " + str(2) + " amours"
# %%
# libérer une variable: enlève une référence 
# sur l'emplacement mémoire
del x
# %%
# fonctions d'introspection
# documentation sur une variable
# help(str)
# affiche les attributs d"une variables
dir(value)
# %%

# %%
# pas de déclaration
# création par l'initialisation
# => première affectation

# conventtions de nommage
# snake_case
# camelCase => pas en python
# PascalCase => uniquement pour les classes
# ALL_CAPS pour les (pseudo) constantes
my_variable = "ma valeur"
PI = 3.14159

# %%
# 5 fonctions fondamentales
# affichage sortie standard
print(my_variable, 3.14, PI, sep=":", end="\n")
# saisir entrée standard
# type d'une variable ==> classe
# EN PYTHON TOUT EST OBJET
val = input("veuillez entrer une valeur: ")
print(val, type(val))

# attributs d'un objet
dir(val)
# les attributs accessibles par l'opérateur '.'
my_variable.upper()

# %%
# aide contextuelle => dispo avec l'extension 
# python dans VSCODE
help(str.upper)

# %%
# emplacement mémoire piloté par python
print(id(my_variable))
clone_var = my_variable
id(clone_var)
# chgt de valeur et de type (typage dynamique)
my_variable = 3.33
print(id(my_variable), id(clone_var))
# opérateur de comparaison des ids
print(
    id(my_variable) == id(clone_var), 
    my_variable is clone_var
)
# %%
x = 1
y = 1
x is y

# %%
# built ins
integer = 42
# single precision
_float =  3.14
_str = "voila"
boolean = True or False
nothing = None

# structures
# liste: indexable, iterable, mutable
items = [1, "ok", 1.41, False, [0]]

# tuple: indexable, iterable, immutable
_tuple = (1, 2, 5, "aaa")

# accès aux valeurs par des clés immutables
# itérable et mutable
dico = {
    "key": "value", 
    3.14: [1, 2, 3],
    ("42.143", "-1.345543"): "Paris"
}

# set: non indexable, itérable, mutable, garantie l'unicité
fruits = {"pomme", "poire", 4}
print(type(integer), type(_float), type(_str), type(boolean), type(nothing), type(items), type(_tuple), type(dico), type(fruits))

# %%
## mutabilité vs immutabilité
# mutabilité : modif "interne" => sans réaffectation de la variable
items[0] = 10
dico["key"] = "other value"
fruits.discard(4)

# immutabilité: changement uniquement par réaffectation
# int et float: pas d'opérations internes
# TypeError
# _str[0] = "V"
# _tuple[0] = 33
# %%
# attention aux affectations de mutables
items = [1, 2, "ok", 2**0.5]
clone = items
shallow_clone = items.copy()
clone.append(True)
shallow_clone.remove("ok")
# avec mutable + affectation + operation interne
# les mutables restent corrélés en mémoire
print(items is clone)
# avec copy
print(items is shallow_clone)
# les éléments internes sont a priori corrélés
print(items[1] is shallow_clone[1])
items[1] = 8
print(items[1] is shallow_clone[1])
# %%
# tuples implicites

x = 1
y = 2
# UNPACKING
x, y = 1, 2

# x = 10
# y = x + 3
x, y = 10, x + y
x, y
# %%
for a, b in [(1, 2), (3, 4)]:
    print(a, b)
# %%

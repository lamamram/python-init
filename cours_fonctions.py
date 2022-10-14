# %%
# définition et appel
# définition
from ast import keyword
from sys import ps2


def func():
    print("inside func")
    return "result"

# l'appel
# () se nomme opérateur d'appel
# les fonctions sont dites callables
# la valeur de l'instruciton retrurn
# donne sa valeur à l'appel
func()

# %%
# typage des paramètres et des valeurs de retours
# annotations: purement informatif
# docstring: triple chaine à placer
# jjuste en dessous du nom de la fonciton
def func(n: int) -> int:
    """
    fonction incroyable qui multiplie par trois un entier.
    n: int
    """
    return 3 * n

func(3)
func("rien ")
# func(None)

# %%
help(func)
# %%
# unpacking des valeurs de retour

def func():
    return "val1", "val2"

v1, v2 = func()
tup = func()
tup[0]
# v1, *others = func()

# %%
# paramètres positionnels/obligatoire
def func(p1, p2):
    return p1, p2

# positionnel => l'ordre d'appel corresponde à 
# l'ordre de définition
func(1, 2)
# obligatoires
# TypeError
# func(1)

# %%
# appel nommé
def func(p1, p2):
    return p1, p2

# on flèche les valeurs sur les paramètres
# meilleure lisibilité et organisation de l'appel
func(p2=1, p1=2)

# %%
# paramètres nommés/optionnels à la def
# attention: les positionnels sont avant les nommés
# def func(p1="dflt", p2):
def func(p1, p2="dflt"):
    return p1, p2

func(1)
# SyntaxError
# func(p2=1, 2)


# %%
# paramètres positionnels supplémentaires
def func(p1, p2, *params):
    """
    expliquer comment utiliser *params
    """
    return p1, p2, params

func(1, 2, 3, 4, 5)
# non obligatoires
func(1, 2)

# %%
def func(p1, p2="dflt", **kwargs):
    """
    expliquer comment utiliser **kwargs
    """
    return p1, p2, kwargs

func(1, option1=3, option2=4)
# %%
# *values dans la signature de print
# print()

# %%
# * à l'appel
def func(p1, p2, *params):
    return p1, p2, params
params = (1, 2, 3, 4, 5)
# désagréable
# func(params[0], params[1], params[2], params[3], params[4])
# agréable
func(*params)
# %%
def func(p1, p2, p3):
    return p1, p2, p3

keywords = {"p2": 2, "p1": 1, "p3": 3}
# func(keywords["p1"], keywords["p2"], keywords["p3"])
func(**keywords)

# %%
# portée des variables: variables globales
def do_thing():
    print(f"x dans la fonction: {x, id(x)}")

x = 10

do_thing()
print(f"x hors de la fonction: {x, id(x)}")
# x est globale à la fonction do_thing


# %%
# portée des variables: variables locales à une fonction
def do_thing():
    x = 5
    print(f"x local  à la fonction: {x, id(x)}")

x = 10

do_thing()
print(f"x global hors de la fonction: {x, id(x)}")
# le x global n'est pas mis à jour dans la fonction
# un x local est créé dans la portée de la fonction,
# et n'existe que le temps d'exécution de la fonction

# %%
# portée des variables: variables locales à une fonction
def do_thing():
    global x, y
    x = 5
    print(f"x global dans la fonction: {x, id(x)}")

x, y = 10, 15

do_thing()
print(f"x global hors de la fonction: {x, id(x)}")
# le x global est utilisé dans la fonciton en tant que tel
# le x global est fonc modifié par la fonction
#la valeur modifiée est disponible après la fonction

# %%
# attention aux mutables dans les passages par paramètres
def add_to_list(lst: list, elem):
    # lst.append(elem)
    lst += [4]
    # lst = lst + [4]
    print(f'emplacement mem du paramètres: {id(lst)}')

l = [1, 2, 3]
print(f'emplacement mem de laglobale: {id(l)}')
add_to_list(l, 4)
print(l)

# les paramètres de fonctions sont des références aux variables
# globales injectées dans la fonction
# si le paramètre est un mutable, on peut modifier
# la globale depuis la fonction 
# %%

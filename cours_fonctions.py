# %%
# définition et appel
# définition
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

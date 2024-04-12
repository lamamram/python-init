# %%
# définition de fonction
def fct():
    print("coucou")
    # return 0

def ret():
    return "coucou"

# fct est une procédure, i.e une fonction 
# sans valeur de retour

# appeler la fonction
# () : l'opérateur parenthèse
# fct() est une expression qui a une valeur
# une fonction sans valeur de retour retourne None
print(fct())
# ret() retourne la chaine caractère "coucou"
print(ret())


# %%
# paramètres
# param: annotation: information sur les paramètres
def fct(param: "int|str|float"):
    """
    fonction *3 blabla
    paramètres possibles ....
    valeurs de retour: rt, error
    """
    # ci dessus documentation
    if type(param) in [int, float, str]:
        return  3 * param, None
    else:
        return None, f"{param} est un {type(param)} !!!"

        
# polymorphismee
fct(2)
rt, error = fct("rien")
print(rt, error)
# attention: responsabilité de l'utilisateur
rt, error = fct({"k": "v"})
print(rt, error)
# %%
# les fonctions sont des objets comme les autres !!!
fct.__annotations__
fct.__doc__
# %%
# répittion
[0] * 10

# %%
# types de paramètres
# paramètre positionnels / obligatoires
def fct(p1, p2):
    return p1, p2

fct("p1", "p2")
# obligatoire
# fct("p1")
# positionnels
fct("p2", "p1")

# cela dit, la définition est positionnelle ...
# mais on peut appeler la fonction avec des paramètres nommés
fct(p2="p2", p1="p1")
# %%
# paramètres nommés/optionnels à la définition
# ordre des paramètres, les positionnels avant les nommés
def fct(p1, sec="default", sec2="alt"):
    return p1, sec, sec2

fct("p1")
fct("p1", "sec")
# flécher les valeurs si l'on a plusieurs paramètres nommés 
# fct("p1", "sec2")
fct("p1", sec2="sec2")

# %%
# paramètres *args: vont donner la possibilité d'appeler autant de paramètres positionnels
# print("ok", "ko", "hello")
def fct(*args):
    # args est un tuple qu'on peut exploiter
    return args

print(fct(1, 2, 3, "ok"), p=1)
# optionnels,  donc à gauche des positionnels
# mais positionnels donc à gauche des nommés
fct()

# %%
# "kw"  => keyword
# sont des paramètres nommés optionnels de nombres variables
def fct(**kwargs):
    # args est un tuple qu'on peut exploiter
    return kwargs

fct(k1="v1", k2="v2")
# %%
# signature universelle
def fct(*args, **kwargs):
    return args, kwargs

fct(1, 2, 3, 4, k1="v1", k2="v2")

# %%
import random
from time import time

def square(x: float):
    return x ** 2
# génération d'une liste de 30 float entre 1 à 100
numbers = [ random.random()*random.randint(1, 100) for _ in range(300) ]
# numbers = [ square(random.random()*random.randint(1, 100)) for _ in range(30) ]
print(numbers)

# %%
# technique programmation impérative
start = time()
for i, n in enumerate(numbers):
    numbers[i] = square(n)
print(time() - start)
numbers


# technique de programmation fonctionnelle
# map applique une fonction en paramètres sur tous les éléments
# d'un itérable en paramètres
# retourne un itérable des valeurs transformées par la fonction
# %%
# map est codée en C donc bcp plus rapide 
# => que un for
# => qu'une liste en compréhension []
start = time()

#Y =  map ° square (X)
# Y = SQUARE * X
# REM: la valeur de retour est un "objet map"
# => qui est un itérable (comme une liste)
# => qu'on ne peut pas affichier mais qu'on peut exploiter
squares = map(square, numbers)
print(time() - start)

# %%
# print(squares)

# fonction nommées :réutilisable
def inf_1000(f: float):
    return f < 1000

print(filter(lambda f: f < 1000, squares))

# %%
from random import shuffle
# tri
values = [f"values_{i}" for i in range(20) ]
shuffle(values)
## NB: .sort() => change la liste mais ne retourne pas
# values.sort()
# values
## sorted(l): retourne la valeur triée mais ne change pas le paramètre
# je veux trier sur l'entier compris dans mes valeurs, situé après l'underscore
sorted(values, key=lambda v: int(v[v.index("_") + 1:]))

# %%
# %%

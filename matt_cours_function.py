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

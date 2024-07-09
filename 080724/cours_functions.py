# %%
# definition
def ma_fonction():
    print("coucou")

# appel, application de l'opérateur "()" à la fonction
ma_fonction()
# %%
# l'instruction termine le bloc puis retourne la valeur associée ou alors None
def ma_print_func():
     # exécution d'une ligne du bloc
     print("coucou")

def ma_fonction():
    return "coucou"
    print("after")

print(ma_print_func()) # affiche la valeur de retour de ma_print_func => None
ma_fonction() # valeur de retour de l'expression ou de l'appel ma_fonction
f"{ma_fonction()} tout le monde" 
# %%

def ma_fonction():
  l = "WORLD" # variable locale à la fonction
  print(f"{g} {l} !") # lecture de g globale
  # g = "HELLO" # UnboundLocalError: 
  # on ne peut (plus) modifier une globale dans
  # la portée locale.

g = "hello" # variable globale à la fonction
ma_fonction()
print(l) # NameError: l n'existe pas en dehors de la fonction

# %%
# technique de programmation dont le but
# d'implémenter des fonctions sans retour (procédures)
# mais qui vont modifier l'état des variables globales

def ma_fonction():
  global g # on peut modifier la g en tant que g
  l = "WORLD" 
  g = g.upper() # réaffectation d'un immutable => chgt d'id
  print(f"{g} {l} !", id(g))

g = "hello" # variable globale à la fonction
print(id(g))
ma_fonction()
# le "global g" permet d'utiliser l'id modifié de g 
# dans la portée locale (fonction) 
# dans la portée globale (extérieur de la fonction) 
print(id(g)) 

# %%
def ma_fonction(p1, p2):
  return p1, p2

ma_fonction("p1", "p2") # "p1", "p2" : même position !!!
ma_fonction("p1") # ERREUR: paramètres positionnels = obligatoires

# %%
# def ma_fonction(p2="dflt", p1): SYNTAXERROR
def ma_fonction(p1, p2="dflt"):
  return p1, p2

ma_fonction("p1", "p2") # "p1", "p2" : normal
ma_fonction("p1") # OK

# %%

def ma_fonction(p1, p2):
  return p1, p2

# flécher les valeurs des paramètres à l'appel
# 1/ on a pas besoin de mémoriser l'ordre des paramètre de la définition
# 2/ lisibilité # mysql_connect(host=192.168.1.15, user=mysql, port=3306, db=machin)
ma_fonction(p2="p1", p1="p2")

# %%

def my_func(a, b="dflt", c=3.14):
   print(a, b, c)

my_func(1, "dflt", 8.12) # appel positionnel
my_func(1, c=8.12) # appel nommé
# %%
def my_join(*params):
   print(params)
   return " ".join(params)

my_join("truc")
my_join("truc", "machin")

# %%
def my_join(params):
   return " ".join(params)

my_join(["truc"])
my_join(["truc", "machin"])

# %%

def my_func(param, **options):
   if "debug" in options and options["debug"]:
      print(f"DEBUG: param vaut : {param}")
   return param

my_func(10)
my_func(10, debug=True)
# %%

def my_func(p1, p2, p3):
   return p1 ,p2, p3

params = ["p1", "p2", "p3"]

my_func(params[0], params[1], params[2])
my_func(*params)
# %%

def my_func(p1, p2, p3):
   return p1 ,p2, p3

params = {"p1": "v1", "p3": "v3", "p2": "v2"}

my_func(params["p1"], params["p2"], params["p3"])
my_func(**params)

# %%
# introspection des fonctions

def my_func():
  """
  DOCSTRING !! qu'on met sur la 1ère ligne du bloc
  ma fonction my_func qui ne fait RIEN !!
  ...
  ...
  """
  pass

# print(my_func)
type(my_func)
id(my_func)
dir(my_func)
# help(my_func)
print(my_func.__doc__)

# %%
# documentation contextuelle utilisée par l'autocompléteur des EDI
# help(str.replace)
"truc".replace()
my_func()
# %%

def my_func(nom: str, age: int=33) -> str:
   age += 2
   return f"nom: {nom}, age: {age}"

my_func("matt")
# my_func("matt", "troite trois")

my_func.__annotations__
my_func()
# %%
# notion de fonction lambda

# programmation impérative
lst = list(range(100))

for i, val in enumerate(lst):
   lst[i] = val**2

lst
# %%

# idem en programmation fonctionnelle
# fonction nommée
def sq(x):
   return x**2

lst = list(range(100))
# map est capable d'appliquer une fonction en paramètre
# sur tous les éléments d'un itérable
list(map(sq, lst)) # y = map ° sq(lst)


# %%
# avec une fonction anonyme
lst = list(range(100))
# list(map(lambda x:x**2, lst)) # y = map ° sq(lst)

list(filter(lambda x: x > 50, lst))

# %%
# tri complexe
from random import shuffle
lst = [ f"line_{i}" for i in range(20) ]
shuffle(lst)
lst
# %%
# sorted(lst)
sorted(lst, key=lambda l: int(l[5:]))
# %%

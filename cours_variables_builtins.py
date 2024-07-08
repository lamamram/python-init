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

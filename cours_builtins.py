# %%
# affectation: mettre 10 dans x
# j'ai déclaré un nom de variable: x
# j'ai initialisé cette variable avec la valur 10 en int
x = 10
y = 42
# le plus ici est l'opérateur de l'addition des ints
# notion: d'expression: toute inscription evaluable
print(x)
print(42)
x + 42
x + y
# %%
# opération sur les builtins de type str
first_word = "hello my Jack's"
second_word = 'world'
first_word + " " + second_word
# %%
# typage fort: pas (bcp) de conversion de type implicite
# on doit faire des conversion de type explicite
calcul  = 1
print("j'ai " + str(calcul + y) + " truc")
# conversion avec les paramètres du print 
# et concaténation auto avec " " 
print("j'ai", calcul + y, "truc")
print("j'ai", calcul + y, "truc", sep='"')
# idem avec "\" échappement de caractère
# i.e que le caractère suivant abndonne son rôle en python
print("j'ai", calcul + y, "truc", sep="\"")
# f-string: interpolation des expressions python
# dans une chaine de caractère
print(f"j'ai {calcul + y} truc")
# %%
# on peut échapper le \n
bad_tpl = "j'ai veux \
machin"
# """"""" interpréter le \n
template = """
j'ai {0} truc, 
et aussi {1} machins
""".format(calcul + y, 33)
template

# %%
# petites conversion implicites
# convention de constante... mais
# représentation d'un nombre réel
PI = 3.14
PI = 2.34
# float -> int
# PI + 1.0
PI + 2

# %%
# une liste
numbers = [1, 2, 3.14, -3.33]
type(numbers)
# on peut insérer tout ce que 
nawak = [0, True, 1.41, "chariot", numbers]
nawak
# %%
# longueur de la liste
len(nawak)
# demander == lire == get un élement à l'index i
nawak[0], nawak[1], nawak[len(nawak) - 1], nawak[-1][0]
# %%
# le "slicing"
# l'indice de début est compris mais l'indice de fin n'est pas compris
# ou jusqu'à la fin
nawak[1:3]
nawak[1:], nawak[:3]
nawak[-2:], nawak[-3:-2]
# pas de prèlevement tous les 2
nawak[::2], nawak[::-1]



# %%
numbers = [1, 2, 3.14, -3.33]
# modifier , écrire, set
numbers[0] = -1
# Wrong !!
# numbers[5] = 8.8
numbers.append(8.8)
# numbers.remove(8.8)
# dépiler et retourne à droite ou à gauche
print(numbers.pop())
# print(numbers.pop(0))
numbers

# %%
# numbers = numbers + [1, 4, 5.5]
# opérateur accumulatifs
numbers += [1, 4, 5.5]

# numbers.extend([1, 4, 5.5])
numbers
# %%

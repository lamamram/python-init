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
x = input("tapez un entier: ")
print(type(x))
x = int(x)
# unpacking en python
x < 5, x == 10, x != 33, x >= 8
equal_to_10 = x == 10 
if equal_to_10:
    print(x + 12)
    print("x est 10 !!")
else:
    print("x n'est pas 10 !!")
# %%

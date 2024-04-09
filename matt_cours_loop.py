# %%
# un type de donnée itérable => on peut l'employer
# avec boucle for
words = ["un", "chat", "est", "un", "chat"]
for word in words[::-1]:
    print(word)
# %%
# opérateur in
33 in words, "chat" in words, "un" not in words
["un", "chat"] in words

# %%
# autres itérables
proverb = "un chat est un chat"
for letter in proverb:
    print(letter)

proverb[0], proverb[3:7], proverb[-4:]
"c" in proverb, "chat" in proverb

# %%
# mutabilité vs immutabilité
proverb = "un chat est un chat"
# one ne peut pas changer la valeur d'une chaine
# de façon interne => type immutable
# TypeError
# proverb[0] = "U"
# réaffectation totale
# proverb = "Un chat est un chat"
proverb.index("chat")
proverb = proverb.capitalize()
# %%
# autres fonctions de str
n = 5
proverb.replace(proverb[n], proverb[n].upper())
# %%
# le type tuple (en français un n-uplet (x1, ..., xn) )
tup = (1, 2, 3.14,"ok")
tup[0], tup[-1], tup[2:4]
for elem in tup: print(elem)
# =  liste immutable
tup[0] = 1
# %%
# mécanisme d'"unpacking"
x, y, z = 0, 1, 2
x, y, z = (0, 1, 2)
x, y, z
# %%
a, b = 0, 1
# a = b
# b = a + b
while b < 100:
# le a à droite n'a pas vu l'affectaion de gauche
    a, b = b, a + b
    print(b)
# c = a + b
# d = b + c
# ...


# %%


# %%
# un type de donnée itérable => on peut l'employer
# avec boucle for
words = ["un", "chat", "est", "un", "chat"]
for word in words[::-1]:
    print(word)


# %%
words = ["un", "chat", "est", "un", "chat"]
upper_sentence = []
for w in words:
    upper_sentence.append(w.upper())
" ".join(upper_sentence)

# %%
# idem sans nouvelle liste
words = ["un", "chat", "est", "un", "chat"]
i = 0
# for _ in words:
for w in words:
    # print(w is words[i])
    # quand on modifie w il n'est plus (is not) words[i]
    # donc çà ne marche pas
    # w = w.upper()
    words[i] = words[i].upper()
    # print(w is words[i])
    i += 1
" ".join(words)

# %%
# idem avec les bons outils
words = ["un", "chat", "est", "un", "chat"]
# list(enumerate(words, start=1))
for i, word in enumerate(words):
     words[i] = word.upper()
" ".join(words)

# %%
# liste en intension, ou en comprehension
words = ["un", "chat", "est", "un", "chat"]
# " ".join( [ w.upper() for w in words ] )
" ".join( [ w.upper() for w in words if w != "chat" ] )

# %%
# break continue else et la range
# for i in range(10):
# for i in range(1, 11):
# for i in range(10, -1, -1):
#     print(i)
n = 2
while n < 100:
    # nombre pair non premier 
    if n % 2 == 0 and n > 2:
        n += 1
        # on arrête l'itération courante et on commence l'itération suivante
        continue
    for i in range(2, n//2 + 1):
        if n % i == 0:
            # divisible donc arrête le for
            break
    # pas de break donc pas de diviseur donc premier ! 
    else:
        print(n)
    n += 1




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
# if 0:
#if None:
# if []:
# if 3.3333333:
    print("ok")

# %%

# %%
# str, list, tuples: operateur communs
# in
"h" in "hello"
"hell" in "hello"

1 not in [1, 2, 3]
[1, 2] in [1, 2, 3, [1, 2]]
# %%
# + *
'hello' + " wrold"
# attention: tuple à 1 élément
(1, 2) + (3,)

3 * "rien"
[0] * 10
# %%
# slicing
msg = "à bon chat bon rat"
# à bon chat: indoce de début compris, fin non compris
msg[0:10]
msg[:10]
# bon rat
msg[11:]
msg[msg.index("bon", 5):]

# indices négatifs
msg[:-3]

# pas de prélèvement
msg[::2]
# inversion
msg[::-1]
# %%
# str -> list -> str
words = msg.split()
words
" ".join(words[::-1])
# %%
# itération
# for élement in ensemble
for letter in msg:
    print(letter)

for w in words:
    print(w.upper())
# %%
# fonction range pour générer des gammes d'entiers
# même signature qu'un slicing
for i in range(10, -1, -1):
    print(i)

# %%

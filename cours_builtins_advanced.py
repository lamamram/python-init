# %%
# concaténation et répétition

sentence = "toto " + "tata"
sentence

numbers = [1, 2, 3]
numbers + [4, 5, 6]
numbers += [4, 5, 6]
# adage
3 * "rien "

[0] * 10
# %%
# opérateur in: élément dans itérable
6 in numbers
"toto" in sentence # spécifique à str
[5,6] not in numbers # True !!! pas de gestion des sous éléments

# %%
# .index et .count

sentence = "appeler un chat un chat"
sentence.index("chat")
sentence.count("chat")
sentence.index("chat", 15)

start = 0

while sentence[start:].count("chat"):
    ind = sentence.index("chat", start)
    print(ind)
    start = ind + len("chat")
    ## IL FAUT QUE LE BLOC CHANGE LE TEST !!!! SINON INFINITE LOOP
# %%

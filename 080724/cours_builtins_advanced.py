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

lst, tpl, word = [-1, 2, 3], (-1, 2, 3), "bonjour"
# list est MUTABLE
lst[0] = 1 # OK, modification partielle, id(lst) inchangé
# str et tuple sont IMMUTABLE
# word[0] = "B" # TypeError
# tpl[0] = -1 # TypeError
word, tpl = "Bonjour", (1, 2, 3) # OK mais modifie id(word) et id(tpl)
# %%
# modification de str
word = "bonjour"

# retourne la transformation
# mais word inchangé
print(word.capitalize())
print(word)
word = word.capitalize()

# %% 
# modification de listes

lst = [1, 2, 3, 4]
dir(lst)
# pop retourne et supprime
while lst:
    print(lst.pop())

legit_animals = ["chat", "chien", "ane", "cheval", "chat"]
while legit_animals.count("chat"):
    legit_animals.remove("chat")
legit_animals

# %%

# attention au unpacking

a, b = 0, 1

a, b = b, a + b # ici le a de droite vaut 0

a = b
b = a + b # ici le a de droite vaut 1

a, b
# %%
# création de clés / paires de dico VS création d'éléments de list

dico, lst = {"k": "v"}, [1, 2, 3]

dico["k2"] = "v2"
# lst[3] = 4 # IndexError

lst.append(4)
# %%
# checker si une clé existe dans un dico pour utiliser sa valeur

dico = {"k": "v"}

# if "truc" in dico:
#     print(dico["truc"])
# else:
#     print("default")

dico.get("truc", "default")
dico.get("k", "default")
# %%

x = 1
del x
# x + 1 # NameError 
# %%

lst = [-1,3]
del lst[0]
lst
# %%
# objets intermédiaires
dico = {"k": "v"}
dico.values() # objet "dict_values"
list(dico.values())

dico.items() # objet "dict_items"
list(dico.items())
# %%
# utilisation des .values et .items

dico = {"k": "v", "k2": "v2", "k3": "v3"}

for k in dico: print(k)

for v in dico.values(): print(v)

# unpacking sous jacent depuis les tuples gérés dans l'objet dict_items
for k, v in dico.items(): print(k, v)
# %%
# affectations des listes

lst = [1, 2, 3]
lst2 = lst # passage par référence
lst.append(4) # modifie lst ET lst2 car
print(lst is lst2, lst2) # True, [1,2,3,4]
lst = [1,2,3]
lst3 = lst.copy() # ou lst[:] => "copie creuse" i.e indépendante en mémoire
lst.append(4) # modifie lst MAIS PAS lst3 car
print(lst is lst3, lst3) # False, [1,2,3] 
# %%

# idem dico

dico = {"k": "v", "k2": "v2", "k3": "v3"}

dico2, dico3 = dico, dico.copy()
del dico["k"]
dico2, dico3

# %%

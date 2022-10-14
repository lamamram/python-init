# %%
# points communs entre str, list, et tuple
# conversions
chaine = "à bon chat bon rat"
lst = [1, 2, 3]
tup = tuple(lst)
list(tuple(lst))
# liste des caractères individuels de la chaine
list(chaine)
# représentation sous forme de str de la liste
str(lst)
# print() utilise str() en sous main
print(lst)

# %%
# []: accès aux éléments par des indices enties
# types indexables
# ex.premier, dernier élément par la gauche ou par la droite
lst[0], lst[-3], lst[2], lst[-1]
tup[0], tup[-3], tup[2], tup[-1]
chaine[0], chaine[-len(chaine)], chaine[len(chaine) - 1], chaine[-1]
# IndexError
# chaine[44]
# %%
# même comportement par rapport à certaines fonctions standard
# longueur, somme, max, min ...
len(lst), len(chaine)
sum(lst), sum(tup)
min(chaine), min(lst)
# %%
# opérateur in
4 in lst
# la liste [1, 2] n'es pas un élément de lst
[1, 2] in lst
# %%
"a" in chaine
"chat" in chaine

# %%
# index (position) de la 1ère occurence d'un élément
chaine.index("bon")
lst.index(3)
# nb d'occurences de l'élément recherché
chaine.count("bon")

# %%
# opérateur + et * sur les séquences 
chaine + "."
lst + [4, 5]
tup + (4, 5)

# répétition
3 * "rien "
[0] * 13

# %%
# slicing de séquence
motif = "chat"
chaine[0:10], chaine[11:len(chaine)]
chaine[0:chaine.index(motif) + len(motif)]
# raccourcis
chaine[:chaine.index(motif) + len(motif)]

motif_index = "bon"
start_index = chaine.index(motif_index) + len(motif_index)
chaine[chaine.index("bon", start_index):]

# copie indépendante en mémoire vs simple affectation
lst_bis = lst[:]
lst_ter = lst
lst_bis is lst, lst_ter is lst

# inversion de séquence
chaine[::-1]
# %%
# boucle for
# les types de données qui rentrent dans une
# boucle for son dits itérable
for letter in chaine:
    print(letter)

for elem in lst:
    print(elem)

# %%
# mutabilité vs immutabilité
# mutabilité: opération interne sur la variable
# l'emplacement mém ne change pas
lst[0] = -1
lst
# %%
# immutabilité
# tup[0] = -1
# chaine[0] = "A"
# changement par réaffectation uniquement
chaine = "A bon chat bon rat"
chaine = chaine.capitalize()
chaine
# %%
# fonctions internes sur les listes

lst = ["c", "d", "e"]
## fonctions qui modifient la variable
## et ne retourne rien => None
# ajout par la droite : append
print(lst.append("f"))
lst
# ajout par la gauche
lst.insert(0, "b")
lst
## fonctions qui modifient et retourne 
print(lst.pop())
print(lst.pop(0))
lst
# %%
# choix d'une transformation interne ou externe
lst.sort(reverse=True)
lst
print(sorted(lst))
lst
# %%
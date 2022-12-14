# %%
# palindromes 
# comment savoir si une chaine se lit
# de la même façon dans les deux sens
chaine = "esoperesteicietserepose"
# if condition: entête
if chaine == chaine[::-1]:
    # indentation: bloc
    print(chaine, " est un palindrome !!")
# retour à l'indentation précédente: sortie du bloc
else:
    print(chaine, " n'est pas un palindrome !!")

# %%
# écrire le code permettant d'obtenir le dessin suivant
# hint: se donner deux variables
# h pour hauteur et motif pour ^
# hint: utiliser la fonction range(h) pour itéter sur
# les entiers de 0 à h non compris

#   ^
#  ^^^
# ^^^^^

h, motif = 3, "^"
for i in range(1, h + 1):
    # pour chaque ligne
    # combien d'espaces et combien de motifs 
    print((h - i) * " " + (2 * i - 1) * motif)
# %%
# %%
# reprendre le calcul de moyenne
# 1. possibilité de saisir d'un coup une série de nombres
# ex. de saisie: 1,2.6,truc,...
# 2. analyser chaque valeur de la saisie pour déterminer s'il s'agît
# d'un nombre (commencer par entier, puis entier relatif, puis réel)
# HINT: regarder la fonction str.isnumeric()
# 3. les valeurs numériques sont placées dans une nouvelle liste
# 4. calcul de la moyenne à partir de la nouvelle liste, 
# uniquement s'il n'y a pas eu erreur de saisie

values = input("Veuillez entrez des nombres séparés par ,: ")
numbers = []
stop = False
for value in values.split(","):
    #    n >= 0         ou   n < 0 
    if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
        numbers.append(int(value))
    else:
        print(value, "is not a number")
        stop = True

# len(numbers) renvoie un entier
# dans un if il est évalué en tant que booléen 
# => True si != 0 et False si == 0
if not stop and len(numbers):
    moy = sum(numbers)/len(numbers)
    # à ne pas faire !!
    # print("moyenne de " + str(numbers) + " : " + str(round(moy, 2)))
    # on peut faire
    # print("moyenne de ", numbers, ":", round(moy, 2))
    # ...mais obsolète
    # print("moyenne de %s : %.2f" % (numbers, round(moy, 2)))
    # péférable
    print("moyenne de {1} : {0:.2f}".format(moy, numbers))
    print(f"moyenne de {numbers} : {moy + 2:.2f}")
# %%
# version avec manipulation de la boucle
values = input("Veuillez entrez des nombres séparés par ,: ")
numbers = []
for value in values.split(","):
    if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
        numbers.append(int(value))
    else:
        print(f"{value} is not a number")
        break
# le bloc else s'exécute si on ne rencontre jamais break
# dans la boucle
# for: on itère jusqu'au bout de l'itérable
# while: la condition du while devient fausse
else:
    if len(numbers):
        moy = sum(numbers)/len(numbers)
        print(f"moyenne de {numbers} : {moy + 2:.2f}")

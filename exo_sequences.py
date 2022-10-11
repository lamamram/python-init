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
values = values.split(",")
numbers = []
stop = False
for value in values:
    #    n >= 0         ou   n < 0 
    if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
        numbers.append(int(value))
    else:
        print(value, "is not a number")
        stop = True

if not stop and len(numbers) != 0:
    moy = sum(numbers)/len(numbers)
    print("moyenne de ", numbers, ":", round(moy, 2))
# %%

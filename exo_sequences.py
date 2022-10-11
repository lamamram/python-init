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

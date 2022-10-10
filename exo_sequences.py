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

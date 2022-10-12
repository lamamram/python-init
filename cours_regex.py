# %%
import re
# une expression régulière (ou rationnelle) est une
# chaine de caractère qui décrit un modèle de chaines de caractères
# exemple de regex: un code postal français

# 1er caractère 0,1,3,4,5,6,7,8 ou 9 et ensuite 4 chiffres
# ou
# 2 suivi de 0-9 ou A ou B suivi de 3 chiffres

# en langage Regex
pattern = "[013456789][0-9]{4}|2[0-9AB][0-9]{3}"

target_match = "44000 est mon cp"
target_search = "mon cp est 44000 ou 2A320"

# cherche à faire correspondre la regex depuis le début, pas à la fin
# commence par la regex
re.match(pattern, target_match)
# print(re.match(pattern, target_search))

# contient la regex => 1ère occurence
re.search(pattern, target_search)

# toutes les occurences
list(re.finditer(pattern, target_search))
re.findall(pattern, target_search)

# chercher / remplacer
re.sub(pattern, "*****", target_search)

re.split(pattern, "2 rue du la rép 75013 PARIS")
# %%

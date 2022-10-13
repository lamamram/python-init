# %%
# 1. créer deux modules cleaner et counter dans le package utils
# 2. dans cleaner créer une classe Cleaner:
# en paramètre: un texte, une chaine de signes de ponctuation , un nb min. de lettre pour les mots
# hint: regarder la variable punctuation du module string
# interface: 
#   - 4 méthodes privées
#      - regex de suppression de signes de ponctuation
#      - regex de suppression des sauts de ligne 
#      - regex de suppression des suites d'espaces > 1
#      - virer les petits mots
#   - une méthode publique
#     - appelle les méthodes privées 
#     - retourne le texte nettoyé en minuscule

# 3. dans counter, créer une classe Counter
# en paramètre: un objet cleaner ?
# interface:
# méthode publique get_occurences(nb de mots à afficher)
# utiliser la fonction dans misc.py
# trier le dictionnaire d'occurence par ordre décroissant
# affiche les n premiers mots par ordre d'occurence
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

# méthode:
# 1. structurer les classes avant d'écrire le contenu des méthodes (sauf __init__)
# 2. écrire le programme (imports, instanciation et exécution de la méthode publique)
#    avant le contenu des méthodes

# %%
from utils.cleaner import Cleaner
from utils.counter import Counter

txt = """
To create a GUI for your windows and dialogs in PyQt, you can take two main paths: you can use Qt Designer, or you can hand code the GUI in plain Python code. The first path can dramatically improve your productivity, 
whereas the second path puts you in full control of your application’s code.

GUI applications often consist of a main window and several dialogs. If you’re looking to create these graphical components in an 
efficient and user-friendly way, then Qt Designer is the tool for you. In this tutorial, you’ll learn how to use Qt Designer to create your GUIs productively.
"""
from string import punctuation
# sans couplage: le programme
# principal a la responsabilité
# de l'association
# cl = Cleaner(txt)
# co = Counter(cl.clean())

# couplage faible: counter ne connait que l'interface de cleaner
# i.e les méthodes publiques
# interêt: on peut plus envoyer n'importe quel texte
co = Counter(Cleaner(txt))


# couplage fort
# co = Counter(txt, punctuation, 4)
# co.get_occurences(5)
# %%

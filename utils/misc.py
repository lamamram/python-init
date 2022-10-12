"""
modules contenant des fonctions de manipulation de texte
- strip_little_words
- get_occurences
"""

if __name__ == "__main__":
    # si on veut tester le module depuis
    # le package (pas conseillé)
    from helpers import to_lower
else:
    # les imports sont calculés depuis
    # le dossier du programme principal
    # (dossier racine du projet)
    # "chemin absolu depuis la racine"
    from utils.helpers import to_lower
    # "chemin relatif"
    # "." désigne le package courant
    from .helpers import to_lower

PI = 3.14

def strip_lil_words(text, min_length=4):
    """
    nettoie un texte des mots inférieur à un paramètre
    """
    return to_lower(" ".join(filter(
        lambda w: len(w) >= min_length, 
        text.split()
    )))

def get_occurences(text: str):
    occ = {}
    for w in text.split():
        if w not in occ: occ[w] = 1
        else: occ[w] += 1
    return occ

if __name__ == "__main__":
    print(strip_lil_words("à bon chat bon rat"))


"""
modules contenant des fonctions de manipulation de texte
- strip_little_words
- get_occurences
"""

PI = 3.14
# %%
# 1. écrire une fonction qui renvoie un texte donné
# (chaine de mots séparés par " ")
# qui ne conserve que les mots d'au moins 4 caractères

# version impérative
def strip_lil_words(text: str, min_length: int):
    cleaned = []
    for word in text.split():
        if len(word) >= min_length:
            cleaned.append(word)
    return " ".join(cleaned)

# version "sucre syntaxique" 
def strip_lil_words(text: str, min_length: int):
    return " ".join([ w for w in text.split() if len(w) >= min_length])

# version fonctionnelle
# def sup_length(word, min_length=4):
#     return len(word) >= min_length

# fonction lambda, anaonyme, à usage unique
# dont le code se résume à 1 expression
# filter applique une fonction de filtre
# (qui renvoie un booléen) sur un itérable (ex. une liste)
# et qui renvoie les éléments de l'itérable qui
# répondent vrai à la fonction
def strip_lil_words(text, min_length=4):
    """
    nettoie un texte des mots inférieur à un paramètre
    """
    return " ".join(filter(
        lambda w: len(w) >= min_length, 
        text.split()
    ))



# %%
# 2. écrire une fonction qui renvoie un dictionnaires
# présentant en clés les mots d'un texte donné
# (chaine de mots séparés par " ")
# et en valeurs le nb d'occurence de ces mots dans le texte
# ex. à bon chat bon rat => {"à": 1, "bon": 2, "chat: 1" ...}

def get_occurences(text: str):
    occ = {}
    for w in text.split():
        if w not in occ: occ[w] = 1
        else: occ[w] += 1
    return occ



# def sort_occurences(dico: dict):
#     output = {}
#     max_occ = 0
#     for word, occ in dico.items():
#         ...


# bonne pratique pour tous les modules
if __name__ == "__main__":
# vaut "misc" si importé et "__main__" si 
# exécuté en tant que programme principal
# i.e directement par l'interpréteur
    txt = "kerjf erk elr er elrgrkg"
    strip_lil_words(txt, 4)
    dico = get_occurences("à bon chat bon rat")
    print(dict(sorted(
        dico.items(), 
        key= lambda tup: tup[1], 
        reverse=True
    )))
# %%

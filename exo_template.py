# %%
# exercice : remplacer les clés entourées par "((" et "))"
# dans un texte par les valeurs correspondantes dans un dico

# 1. afficher le contenu entre la première occurence de (( et ))
# 2. remplacer ((key1)) par content1 dans _template
# Hint: regarder la fonction str.replace
# 3. itérer sur _template pour remplacer toutes les slots (())
# par la valeur liée à la clé correspondante si celle ci existe ou par N/A

_template = """
lorem ipsum (blabla) ... ((key1)) blabla ....
lorem ipsum (blabla) ... ((key2)) blabla ....
lorem ipsum (blabla) ... ((key3)) blabla ....
lorem ipsum (blabla) ... ((key4)) blabla ....
"""

injections = {
    "key1": "content1",
    "key2": "content2",
    "key3": "content3"
}

# %%
# conception générale d'une boucle while
# 1. tester les premières itérations à la main
# 2. analyser les résultats pour en déduire
# l'évolution des variables => la condition de bouclage
while "((" in _template:
    start_index = _template.index("((") + len("((")
    end_index = _template.index("))")
    key = _template[start_index:end_index]

    # penser à mettre jour la variable avec la transformation
    _template = _template.replace(
        "((" + key + "))", 
        injections.get(key, "N/A")
    )
_template
# %%

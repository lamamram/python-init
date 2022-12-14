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
# porter le script ci dessus en fonction
# 1. choisir un nom
# 2. choisir les paramètres pertinents avec leur ordre d'importance
# obligatoires (sans valeur par défaut), optionnels (valeurs + souvent utilisée)
# une fois les paramètres décidés, 
# refactoriser les valeurs en dur d'après les paramètres
# 3. gérer la valeur de retour
def parse_template(tpl: str, contents: dict, slots=("{{", "}}"), default="N/A"):
    while slots[0] in tpl:
        start_index = tpl.index(slots[0]) + len(slots[0])
        end_index = tpl.index(slots[1])
        key = tpl[start_index:end_index]

        # penser à mettre jour la variable avec la transformation
        tpl = tpl.replace(
            slots[0] + key + slots[1], 
            str(contents.get(key, default))
        )
    return tpl

_tpl = "name: {{name}}, firstname: {{firstname}}, age: {{age}}, password: {{password}}"
contents = {"name": "lamam", "firstname": "matt", "age": 38}

parse_template(_tpl, contents, default="******")
# %%

# %%
# exercice : remplacer les clés entourées par "((" et "))"
# dans un texte par les valeurs correspondantes dans un dico

# 1. afficher le contenu entre la première occurence de (( et ))
# 2. remplacer ((key1)) par content1 dans _template
# Hint: regarder la fonction str.replace
# 3. itérer sur _template pour remplacer toutes les slots (())
# par la clé correspondante si celle ci existe ou par N/A

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
while "((" in _template:
    index_start = _template.index("((") + len("((")
    index_end = _template.index("))")
    key = _template[index_start:index_end]
    _template = _template.replace(f"(({key}))", injections.get(key, "N/A"))
_template
# %%
# portage en fonction
# définition
# paramètres positionnels / obligatoires, puis paramètres nommés / optionnels
# ajour des annotations: purement informatif
def parse_template(tpl: str, values: dict, slot: tuple=("{{","}}"), dflt: str="N/A") -> str:
    """
    Docstring: fonction de templating
    @param tpl: str: template à parser
    ...
    """
    print(f"id du param: {id(tpl)}")
    while slot[0] in tpl:
        index_start = tpl.index(slot[0]) + len(slot[0])
        index_end = tpl.index(slot[1])
        key = tpl[index_start:index_end]
        tpl = tpl.replace(slot[0] + key + slot[1], values.get(key, dflt))

    # valeur de retour
    print(f"id du param: {id(tpl)}")
    return tpl

# appel
print(f"id du template global: {id(_template)}")
parse_template(_template, injections, ("((", "))"))
# valeurs par défaut pour les paramètres nommés
# parse_template("blabla {{key}} {{not_here}}", {"key": "hello"})
# appel nommé
# parse_template(values=injections, tpl=_template)
# %%

# passage par référence des paramètres
def add_to_list(lst: list, value):
    """
    blabla
    """
    print(f"id du param: {id(lst)}")
    lst.append(value)
    # l2 = lst.copy()
    # l2.append(value)
    # return l2

l = [1, 2, 3]
print(f"id de la var globale: {id(l)}")
add_to_list(l, 4)
l
print(add_to_list.__doc__)
print(add_to_list.__annotations__)
# %%

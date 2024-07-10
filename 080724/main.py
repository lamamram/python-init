# %%
# from project.calc import ctrl_mean
# ATTENTION: ne fonctionne pas si l'on a pas l'import du __init__.py !!!
from project import ctrl_mean

if __name__ == "__main__":
    print(ctrl_mean("-1,1", debug=True))
# %%

from text_analyser.occurences_counter import OccurencesCounter

if __name__ == "__main__":
    text = """
Python est un langage de programmation interprété, 
multiparadigme et multiplateformes. 
Il favorise la programmation impérative structurée, 
fonctionnelle et orientée objet. 
Il est doté d'un typage dynamique fort, 
d'une gestion automatique de la mémoire par ramasse-miettes 
et d'un système de gestion d'exceptions ; 
il est ainsi similaire à Perl, Ruby, Scheme, 
Smalltalk et Tcl.
Le langage Python est placé sous 
une licence libre proche de la licence BSD et fonctionne sur la plupart des plateformes informatiques, 
des smartphones aux ordinateurs centraux, 
de Windows à Unix avec notamment GNU/Linux en passant 
par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. 
Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et 
une syntaxe simple à utiliser. 
"""

oc = OccurencesCounter(text)
print(oc.get_occurences())
# %%

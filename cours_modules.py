# %%
# import peut aller trouver
# 1. les modules de la lib standard
# 2. les modules installés via pip
# 3. les modules du répertoire courant

# à l'import tout le code du module est exécuté
# et dispo sous forme de bytecode dans le dossier __pycache__
import misc

txt = "kerjf erk elr er elrgrkg"
# accès au contenu
misc.strip_lil_words(txt, 3)

# documentation
# help(misc)
# attributs du module
# dir(misc)
# nom du module quand celui ci est importé
# misc.__name__
# %%

# %%

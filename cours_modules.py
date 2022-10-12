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
# import sans espace de nom
# attention aux conflits de noms
# utiliser l'alias as pour renommer 
# une variable importée de même nom qu'une variable
# définie après
from misc import PI as PI2, get_occurences # *

PI = 3.14159

txt = "à bon chat bon rat"
get_occurences(txt)
PI, PI2
# print(misc)
# %%
# import utils.misc
# import utils.misc as misc
from utils.misc import PI

# utils.misc.PI
# misc.PI
PI
# %%

from utils.misc import strip_lil_words

strip_lil_words("à bon chat bon rat")
# %%

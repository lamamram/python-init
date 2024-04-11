# %%
"""
les regexes: sont des chaines de caractères, modèles de chaines de caractères qui sont censés
de détecter un motif (pattern)

méta-caractères:

- []: classe: 0-9, a-z, A-Z, [éèàüîôû], [,;./!?]
  => caractère possible pour UN caractère de la cible
- {}: quantificateur {i}, {i, j}, {,j}
- ^ / $ : commence par / fini par
- |: OU
"""
import re

zipcode = "44000"
pas_zipcode = "444000"

# le motif doit correspondre partiellement depuis la gauche
# re.match("[0-9][0-9][0-9][0-9][0-9]", zipcode)
# re.match("[0-9][0-9][0-9][0-9]", zipcode)
# re.match("[0-9]{5}", zipcode)
# re.match("^[0-9]{4,5}$", zipcode)
zipcode_fr_pattern = "[013456789][0-9]{4}|2[0-9AB][0-9]{3}"

zipcode_fr_pattern_strict = f"^{zipcode_fr_pattern}$"

re.match(zipcode_fr_pattern, zipcode)

address = "3 rue des lilas 2B312 AJACCIO"

address2 = "AJACCIO 2B312"

re.search(zipcode_fr_pattern, address)

# replace avec re
re.sub(zipcode_fr_pattern, "******", address)

# split selon une regex
re.split(zipcode_fr_pattern, address)

# %%

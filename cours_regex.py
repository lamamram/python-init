# %%
import re
# (?:) : paranthèse non capturante
float_pattern = "(-?[0-9])+(?:\.[0-9]*)?"
strict_float_pattern = f"^{float_pattern}$"

target1 = "-3.14 is a float"
not_match_target1 = "float: -3.14"
# matche depuis le début
re.match(float_pattern, target1)
re.match(strict_float_pattern, target1)
re.match(float_pattern, not_match_target1)
# %%
target2 = "pi: 3.14, sqrt(two): 1.41"
re.search(float_pattern, target2)
re.findall(float_pattern, target2)
list(re.finditer(float_pattern, target2))
# %%
# %% 
# search replace
re.sub(float_pattern, repl="\\1", string=target2)
# %%

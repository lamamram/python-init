# %%
from datetime import datetime, timedelta
from time import time, sleep
# %%
# création d'objets datetime
dt = datetime(2022, 10, 12, 11, 52)
dt

# depuis une liste
date_parts = [2022, 10, 12, 11, 52]
dt = datetime(*date_parts)
dt

# depuis une chaine de caractères
# "p" comme parse
date_str = "2022-10-12 11:52"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt

# %%
# depuis un timestamp (nb de sceonds depuis le 1er
# janvier 1970 à 00:00)
dt = datetime.fromtimestamp(52 * 365.25 * 86400)
dt

# %%
dt = datetime.now()
# %%
# exploitation des objets datetime
dt.year, dt.month, dt.second # ...
dt.date(), dt.time()
# lundi: 0 => dimanche: 6
dt.weekday()
dt.timestamp()

# formatage en chainede caractère
# "f" comme format
dt.strftime("%d/%m/%Y")
dt.strftime("%A")

# %%
# arithmétique de dates

new_year = datetime(2023, 1, 1)

delta = new_year - datetime.now()
delta.days

# dates négatives ???
delta = datetime.now() - new_year
delta

cuisson_oeuf_coque = timedelta(minutes=3)
atable = datetime.now() + cuisson_oeuf_coque
atable
# %%

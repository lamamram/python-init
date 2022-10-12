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
date_str = "2022-10-12 11:52"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt

# %%
dt = datetime.fromtimestamp(52 * 365.25 * 86400)
dt

# %%
datetime.now()
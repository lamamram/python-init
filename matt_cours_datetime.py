# %%
# import calendar
# lire une dt
from datetime import datetime, timedelta

dt = datetime(2024, 4, 11)

dt.weekday()

dt.now()

dt = datetime.now()

# "f" comme format
dt.strftime("%d/%m/%Y %H:%M")

# nb de secondes depuis le 1er janvier 1970 à minuit
# temps UNIX
dt.timestamp()

# %%
# écrire (créer)
# "p" comme "parse"
dt = datetime.strptime("2024-04-08", "%Y-%m-%d")

dt = datetime.fromtimestamp(54 * 365.25 * 86400)
dt

# %%

dt = datetime.now()

delta = dt - datetime(2024, 4, 8, 9, 30)
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60
remain_sec =  (delta.seconds % 3600) % 60

f"{delta.days} d, {hours} h, {minutes} m, {remain_sec} s"

# %%

dt = datetime.now()
cuisson_oeuf_coque = timedelta(minutes=3)

dt + cuisson_oeuf_coque

# %%

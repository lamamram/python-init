# %%
# écrire une fonction time_remaining dans le module misc de utils
# qui prend en paramètres les heures et minutes de la fin aujourd'hui (17:00)
# et les heures et minutes de la pause cet arès moidi (15:45)
# qui présente une boucle infinie (while True:)
# dans laquelle on regarde toutes les minutes pour
#   - afficher le temps restant en heure minutes secondes
#   - afficher "c'est la pause" entre le début de la pause et + 15 min
# à la fin, casser la boucle infinie
# pour tester, préférer la commande python dans le terminal

# hint: se donner le datetime auj à 17:00 et auj à 15:45
# 1. calculer le temps restant tout seul
# 2. gérer le message si pause
# 3. gérer l'interruption du programme
# 4. gérer la boucle

from datetime import datetime, timedelta


def today_at(h, m):
    today = datetime.now()
    return datetime(
        today.year, 
        today.month, 
        today.day,
        h,
        m
    )
fin_h, fin_m = 17, 0
pause_h, pause_m = 14, 15

fin = today_at(fin_h, fin_m)
pause = today_at(pause_h, pause_m)
fin_pause = pause + timedelta(minutes=15)
now = datetime.now()
    # now - début n'est pas négatif & fin - now idem
if (now - pause).days > -1 and (fin_pause - now).days > -1:
    print("c'est la pause !")
else:
    remains = fin - datetime.now()
    remain_hour = remains.seconds // 3600
    remain_min = (remains.seconds % 3600) // 60
    remain_sec = remains.seconds % 60
    print(f"il reste {remain_hour}h, {remain_min}mn et {remain_sec}s avant {fin_h}:{fin_m:02d}")
# %%
# %%

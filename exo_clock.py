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

from utils.misc import remaining_time
remaining_time(fin_tup=(17, 0), pause_tup=(15, 45), tick=10)
# %%

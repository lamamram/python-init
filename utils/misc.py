"""
modules contenant des fonctions de manipulation de texte
- strip_little_words
- get_occurences
"""
from datetime import datetime, timedelta
from time import sleep
if __name__ == "__main__":
    # si on veut tester le module depuis
    # le package (pas conseillé)
    from helpers import to_lower, today_at
else:
    # les imports sont calculés depuis
    # le dossier du programme principal
    # (dossier racine du projet)
    # "chemin absolu depuis la racine"
    from utils.helpers import to_lower, today_at
    # "chemin relatif"
    # "." désigne le package courant
    from .helpers import to_lower, today_at

PI = 3.14

def strip_lil_words(text, min_length=4):
    """
    nettoie un texte des mots inférieur à un paramètre
    """
    return to_lower(" ".join(filter(
        lambda w: len(w) >= min_length, 
        text.split()
    )))

def get_occurences(text: str):
    occ = {}
    for w in text.split():
        if w not in occ: occ[w] = 1
        else: occ[w] += 1
    return occ

def remaining_time(fin_tup: tuple, pause_tup: tuple, tick=60):
    """
    time remaining before end of working day
    """
    fin_h, fin_m = fin_tup
    pause_h, pause_m = pause_tup

    fin = today_at(fin_h, fin_m)
    pause = today_at(pause_h, pause_m)
    fin_pause = pause + timedelta(minutes=15)
    while True:
        now = datetime.now()
        # now - début n'est pas négatif & fin - now idem
        # if (now - pause).days > -1 and (fin_pause - now).days > -1:
        if pause <= now < fin_pause:
            print("c'est la pause !")
        else:
            remains = fin - datetime.now()
            # après la fin
            if remains.days == -1:
                print("DING DONG")
                break
            remain_hour = remains.seconds // 3600
            remain_min = (remains.seconds % 3600) // 60
            remain_sec = remains.seconds % 60
            print(f"il reste {remain_hour}h, {remain_min}mn et {remain_sec}s avant {fin_h}:{fin_m:02d}")
        sleep(tick)


if __name__ == "__main__":
    print(strip_lil_words("à bon chat bon rat"))


# %%
# mécanisme de capture
# try teste les instruction dans son bloc
# dès qu'une erreur est rencontrée,
# le bloc s'interromp et on exécute le bloc except
try:
    3/0
    print("coucou")
    {}["k"]
except:
    print("exception capturée")

# %%
# Exception est la classe mère des exceptions
# capture toutes les classes filles
# on peut exploiter l'objet exception généré
try:
    3/0
    print("coucou")
    {}["k"]
except Exception as e:
    print(f"exception capturée: {e, e.args[0], type(e)}")

# %%
# traitements spécifiques en fonction de l'erreur
# plusieurs bloc except, examinés de haut en bas
# quand une erreur survient
try:
    denom, dico = 0, {}
    # 3/denom
    print("coucou")
    dico["k"]
    1 + " tiens vaut mieux que " + 2
except ZeroDivisionError as ze:
    denom = 1
    print(3/denom)
# un bloc except peut capturer plusieurs exceptions
# pour le même traitement
except (KeyError, TypeError) as ke:
    print(dico.get("k", "v"))
    print("un tiens vaut mieux que 2 ...")
except Exception as e:
    print(f"exception capturée: {e, e.args[0], type(e)}")

# modus operandi
# 1. placer try/excpet avec Exception => capture tout
# 2. tamiser avec les traitements spécifiques certaines exceptions
# %%
# else et finally
import sys

try:
    # denom, dico, un, deux = 1, {"k": "v"}, "un", "deux"
    denom, dico, un, deux = 1, {}, "un", "deux"
    3/denom
    dico["k"]
    chaine = un + " tiens vaut mieux que " + deux
    print("coucou")
    sys.exit(0)
except Exception as e:
    print(f"exception capturée: {e, e.args[0], type(e)}")
    sys.exit(0)
# else s'exécute si le bloc try s'exécute jusqu'au bout
# s'il n'ya pas d'exceptions levées
else:
    print(3/denom, dico["k"], chaine)
# s'exécute même en cas d'exception 
# ou de sortie du programme 
finally:
    print("whatever it takes")

print("suite du programme")
# %%
# lancer des exceptions

def avg_notes(notes: list):
    ## gestion naive
    # if not notes: return "vide !"
    # for note in notes:
    #     if not isinstance(note, (float, int)): return f"{note} pas un nb !"
    #     if not 0 <= note <= 20: return f"{note} pas dans [0, 20] !" 
    
    ## exception
    if not notes: raise ZeroDivisionError("liste vide !")
    for note in notes:
        if not isinstance(note, (float, int)): 
            raise TypeError(f"{note} pas un nb !")
        if not 0 <= note <= 20: 
            raise ValueError(f"{note} pas dans [0, 20] !")
    return round(sum(notes)/len(notes), 1)

if __name__ == "__main__":
    try:
        avg_notes([0, 15, 20])
        # avg_notes(["bla", "bli", "blo"])
        # avg_notes([])
        # avg_notes([0, 15, 22])
    except Exception as e:
        print(e)

# %%

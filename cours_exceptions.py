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

# %%

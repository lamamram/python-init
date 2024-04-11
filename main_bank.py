# %%
from bank.account import BankAccount
from bank.client import Client

# print("coucou")

if __name__ == "__main__":
    # le bloc try essaie d'exécuter tout le bloc
    # 1/ pas d'erreur on continue sans exécuter le ou les except
    try:
        cl = Client(132423423, "LAMAMRA", "matt", "Apr 11th 1983")
        acc = BankAccount(34534544, cl, 500.)

        print(acc.get_client_name())
        acc.check_birth_date()
        print(acc.get_balance())
    # le bloc except interrompt le code sans faire planter en exécutant le bloc associé
    # si une erreur de type ValueError dans le bloc try
    # as va permettre d'exploiter l'objet de type XXXError
    except ValueError as e:
        print(e)
    except TypeError as te:
        print(te)
    # capture toutes les erreurs
    except Exception as all_exc:
        print(all_exc)
# %%

# %%
from bank.account import BankAccount
from bank.client import Client

# print("coucou")

if __name__ == "__main__":
    try:
        cl = Client(132423423, "LAMAMRA", "matt", "1983-04-01")
        acc = BankAccount(34534544, cl, 500.)

        print(acc.get_client_name())
        acc.check_birth_date()
        print(acc.get_balance())
    except ValueError as e:
        print(e)
# %%

from bank.account import BankAccount
from bank.client import Client

print("coucou")

if __name__ == "__main__":
    cl = Client(132423423, "LAMAMRA", "matt", "13/02/1983")
    acc = BankAccount(34534544, cl, 500.)

    print(acc.get_client_name())
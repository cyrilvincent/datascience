# Créer la classe BankAccount
# Créer les attributs dans le constructeur
# Créer les méthodes
# Vérifications fonctionnelles
# Exceptions (bonus) try except raise
# Bonus : Gérer la class Transaction

import datetime

class BankAccount:

    def __init__(self, owner, bank):
        self.owner = owner
        self.bank = bank
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount))
        else:
            raise ValueError("Amount must be > 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(-amount))
            return amount
        else:
            raise ValueError("Amount must be >0 and <balance")

class Transaction:

    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.datetime.now()

if __name__ == '__main__':
    account1 = BankAccount("Cyril","Bank")
    account1.deposit(100)
    account1.withdraw(30)
    print(account1.balance)
    try:
        account1.withdraw(100000)
    except ValueError as ve:
        print(ve)

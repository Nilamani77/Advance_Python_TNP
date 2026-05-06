# single inheritance

class Account:
    def __init__(self, account_holder, balance):
        self.acoount_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f"Acoount holder:{self.account_holder}")
        print(f"balance:{self.balance}")


class Saving_account(Account):
    def __init__(self,account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance*(self.interest_rate/100)
        return interest

    def show_balance(self):
        super().show_balance()
        interest = self.calculate_interest()
        print(f"Interest:${interest}")
        print(f"Total Balance:{self.balance+interest}")

account = Saving_account("Nilamani",2000,5)

account.show_balance()

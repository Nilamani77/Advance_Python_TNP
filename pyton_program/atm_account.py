class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print("-", t)


accounts = {}

def create_account():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    accounts[acc_no] = Account(acc_no, name, balance)
    print("Account created successfully.")

def access_account():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found.")
        return

    account = accounts[acc_no]

    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            break

        else:
            print("Invalid option.")


while True:
    print("\n=== ATM System ===")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        create_account()

    elif option == "2":
        access_account()

    elif option == "3":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice.")

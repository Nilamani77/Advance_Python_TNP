print("Welcome to Gietu Bank")

balance = 1000.0
transaction = []

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            transaction.append(f"Deposit: ${amount:.2f}")
            print("Deposit successful!")
        else:
            print("Amount must be positive.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            transaction.append(f"Withdraw: ${amount:.2f}")
            print("Withdrawal successful!")

    elif choice == '3':
        print(f"Current Balance: ${balance:.2f}")

    elif choice == '4':
        print("\nTransaction History:")
        if len(transaction) == 0:
            print("No transactions yet.")
        else:
            for t in transaction:
                print("-", t)

    elif choice == '5':
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Try again.")

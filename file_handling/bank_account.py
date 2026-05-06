

def create_account():
    try:
        name = input("Enter Your Name: ")
        balance = input("Enter Your Balance: ")

        if not name or not balance:
            print("All fields are required!")
            return

        balance = int(balance)

        file = open("account.txt", "w")
        file.write(f"{name},{balance}")
        file.close()

        print("✅ Account created successfully")

    except ValueError:
        print("Balance must be a number!")
    except Exception as e:
        print("Error:", e)


def check_balance():
    try:
        file = open("account.txt", "r")
        content = file.read()

        if content == "":
            print("No record found!")
        else:
            name, balance = content.split(",")
            print(f"\nName: {name}")
            print(f"Balance: {balance}")

        file.close()

    except FileNotFoundError:
        print("File not found. No account exists.")



def deposit_money():
    try:
        deposit_name = input("Enter Name: ")

        file = open("account.txt", "r+")
        data = file.read()

        if data == "":
            print("No record found!")
            file.close()
            return

        name, balance = data.split(",")

        if name != deposit_name:
            print("Account not found!")
            file.close()
            return

        amount = int(input("Enter amount to deposit: "))
        new_balance = int(balance) + amount

        file.seek(0)
        file.write(f"{name},{new_balance}")
        file.truncate()
        file.close()

        print("✅ Money deposited successfully")
        print("Updated Balance:", new_balance)

    except ValueError:
        print("Amount must be a number!")
    except FileNotFoundError:
        print("File not found.")

def withdraw():
    try:
        withdraw_name = input("Enter Name: ")

        file = open("account.txt", "r+")
        data = file.read()

        if data == "":
            print("No record found!")
            file.close()
            return

        name, balance = data.split(",")

        if name != withdraw_name:
            print("Account not found!")
            file.close()
            return

        amount = int(input("Enter amount to withdraw: "))

        if amount > int(balance):
            print("❌ Insufficient Balance!")
            file.close()
            return

        new_balance = int(balance) - amount

        file.seek(0)
        file.write(f"{name},{new_balance}")
        file.truncate()
        file.close()

        print("✅ Money withdrawn successfully")
        print("Updated Balance:", new_balance)

    except ValueError:
        print("Amount must be a number!")
    except FileNotFoundError:
        print("File not found.")




def main():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

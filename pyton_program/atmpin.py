def atm_pin_validation():
    correct_pin = "1234"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        user_input = input("Enter your PIN: ")

        if user_input == correct_pin:
            print("Welcome to your account ✅")
            return  
        else:
            attempts += 1
            attempts_left = max_attempts - attempts

            if attempts_left > 0:
                print(f"Invalid PIN ❌. Attempts left: {attempts_left}")
            else:
                print("Too many incorrect attempts 🚫. Your account is now blocked.")

atm_pin_validation()

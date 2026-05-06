file_name = "parking_records.txt"

while True:
    print("\n--- Parking Lot Management ---")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show Parking Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vehicle = input("Enter Vehicle Number: ")
        time = input("Enter Entry Time: ")

        with open(file_name, "a") as file:
            file.write(vehicle + "," + time + ",IN\n")

        print("Vehicle Entry Recorded Successfully.")


    elif choice == "2":
        vehicle = input("Enter Vehicle Number: ")
        time = input("Enter Exit Time: ")

        with open(file_name, "a") as file:
            file.write(vehicle + "," + time + ",OUT\n")

        print("Vehicle Exit Recorded Successfully.")

    elif choice == "3":
        print("\n--- Parking Records ---")

        try:
            with open(file_name, "r") as file:
                records = file.readlines()

                if len(records) == 0:
                    print("No records found.")
                else:
                    for record in records:
                        print(record.strip())

        except FileNotFoundError:
            print("No records file found.")


    elif choice == "4":
        print("Exiting System...")
        break

    else:
        print("Invalid choice. Try again.")
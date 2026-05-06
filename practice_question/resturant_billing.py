menu = {
    1: ("Pizza", 250),
    2: ("Burger", 120),
    3: ("Pasta", 180),
    4: ("Cold Drink", 60)
}

gst_rate = 0.05  
total = 0
bill_items = []

print("------ Restaurant Menu ------")
for key, value in menu.items():
    print(f"{key}. {value[0]} - ₹{value[1]}")

while True:
    try:
        item_no = int(input("\nEnter item number (0 to finish): "))
        
        if item_no == 0:
            break

        if item_no not in menu:
            print("Invalid item number. Try again.")
            continue

        qty = int(input("Enter quantity: "))

        item_name, price = menu[item_no]
        cost = price * qty
        total += cost

        bill_items.append((item_name, qty, cost))

    except ValueError:
        print("Please enter valid numbers.")


gst = total * gst_rate
final_bill = total + gst


print("\n------ Final Bill ------")
for item in bill_items:
    print(f"{item[0]} x {item[1]} = ₹{item[2]}")

print("------------------------")
print(f"Total: ₹{total}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")
print("------------------------")
print("Thank you! Visit Again 😊")
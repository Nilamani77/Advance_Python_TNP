# import random

# while True:
#     n = int(input("Enter number of players: "))
#     players = {}

#     for i in range(n):
#         name = input("Enter player name: ")
#         players[name] = 0

#     print("\nRolling Dice 5 Times...\n")

#     for name in players:
#         total = 0
#         print(name, "rolls:", end=" ")

#         for i in range(5):
#             roll = random.randint(1, 5)
#             print(roll, end=" ")
#             total += roll

#         players[name] = total
#         print("-> Total:", total)

#     max_score = max(players.values())

#     print("\nResult:")
#     for name in players:
#         if players[name] == max_score:
#             print("Winner is", name, "with score", max_score)

#     again = input("\nPlay again? (yes/no): ")
#     if again.lower() != "yes":
#         print("Game Over!")
#         break

def descending_order(num):
    digits = str(num)                
    sorted_digits = sorted(digits, reverse=True) 
    return int("".join(sorted_digits))  
print(descending_order(73398))
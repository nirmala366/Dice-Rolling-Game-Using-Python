import random

while True:
    chioce = input("Roll The Dice? (Y/N): ").lower()
    if chioce == "y" :
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif chioce == "n":
        print("Thank you for playing!!")
        break
    else :
        print("Invalid Choice")
'''

Project 3C

Slot Machine

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

import random


def slot_machine():
    words = ["Cherry", "Orange", "Plums", "Bell", "Melon", "Bar"]
    total_money_inserted = 0
    total_money_won = 0

    print("Welcome to the Slot Machine Game!")

# game loop
    while True:
        # prompt user for money
        try:
            money_inserted = float(input("Enter the amount of money you want to use: $"))
            if money_inserted <= 0:
                print("Enter a positive amount.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        #add money to total
        total_money_inserted += money_inserted

        # generate random results
        results = [random.choice(words) for _ in range(3)]
        print("Slot Machine Results: ", results)

        # determine winnings
        if results[0] == results[1] == results[2]:
            winnings = money_inserted * 3
            print(f"Congratulations! All three words match. You win ${winnings:.2f}.")
        elif results[0] == results[1] or results[1] == results[2] or results[0] == results[2]:
            winnings = money_inserted * 2
            print(f"Congratulations! Two words match. You win ${winnings:.2f}.")
        else:
            winnings = 0
            print("Sorry, no matches. You win $0.")

        # add winnings to total
        total_money_won += winnings

        # prompt user to play again?
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break

    print(f"Total money entered into the slot machine: ${total_money_inserted:.2f}")
    print(f"Total money won: ${total_money_won:.2f}")

# Run the slot machine
slot_machine()

'''

Project 3B

Number Guessing Game

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

import random

# generate number
def generate_random_number():
    return random.randint(1, 100)

# prompt user to guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

# give feedback
def give_feedback(guess, target):
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct!")

# game loop
def play_game():
    target_number = generate_random_number()
    guess = None
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != target_number:
        guess = get_user_guess()
        give_feedback(guess, target_number)
    
    print(f"Congratulations! You guessed the number!")

if __name__ == "__main__":
    play_game()

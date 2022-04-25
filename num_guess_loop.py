#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This is a guess the number game

# Importing the random module
import random


def main():
    # Generate the random number
    random_number = random.randint(0, 9)

    # Greet the user
    print("This is a number guessing game.")

    while True:
        # Ask user for input
        user_input = input("Enter a number between 0 and 9: ")

        try:
            # Cast user input to a integer
            user_num = int(user_input)

            # Check if they guessed correctly or not
            if user_num == random_number:
                print("You guessed correctly!")
                break
            else:
                print("You guessed wrong. Please try again.")
                continue
        except:
            # In case the user input a value other than a number
            print("Invalid Input. Please try again.")
            continue


if __name__ == "__main__":
    main()
